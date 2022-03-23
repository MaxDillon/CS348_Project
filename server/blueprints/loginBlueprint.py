

from flask import Blueprint, make_response, request
from login.login import get_accounts, login_required, login_user, logout_user, get_tokens
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


	@loginBlueprint.route('/isLoggedIn', methods=['GET'])
	@login_required(MakeSession)
	def isLoggedIn(user_id=None):
		resp = make_response({
			'message': 'Success'
		})
		resp.status_code = 200
		return resp
		

	@loginBlueprint.route('/logout', methods=['GET'])
	@login_required(MakeSession)
	def logout(user_id=None):
		resp = make_response()
		resp.status_code = 200
		with MakeSession() as session:
			logout_user(resp, user_id, session)

		return resp

	@loginBlueprint.route('/getAccounts', methods=['GET'])
	def getAccounts(user_id=None):
		with MakeSession() as session:
			resp = make_response(get_accounts(session))
		resp.status_code = 200

		return resp


	@loginBlueprint.route('/getTokens', methods=['GET'])
	def getTokens(user_id=None):
		with MakeSession() as session:
			resp = make_response(get_tokens(session))
		resp.status_code = 200

		return resp


	return loginBlueprint