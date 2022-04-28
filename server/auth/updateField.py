import json
import bcrypt
import sys
from flask import Response
from sqlalchemy import select, update
from sqlalchemy.orm import Session
from database.schema import Account
from auth.crypto import encode_password, generate_auth_cookie


def update_account(resp: Response, userid, fieldName, fieldVal, session: Session):
    upd = update(Account)
    upd = upd.values({fieldName: fieldVal})
    upd = upd.where(Account.user_id == userid)
    session.execute(upd)
    session.commit()

    return resp
