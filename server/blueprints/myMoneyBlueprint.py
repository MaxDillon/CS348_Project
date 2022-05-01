from datetime import datetime, timedelta
import json
import sys
from flask import Blueprint, make_response, request
from auth.auth_tools import get_user
from sqlalchemy.orm import sessionmaker

from info.user_info import get_past_holding_dump


def create_blueprint(MakeSession: sessionmaker):
    myMoneyBlueprint = Blueprint("myMoneyBlueprint", __name__)

    @myMoneyBlueprint.route("/pastHoldings", methods=["GET"])
    def pastHoldings():

        resp = make_response()
        time_end = datetime.now()

        time_start = datetime.now() - timedelta(days=14365)

        with MakeSession() as session:
            account = get_user(session)
            data = get_past_holding_dump(session, account, time_start, time_end)


        resp.set_data(
            json.dumps("asdfa")
        )

        return resp

    return myMoneyBlueprint
