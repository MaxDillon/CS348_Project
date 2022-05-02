import sys
import typing
from retry import retry

import sqlalchemy
from sqlalchemy import Column, MetaData, Table, create_engine, String
from sqlalchemy.inspection import inspect

from sqlalchemy.engine.base import Engine

# from sqlalchemy.engine.result import ResultProxy
# from sqlalchemy.engine.result import RowProxy


class DatabaseEndpoint:
    @retry(delay=1)
    def __init__(self):
        self.metadata = sqlalchemy.MetaData()
        self.engine: Engine = create_engine(
            "postgresql://postgres:postgres@postgres:5432/postgres"
        )

        self.account = Table(
            "account", self.metadata, autoload=True, autoload_with=self.engine
        )
        self.session = Table(
            "session", self.metadata, autoload=True, autoload_with=self.engine
        )

    def connect(self):
        return self.engine.connect()

    def execute_query(self, sql):
        result = self.execute(sql)
        return self._json_from_result_set(result)

    def _json_from_result_set(self, result_set, table=None):
        return {
            "result": [
                {key: str(value) for key, value in r.items()} for r in result_set
            ],
            "table": table,
        }
