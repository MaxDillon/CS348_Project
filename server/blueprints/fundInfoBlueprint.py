
import json
import sys
from flask import Blueprint, make_response, request
import flask
from auth.login import login_user
from auth.logout import logout_user
from auth.register import register_account
from auth.auth_tools import get_accounts, get_tokens, get_user, login_required, check_loggedin_token
from sqlalchemy.orm import sessionmaker, Session
from database.schema import t_transactions #import the fund info table from the schema.py
from sqlalchemy import select
from database.schema import Employee


def create_blueprint(MakeSession: sessionmaker):
	fundInfoBlueprint = Blueprint('fundInfoBlueprint', __name__)

	@fundInfoBlueprint.route('/getFunds', methods=['GET'])
	def getFunds():
		#resp = make_response()

		session:Session = MakeSession()

		transactionHistory = select(t_transactions.columns.fund_name,t_transactions.columns.fund_description,t_transactions.columns.parent_company,t_transactions.columns.fund_value,t_transactions.columns.fund_invested)
		#
        historyDetails = session.execute(transactionHistory).all()
		response = [x._asdict() for x in historyDetails]
		res = flask.make_response(flask.jsonify(response), 200)
		session.close()
		#print(res)
		return res


	return transactionBlueprint

