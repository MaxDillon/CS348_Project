from datetime import timedelta
import secrets
import bcrypt
import sys
from flask import make_response, request
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


def login_user(resp, username, password, MakeSession: sessionmaker):
	with MakeSession() as session:
		session: Session
		user_data = get_user_data(username, session)

		if user_data is None or not compare_passwords(password, user_data.get("pass_hash")):
			return False
		user_id = user_data.get("user_id")

		generate_auth_cookie(resp, user_id, session)
		return True



def logout_user(resp, user_id, MakeSession: sessionmaker):
	token = request.cookies.get('token')
	resp.delete_cookie('token')

	with MakeSession() as session:
		session: Session
		del_login_session = delete(Loginsession).where(Loginsession.token == token.encode('utf-8')).execution_options(synchronize_session="fetch")
		session.execute(del_login_session)
		session.commit()


def encode_password(password):
	passwordEncode = password.encode("utf-8")
	bcryptHash = bcrypt.hashpw(passwordEncode, bcrypt.gensalt())
	return bcryptHash



def get_accounts(MakeSession: sessionmaker):
	with MakeSession() as session:
		session: Session
		account_query = select(Account.user_id, Account.username, cast(Account.pass_hash, String).label("pass_hash"))
		accounts = session.execute(account_query).all()

		return {'data':[dict(account) for account in accounts]}



def get_tokens(MakeSession: sessionmaker):
	with MakeSession() as session:
		session: Session
		session_query = select(cast(Loginsession.token, String).label("token"), Loginsession.user_id)
		login_sessions = session.execute(session_query).all()

		return {'data':[ dict(login_session) for login_session in login_sessions]}



def validate_token(token, MakeSession: sessionmaker):
	if token is None:
		return None
	with MakeSession() as session:
		session: Session
		session_query = select(Loginsession.user_id).where(Loginsession.token == token.encode('utf-8'))
		this_session = session.execute(session_query).one_or_none()


		return dict(this_session) if this_session is not None else None 

		
def login_required(MakeSession: sessionmaker):
	def _wrapped_decorator(func):
		@wraps(func)
		def _wrapper(*args, **kwargs):

			cookie_token = request.cookies.get('token')
			cookie_username = request.cookies.get('username')
			
			user_info = validate_token(cookie_token, MakeSession)

			if user_info is None: # or cookie_username != user_info.get('username'):
				resp = make_response({'message': 'Incorrect Auth Token'})
				resp.delete_cookie('token')
				resp.status_code = 401
				return resp
			user_id = user_info.get('user_id')
			return func(*args, user_id=user_id, **kwargs)
		return _wrapper
	return _wrapped_decorator


