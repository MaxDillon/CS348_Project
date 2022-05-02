from datetime import datetime, timedelta
import json
import sys
from flask import Blueprint, make_response, request
from auth.auth_tools import get_user
from sqlalchemy.orm import sessionmaker

from info.user_info import get_past_holdings


def create_blueprint(MakeSession: sessionmaker):
    myMoneyBlueprint = Blueprint("myMoneyBlueprint", __name__)

    @myMoneyBlueprint.route("/pastHoldings", methods=["GET"])
    def pastHoldings():

        resp = make_response()
        time_end = datetime.now().timestamp()

        time_start = (datetime.now() - timedelta(days=(365 * 2))).timestamp()

        with MakeSession() as session:
            account = get_user(session)
            times, values = get_past_holdings(
                session, account, time_start, time_end
            )

        resp.set_data(json.dumps({"times": times, "values": values}, indent=4))

        return resp

    return myMoneyBlueprint
