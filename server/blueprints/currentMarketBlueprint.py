import sys
from flask import Blueprint, make_response, request
from auth.login import login_user
from auth.logout import logout_user
from auth.register import register_account
from auth.auth_tools import (
    get_accounts,
    get_tokens,
    login_required,
    check_loggedin_token,
)
from auth.market import get_market_data
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
import json


def create_blueprint(MakeSession: sessionmaker):
    currentMarketBlueprint = Blueprint("currentMarketBlueprint", __name__)

    @currentMarketBlueprint.route("/getMarket", methods=["GET"])
    def getMarket():
        resp = make_response()

        with MakeSession() as session:
            allCompanies = get_market_data(session)

        print(allCompanies, file=sys.stderr)
        results = [
            {
                "company_id": result.company_id,
                "company_name": result.company_name,
                "current_trading_price": result.current_trading_price,
                "num_shares": result.num_shares,
            }
            for result in allCompanies
        ]

        resp.set_data(json.dumps({"data": results}))

        return resp

    return currentMarketBlueprint
