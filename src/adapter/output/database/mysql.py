import os

from mysql.connector import connect
from urllib.parse import urlparse


class Mysql:

    _instance = None
    connection = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def _connect(self):
        if self.connection is None:
            is_development = os.getenv("FLASK_ENV") == "development"
            if is_development:
                host = os.getenv("DB_HOST")
                user = os.getenv("DB_USER")
                pwd = os.getenv("DB_PWD")

            host = self._parse_host(host)

            self.connection = connect(
                host=host,
                user=user,
                password=pwd,
                port=os.getenv("DB_PORT"),
                database=os.getenv("DB_NAME"),
            )

    @staticmethod
    def _parse_host(host):
        if not host.startswith("jdbc:"):
            return host
        url = urlparse(host.replace("jdbc:", ""))
        return url.hostname

    @classmethod
    def fetchall(cls, sql):
        db = cls.instance()
        db._connect()
        with db.connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

    @classmethod
    def upsert(cls, sql):
        db = cls.instance()
        db._connect()
        with db.connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql)
            db.connection.commit()
            return (cursor.rowcount, 'rows affeted')
