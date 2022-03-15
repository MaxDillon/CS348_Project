
from datetime import datetime, timedelta
from functools import wraps
import json
from flask import Blueprint, make_response, redirect, request
from login.validatePassword import validatePassword
import secrets
loginBlueprint = Blueprint('loginBlueprint', __name__)

logged_in = {}

@loginBlueprint.route('/getDate', methods=['GET'])
def getDate():
	now = datetime.now()
	return {
		'date': now
	}

def login_required(function_to_protect):
	@wraps(function_to_protect)
	def wrapper(*args, **kwargs):
		sessionCookie = request.cookies.get('token')
		username = logged_in.get(sessionCookie)
		if username == None:
			return redirect("",401)
		else:
			return function_to_protect(*args, **kwargs)
	return wrapper




@loginBlueprint.route('/login', methods=['POST'])
def login():
	resp = make_response()
	data = request.get_json()
	username = data.get('username')
	password = data.get('passHash')
	token = validatePassword(username, password)
	if token is None:
		resp.status_code = 401
		resp.set_data(json.dumps(token))
		return resp


	resp.set_cookie(
		key = 'token', 
		value = token['token'],
		secure=True,
		expires=datetime.now() + timedelta(days=1),
		httponly=True
	)
	logged_in[token['token']] = username
	resp.set_data(json.dumps(token))
	return resp


@loginBlueprint.route('/testRequired', methods=['GET'])
@login_required
def testRequired():
	resp = make_response({'question': 'success'})
	return resp



@loginBlueprint.route('/logout', methods=['GET'])
@login_required
def logout():
	resp = make_response({'question': 'success'})
	resp.delete_cookie('token')
	return resp