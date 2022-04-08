
from flask import Response, request
from sqlalchemy import delete
from sqlalchemy.orm import Session
from database.schema import Account
from database.schema import Account, Loginsession


def logout_user(resp: Response, session: Session):
	token = request.cookies.get('token').encode('utf-8')
	resp.delete_cookie('token')
	delete_login_session = delete(Loginsession).where(Loginsession.token == token).execution_options(synchronize_session="fetch")
	session.execute(delete_login_session)
	session.commit()