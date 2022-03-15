

import sys
from sqlalchemy import Column, MetaData, Table, create_engine, String
from sqlalchemy.inspection import inspect
import typing

import sqlalchemy

def init_database():
	engine = create_engine('postgresql://postgres:postgres@postgres:5432/postgres') #, echo=True)
	return engine


def _json_from_result_set(result_set, table=None):

	return {
		'result': [
			{key: value for key, value in r.items()}
			for r in result_set
		],
		'table': table
	}


def execute_query(engine, sql):
	result = engine.execute(sql)
	return _json_from_result_set(result)





def print_customers(engine):
	connection = engine.connect()
	metadata = sqlalchemy.MetaData()
	customer = Table('customer', metadata, autoload=True, autoload_with=engine)
	query = sqlalchemy.select([customer]) 

	resultProxy = connection.execute(query)
	resultSet = resultProxy.fetchall()

	return _json_from_result_set(resultSet, customer.name)


