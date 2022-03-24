from datetime import timedelta
import json
import secrets
import bcrypt
import sys
from flask import Response, make_response, request
import sqlalchemy
from sqlalchemy import select, delete, String
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.sql import cast
from functools import wraps
from database.schema import Account, Loginsession
from datetime import datetime



def compare_passwords(passHashString, bcryptPassword):
	passHashBytes = passHashString.encode("utf-8")
	return bcrypt.checkpw(passHashBytes, bcryptPassword)


def get_user_data(username, session: Session):
	account_query = select(Account.user_id, Account.pass_hash).where(Account.username == username)
	this_account = session.execute(account_query).one_or_none()

	return dict(this_account) if this_account is not None else None
		

def generate_auth_cookie(resp, user_id: str, session: Session):
	token = secrets.token_hex(32).encode('utf-8')

	new_login_session = Loginsession(user_id=user_id, token=token, create_time=datetime.now())
	session.add(new_login_session)
	session.commit()

	resp.set_cookie(
		key='token',
		value=token,
		expires=datetime.now() + timedelta(days=1),
		secure=True,
		httponly=True
	)


def login_user(resp, username, password, session: Session):
	user_data = get_user_data(username, session)

	if user_data is None or not compare_passwords(password, user_data.get("pass_hash")):
		return False
	user_id = user_data.get("user_id")

	generate_auth_cookie(resp, user_id, session)
	return True


def encode_password(password: str):
	passwordEncode = password.encode("utf-8")
	bcryptHash = bcrypt.hashpw(passwordEncode, bcrypt.gensalt())
	return bcryptHash


def register_account(resp: Response, email, username, password, session: Session):
	username_query = select(Account.username).where(Account.username == username)
	username_exists = session.execute(username_query).one_or_none()
	print(username_exists, file=sys.stderr)
	email_query = select(Account.email).where(Account.email == email)
	email_exists = session.execute(email_query).one_or_none()

	if username_exists is not None:
		resp.set_data(json.dumps({'message': 'username already exists'}))
		resp.status_code = 401;
		return resp
	if email_exists is not None:
		resp.set_data(json.dumps({'message': 'email already exists'}))
		resp.status_code = 401;
		return resp
	
	new_account = Account(email=email, username=username, pass_hash=encode_password(password))
	session.add(new_account)
	session.commit()

	user_id_query = select(Account.user_id).where(Account.username == username)
	user_id = session.execute(user_id_query).one()[0]
	print(user_id, file=sys.stderr)

	generate_auth_cookie(resp, user_id, session)
	return resp



def logout_user(resp, session: Session):
	token = request.cookies.get('token').encode('utf-8')
	resp.delete_cookie('token')

	# login_session_query = select(Loginsession).where(Loginsession.token == token.encode('utf-8'))
	# login_session = session.execute(login_session_query).one()
	delete_login_session = delete(Loginsession).where(Loginsession.token == token).execution_options(synchronize_session="fetch")
	session.execute(delete_login_session)
	session.commit()



def get_accounts(session: Session):
	account_query = select(Account.user_id, Account.username, cast(Account.pass_hash, String).label("pass_hash"))
	accounts = session.execute(account_query).all()

	return {'data':[dict(account) for account in accounts]}



def get_tokens(session: Session):
	session_query = select(cast(Loginsession.token, String).label("token"), Loginsession.user_id)
	login_sessions = session.execute(session_query).all()

	return {'data':[ dict(login_session) for login_session in login_sessions]}



def check_loggedin_token(token, session: Session):
	if token is None:
		return False

	session_query = select(Loginsession).where(Loginsession.token == token.encode('utf-8'))
	this_session = session.execute(session_query).one_or_none()

	# return dict(this_session) if this_session is not None else None 
	return this_session is not None

		

def login_required(MakeSession: sessionmaker):
	def _wrapped_decorator(func):
		@wraps(func)
		def _wrapper(*args, **kwargs):

			cookie_token = request.cookies.get('token')
			cookie_username = request.cookies.get('username')
			
			with MakeSession() as session:
				is_logged_in = check_loggedin_token(cookie_token, session)

			if not is_logged_in: # or cookie_username != user_info.get('username'):
				resp = make_response({'message': 'Incorrect Auth Token'})
				resp.delete_cookie('token')
				resp.status_code = 401
				return resp
			return func(*args, **kwargs)
		return _wrapper
	return _wrapped_decorator


