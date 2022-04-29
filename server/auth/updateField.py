import json
import bcrypt
import sys
from flask import Response
from sqlalchemy import select, update
from sqlalchemy.orm import Session
from database.schema import Account
from auth.crypto import encode_password, generate_auth_cookie


def update_account(account: Account, fieldName, fieldVal, session: Session):
    print(f"set {fieldName} to {fieldVal}", sys.stderr)
    
    setattr(account, fieldName, fieldVal)
    session.commit()
