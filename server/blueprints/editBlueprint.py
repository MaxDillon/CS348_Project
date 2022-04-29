import json
import sys
from flask import Blueprint, make_response, request
from auth.login import login_user
from auth.logout import logout_user
from auth.updateField import update_account
from auth.auth_tools import (
    get_accounts,
    get_tokens,
    get_user,
    login_required,
    check_loggedin_token,
)
from sqlalchemy.orm import sessionmaker
from database.schema import Account, t_transactions

from database.schema import Employee


def create_blueprint(MakeSession: sessionmaker):
    editBlueprint = Blueprint("editBlueprint", __name__)

    @editBlueprint.route("/getUser", methods=["GET"])
    def getUser():
        resp = make_response()

        with MakeSession() as session:
            user = get_user(session)

        resp.set_data(
            json.dumps(
                {
                    "username": user.username,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                    "phone": user.phone,
                }
            )
        )

        return resp

    @editBlueprint.route("/update", methods=["post"])
    def updateField():
        resp = make_response()
        data = request.get_json()
        fieldName = data.get("fieldName")
        fieldVal = data.get("fieldVal")

        with MakeSession() as session:
            user: Account = get_user(session)

            update_account(user, fieldName, fieldVal, session)

        return resp

    return editBlueprint
