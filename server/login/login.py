from datetime import timedelta
from multiprocessing import connection
import secrets
import bcrypt
import sys
from flask import make_response, redirect, request
import sqlalchemy

from functools import wraps

from datetime import datetime

from database.DatabaseEndpoint import DatabaseEndpoint


def compare_passwords(passHashString, bcryptPassword):
	passHashBytes = passHashString.encode("utf-8")
	return bcrypt.checkpw(passHashBytes, bcryptPassword)


def get_user_data(username, database, connection):
	account = database.account
	account_query = sqlalchemy.select([account]).where(account.columns.username == username)

	this_account = connection.execute(account_query).fetchone()

	if this_account is None:
		return None
	
	return {key: value for key, value in this_account.items()}
	

def generate_auth_cookie(resp, user_id, database, connection):
	token = secrets.token_hex(32).encode('utf-8')

	query = sqlalchemy.insert(database.session).values(
		user_id=user_id,
		token=token
	)
	connection.execute(query)

	resp.set_cookie(
		key='token',
		value=token,
		expires=datetime.now() + timedelta(days=1),
		secure=True,
		httponly=True
	)


def login_user(resp, username, password, database: DatabaseEndpoint):
	connection = database.connect()
	user_data = get_user_data(username, database, connection)

	if user_data is None or not compare_passwords(password, user_data.get("pass_hash")):
		return False


	user_id = user_data.get("user_id")
	generate_auth_cookie(resp, user_id, database, connection)
	return True



def logout_user(resp, user_id, database: DatabaseEndpoint):
	token = request.cookies.get('token')
	resp.delete_cookie('token')
	connection = database.connect()
	session_table = database.session
	session_query = sqlalchemy.delete(session_table).where(session_table.columns.token == token.encode('utf-8'))
	connection.execute(session_query)


def encode_password(password):
	passwordEncode = password.encode("utf-8")
	bcryptHash = bcrypt.hashpw(passwordEncode, bcrypt.gensalt())
	return bcryptHash



def get_accounts(database: DatabaseEndpoint):
	connection = database.connect()
	account_table = database.account
	account_query = sqlalchemy.select([account_table])
	accounts = connection.execute(account_query).fetchall()

	return {
		'data':[
			{key: str(value) for key, value in account.items()}
			for account in accounts
		]
	}

def validate_token(token, database: DatabaseEndpoint):
	if token is None:
		return None
	connection = database.connect()
	session_table = database.session
	session_query = sqlalchemy.select([session_table]).where(session_table.columns.token == token.encode('utf-8'))
	this_session = connection.execute(session_query).fetchone()
	if this_session is None:
		return None
	
	return {key: value for key, value in this_session.items()}

def login_required(database):
	def _wrapped_decorator(func):
		@wraps(func)
		def _wrapper(*args, **kwargs):

			cookie_token = request.cookies.get('token')
			cookie_username = request.cookies.get('username')
			
			user_info = validate_token(cookie_token, database)

			if user_info is None: # or cookie_username != user_info.get('username'):
				resp = make_response({'message': 'Incorrect Auth Token'})
				resp.status_code = 401
				return resp
			user_id = user_info.get('user_id')
			return func(*args, user_id=user_id, **kwargs)
		return _wrapper
	return _wrapped_decorator


