# coding: utf-8
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, LargeBinary, String, Table, text
from sqlalchemy.dialects.postgresql import MONEY
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
    phone = Column(String(250))
    pass_hash = Column(LargeBinary, nullable=False)
    money_invested = Column(Integer, nullable=False, server_default=text("0"))


class Company(Base):
    __tablename__ = 'company'

    company_id = Column(String(250), primary_key=True)
    company_name = Column(String(250), nullable=False)
    current_trading_price = Column(MONEY, nullable=False)
    num_shares = Column(Integer, nullable=False)


class Employee(Base):
    __tablename__ = 'employee'

    employee_id = Column(Integer, primary_key=True, server_default=text("nextval('employee_employee_id_seq'::regclass)"))
    username = Column(String(250), nullable=False)
    first_name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250))
    phone = Column(String(250))
    pass_hash = Column(LargeBinary, nullable=False)

    managers = relationship(
        'Employee',
        secondary='manages',
        primaryjoin='Employee.employee_id == manages.c.employee_id',
        secondaryjoin='Employee.employee_id == manages.c.manager_id'
    )


t_companyhistory = Table(
    'companyhistory', metadata,
    Column('company_id', ForeignKey('company.company_id', ondelete='CASCADE', onupdate='CASCADE')),
    Column('time_fetched', DateTime, nullable=False),
    Column('trading_price', MONEY, nullable=False)
)


class Loginsession(Base):
    __tablename__ = 'loginsession'

    token = Column(LargeBinary, primary_key=True)
    user_id = Column(ForeignKey('account.user_id', ondelete='CASCADE', onupdate='CASCADE'))
    time_created = Column(DateTime)

    user = relationship('Account')


t_manages = Table(
    'manages', metadata,
    Column('manager_id', ForeignKey('employee.employee_id', ondelete='CASCADE', onupdate='CASCADE')),
    Column('employee_id', ForeignKey('employee.employee_id', ondelete='CASCADE', onupdate='CASCADE'))
)


t_paymenthistory = Table(
    'paymenthistory', metadata,
    Column('user_id', ForeignKey('account.user_id', ondelete='CASCADE', onupdate='CASCADE')),
    Column('time_created', DateTime, nullable=False),
    Column('amount_invested', Integer, nullable=False)
)


t_transactions = Table(
    'transactions', metadata,
    Column('company_id', ForeignKey('company.company_id', ondelete='CASCADE', onupdate='CASCADE')),
    Column('user_id', ForeignKey('account.user_id', ondelete='CASCADE', onupdate='CASCADE')),
    Column('time_executed', DateTime, nullable=False),
    Column('num_shares', Integer, nullable=False),
    Column('buy_or_sell', Boolean, nullable=False)
)
