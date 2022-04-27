import sys
from flask import make_response, request
from sqlalchemy import select, String
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.sql import cast
from functools import wraps
from database.schema import Account, Loginsession



def get_accounts(session: Session):
	account_query = select(Account.user_id, Account.username, cast(Account.pass_hash, String).label("pass_hash"))
	accounts = session.execute(account_query).all()

	return {'data':[dict(account) for account in accounts]}



def get_tokens(session: Session):
	session_query = select(cast(Loginsession.token, String).label("token"), Loginsession.user_id)
	login_sessions = session.execute(session_query).all()

	return {'data':[ dict(login_session) for login_session in login_sessions]}


def get_user(session: Session) -> Account:
	token = request.cookies.get("token")
	if (token == None):
		return None
	session_query = select(Account).join(Loginsession).where(Loginsession.token == token.encode('utf-8'))
	print(session_query, file=sys.stderr)
	this_session = session.execute(session_query).one_or_none()

	return this_session.Account


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


