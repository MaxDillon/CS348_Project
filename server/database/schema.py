# coding: utf-8
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, LargeBinary, String, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Account(Base):
    __tablename__ = 'account'

    user_id = Column(Integer, primary_key=True, server_default=text("nextval('account_user_id_seq'::regclass)"))
    username = Column(String(250), nullable=False)
    first_name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250))
    phone = Column(Integer)
    pass_hash = Column(LargeBinary, nullable=False)
    money_invested = Column(Integer, nullable=False, server_default=text("0"))


class Fundinformation(Base):
    __tablename__ = 'fundinformation'

    order_id = Column(Integer, primary_key=True)
    fund_name = Column(String(250), nullable=False)
    free_money = Column(Integer, nullable=False)
    keywords = Column(String(250), nullable=False)
    fund_value = Column(Integer, nullable=False)


class Holding(Base):
    __tablename__ = 'holding'

    company_id = Column(Integer, primary_key=True)
    company_name = Column(String(250), nullable=False)
    stocks = Column(Integer, nullable=False)
    buying_val = Column(Integer, nullable=False)


class Market(Base):
    __tablename__ = 'market'

    company_id = Column(Integer, primary_key=True)
    market_name = Column(String(250), nullable=False)
    total_stocks = Column(Integer, nullable=False)
    trading_price = Column(Integer, nullable=False)


class Transactionhistory(Base):
    __tablename__ = 'transactionhistory'

    company_id = Column(Integer, primary_key=True)
    executed_by = Column(String(250), nullable=False)
    buy_sell = Column(Boolean, nullable=False)
    number = Column(Integer, nullable=False)


class Loginsession(Base):
    __tablename__ = 'loginsession'

    token = Column(LargeBinary, primary_key=True)
    user_id = Column(ForeignKey('account.user_id', ondelete='CASCADE', onupdate='CASCADE'))
    create_time = Column(DateTime, nullable=False)

    user = relationship('Account')
