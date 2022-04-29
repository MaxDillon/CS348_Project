import json
import bcrypt
import sys
from flask import Response
from sqlalchemy import select
from sqlalchemy.orm import Session
from database.schema import Account
from auth.crypto import encode_password, generate_auth_cookie


def register_account(resp: Response, email, username, password, session: Session):
    username_query = select(Account.username).where(Account.username == username)
    username_exists = session.execute(username_query).one_or_none()

    email_query = select(Account.email).where(Account.email == email)
    email_exists = session.execute(email_query).one_or_none()

    if username_exists is not None:
        resp.set_data(json.dumps({"message": "username already exists"}))
        resp.status_code = 401
        return resp
    if email_exists is not None:
        resp.set_data(json.dumps({"message": "email already exists"}))
        resp.status_code = 401
        return resp

    new_account = Account(
        email=email, username=username, pass_hash=encode_password(password)
    )
    session.add(new_account)
    session.commit()

    user_id_query = select(Account.user_id).where(Account.username == username)
    user_id = session.execute(user_id_query).one()[0]

    generate_auth_cookie(resp, user_id, session)
    return resp
