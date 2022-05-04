import json
import sys
from flask import Blueprint, make_response, request
import flask
from auth.login import login_user
from auth.logout import logout_user
from auth.register import register_account
from auth.auth_tools import (
    get_accounts,
    get_tokens,
    get_user,
    login_required,
    check_loggedin_token,
)
from sqlalchemy.orm import sessionmaker, Session

# import the fund info table from the schema.py
from database.schema import Fundinfo, t_transactions
from sqlalchemy import select
from database.schema import Employee


def create_blueprint(MakeSession: sessionmaker):
    fundInfoBlueprint = Blueprint("fundInfoBlueprint", __name__)

    @fundInfoBlueprint.route("/getFunds", methods=["GET"])
    def getFunds():
        # resp = make_response()

        session: Session = MakeSession()

        fundHistory = select(
            Fundinfo.fund_name,
            Fundinfo.fund_description,
            Fundinfo.parent_company,
            Fundinfo.fund_value,
            Fundinfo.fund_invested,
        )

        # import the fund info table from the schema.py
        historyDetails = session.execute(fundHistory).one_or_none()
        print("Answer: ", historyDetails, flush=True)
        # response = [x for x in historyDetails]
        response = historyDetails._asdict()
        res = flask.make_response(flask.jsonify(response), 200)
        session.close()
        return res

    return fundInfoBlueprint
