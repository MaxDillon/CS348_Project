
import json
import sys
from flask import Blueprint, make_response, request
from soupsieve import select
from auth.login import login_user
from auth.logout import logout_user
from auth.register import register_account
from auth.auth_tools import get_accounts, get_tokens, get_user, login_required, check_loggedin_token
from sqlalchemy.orm import sessionmaker
from database.schema import t_transactions

from database.schema import Employee



def create_blueprint(MakeSession: sessionmaker):
	transactionBlueprint = Blueprint('transactionBlueprint', __name__)

	@transactionBlueprint.route('/getTransactions', methods=['GET'])
	def getTransactions():
		resp = make_response()

		with MakeSession() as session:
			user = get_user(session)

			user: Employee


		resp.set_data(json.dumps({
			"data": [{id: 1, }]
		}))

		return resp


	return transactionBlueprint