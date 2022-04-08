import bcrypt
from flask import Response, request
from sqlalchemy import select
from sqlalchemy.orm import Session
from database.schema import Account, Loginsession
from auth.crypto import generate_auth_cookie, compare_passwords



def get_user_data(username, session: Session):
	account_query = select(Account.user_id, Account.pass_hash).where(Account.username == username)
	this_account = session.execute(account_query).one_or_none()

	return dict(this_account) if this_account is not None else None
		

def login_user(resp: Response, username, password, session: Session) -> bool:
	user_data = get_user_data(username, session)

	if user_data is None or not compare_passwords(password, user_data.get("pass_hash")):
		return False
	user_id = user_data.get("user_id")

	generate_auth_cookie(resp, user_id, session)
	return True
