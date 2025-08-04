#__all__ - указывает на разрешенные для импорта функции
__all__ = ['create']
from typing import Any

import pymysql
from pymysql import Connection
from pymysql.cursors import Cursor

from settings import host, password, user, db, port


def create(db_host=host, db_port=port, db_name=db, db_user=user, db_password=password) -> pymysql.Connection:
    print(f"user: {db_user} password: {db_password} host:{db_host}  db_name:{db_name}")
    try:
        connection = pymysql.connect(
            host=db_host,
            port=db_port,
            database=db_name,
            user=db_user,
            password=db_password,
            cursorclass=pymysql.cursors.DictCursor
        )
        print(f'Подключение к БД выполнено успешно!')
        return connection
    except Exception as ex:
        print(f'Ошибка подключения к базе данных: {ex}')





if __name__ == '__main__':
    create()
