

import sys
from sqlalchemy import Column, MetaData, Table, create_engine, String
import typing

import sqlalchemy

def init_database():
	engine = create_engine('postgresql://postgres:postgres@postgres:5432/postgres', echo=True)
	return engine


def execute_query(database, sql):
	result = database.execute(sql)
	for r in result:
		print(r, file=sys.stderr)



def print_customers(database: sqlalchemy.engine.Engine):
	meta = MetaData(database)
	user_table = Table('', meta, 
		Column('user_id', String),
		Column('username', String),
		Column('first_name', String),
		Column('last_name', String),
		Column('email', String),
		Column('phone', sqlalchemy.Integer),
		Column('pass_hash', String),
		Column('money_invested', sqlalchemy.Integer)
	)

	with database.connect() as conn:
		conn: sqlalchemy.engine.Connection
		result = conn.execute(user_table.select())
		for r in result:
			print(r, file=sys.stderr)
