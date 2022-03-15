
from datetime import datetime, timedelta
from functools import wraps
import json
import sys
from flask import Blueprint, make_response, redirect, request
from login.validatePassword import validatePassword, validateToken


def login_required(database):
	def _wrapped_decorator(func):
		@wraps(func)
		def _wrapper(*args, **kwargs):

			sessionCookie = request.cookies.get('token')
			user_info = validateToken(sessionCookie, database)

			if user_info is None:
				return redirect("", 401)
			username = user_info.get('username')
			return func(*args, username, **kwargs)
		return _wrapper
	return _wrapped_decorator


def create_blueprint(database):
	loginBlueprint = Blueprint('loginBlueprint', __name__)

	@loginBlueprint.route('/login', methods=['POST'])
	def login():
		resp = make_response()
		data = request.get_json()
		username = data.get('username')
		password = data.get('passHash')
		token = validatePassword(username, password, database)
		if token is None:
			resp.status_code = 401
			resp.set_data({})
			return resp
		resp.status_code = 200
		resp.set_cookie(
			key='token',
			value=token,
			expires=datetime.now() + timedelta(days=1),
			secure=True,
			httponly=True
		)
		resp.set_data({})
		return resp


	@loginBlueprint.route('/testRequired', methods=['GET'])
	@login_required(database)
	def testRequired(username):
		resp = make_response({'username': username})
		return resp



	@loginBlueprint.route('/logout', methods=['GET'])
	@login_required(database)
	def logout(username):
		resp = make_response({'question': 'success'})
		resp.delete_cookie('token')
		return resp
	
	return loginBlueprint