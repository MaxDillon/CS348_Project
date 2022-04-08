

import sys
from flask import Blueprint, make_response, request
from auth.login import login_user
from auth.logout import logout_user
from auth.register import register_account
from auth.auth_tools import get_accounts, get_tokens, login_required, check_loggedin_token
from sqlalchemy.orm import sessionmaker



def create_blueprint(MakeSession: sessionmaker):
	loginBlueprint = Blueprint('loginBlueprint', __name__)

	@loginBlueprint.route('/login', methods=['POST'])
	def login():
		resp = make_response()
		data = request.get_json()
		username = data.get('username')
		password = data.get('password')

		with MakeSession() as session:
			success = login_user(resp, username, password, session)

		if not success:
			resp.status_code = 401
			# resp.set_data({'message': 'Username or Password were Incorrect'})
		else:
			resp.status_code = 200
		return resp

	@loginBlueprint.route('/register', methods=['post'])
	def register():
		resp = make_response()
		data = request.get_json()
		email = data.get('email')
		username = data.get('username')
		password = data.get('password')

		with MakeSession() as session:
			resp = register_account(resp, email, username, password, session)

		return resp
		

	@loginBlueprint.route('/isLoggedIn', methods=['GET'])
	def isLoggedIn():
		cookie_token = request.cookies.get('token')
		with MakeSession() as session:
			answer = check_loggedin_token(cookie_token, session)
		resp = make_response({
			'answer': answer
		})
		resp.status_code = 200
		return resp
		

	@loginBlueprint.route('/logout', methods=['GET'])
	@login_required(MakeSession)
	def logout():
		resp = make_response()
		resp.status_code = 200
		with MakeSession() as session:
			logout_user(resp, session)
		return resp

	@loginBlueprint.route('/getAccounts', methods=['GET'])
	def getAccounts():
		with MakeSession() as session:
			resp = make_response(get_accounts(session))
		resp.status_code = 200

		return resp


	@loginBlueprint.route('/getTokens', methods=['GET'])
	def getTokens():
		with MakeSession() as session:
			resp = make_response(get_tokens(session))
		resp.status_code = 200

		return resp


	return loginBlueprint