import secrets
import bcrypt
from datetime import timedelta
from sqlalchemy.orm import Session
from functools import wraps
from database.schema import Loginsession
from datetime import datetime


def encode_password(password: str):
	passwordEncode = password.encode("utf-8")
	bcryptHash = bcrypt.hashpw(passwordEncode, bcrypt.gensalt())
	return bcryptHash

def compare_passwords(passHashString, bcryptPassword):
	passHashBytes = passHashString.encode("utf-8")
	return bcrypt.checkpw(passHashBytes, bcryptPassword)


def generate_auth_cookie(resp, user_id: str, session: Session):
	token = secrets.token_hex(32).encode('utf-8')

	new_login_session = Loginsession(user_id=user_id, token=token, time_created=datetime.now())
	session.add(new_login_session)
	session.commit()

	resp.set_cookie(
		key='token',
		value=token,
		expires=datetime.now() + timedelta(days=1),
		secure=True,
		httponly=True
	)
