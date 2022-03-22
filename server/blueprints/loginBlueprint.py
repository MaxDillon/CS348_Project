

from flask import Blueprint, make_response, request
from login.login import get_accounts, login_required, login_user, logout_user, get_tokens



def create_blueprint(database):
	loginBlueprint = Blueprint('loginBlueprint', __name__)

	@loginBlueprint.route('/login', methods=['POST'])
	def login():
		resp = make_response()
		data = request.get_json()
		username = data.get('username')
		password = data.get('password')

		success = login_user(resp, username, password, database)

		if not success:
			resp.status_code = 401
			# resp.set_data({'message': 'Username or Password were Incorrect'})
		else:
			resp.status_code = 200
		return resp


	@loginBlueprint.route('/isLoggedIn', methods=['GET'])
	@login_required(database)
	def isLoggedIn(user_id=None):
		resp = make_response({
			'message': 'Success'
		})
		resp.status_code = 200
		return resp
		

	@loginBlueprint.route('/logout', methods=['GET'])
	@login_required(database)
	def logout(user_id=None):
		resp = make_response()
		resp.status_code = 200
		logout_user(resp, user_id, database)

		return resp

	@loginBlueprint.route('/getAccounts', methods=['GET'])
	def getAccounts(user_id=None):
		resp = make_response(get_accounts(database))
		resp.status_code = 200

		return resp


	@loginBlueprint.route('/getTokens', methods=['GET'])
	def getTokens(user_id=None):
		resp = make_response(get_tokens(database))
		resp.status_code = 200

		return resp


	return loginBlueprint