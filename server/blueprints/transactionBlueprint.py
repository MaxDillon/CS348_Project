
import json
import sys
from flask import Blueprint, make_response, request
import flask
from auth.login import login_user
from auth.logout import logout_user
from auth.register import register_account
from auth.auth_tools import get_accounts, get_tokens, get_user, login_required, check_loggedin_token
from sqlalchemy.orm import sessionmaker, Session
from database.schema import t_transactions
from sqlalchemy import select
from database.schema import Employee


def create_blueprint(MakeSession: sessionmaker):
	transactionBlueprint = Blueprint('transactionBlueprint', __name__)

	@transactionBlueprint.route('/getTransactions', methods=['GET'])
	def getTransactions():
		resp = make_response()

		session:Session = MakeSession()

		# with MakeSession() as session:
		user = get_user(session)
	#	print("User->\t", user, flush=True)
	#	print("hello!!!  ", user.user_id, flush=True)

		numb = user.user_id
		transactionHistory = select(t_transactions.columns.company_id,t_transactions.columns.num_shares,t_transactions.columns.buy_or_sell,t_transactions.columns.time_executed).filter(t_transactions.columns.user_id == numb)
		historyDetails = session.execute(transactionHistory).all()
	#	print("response: ",historyDetails)
		response = [x._asdict() for x in historyDetails]
	#	print("response: ",response)
		res = flask.make_response(flask.jsonify(response), 200)
		session.close()

		return resp


	return transactionBlueprint

