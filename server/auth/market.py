import bcrypt
from flask import Response, request
from sqlalchemy import select
from sqlalchemy.orm import Session
from database.schema import Company, Loginsession

def get_market_data(session: Session):
    account_query = select(Company.company_id, Company.company_name, Company.current_trading_price, Company.num_shares)
    this_account = session.execute(account_query).all()
    return this_account