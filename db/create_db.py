from pygments.lexer import using

from db import connection
from settings import db


def drop_db():
    try:
        print(f'Удаляем базу данных {db} ...')
        conn = connection.create(db_name='sys')
        with conn.cursor() as cursor:
            sql = f"DROP DATABASE IF EXISTS `{db}`;"
            cursor.execute(sql)
        print(f'База данных {db} удалена!')
    except Exception as ex:
        print(f'Не удалось удалить БД {db}', ex, sep='\n')



def create_db():
    try:
        print(f'Создаем базу данных {db} ...')
        conn = connection.create(db_name= "sys")
        with conn.cursor() as cursor:
            sql = f'CREATE DATABASE IF NOT EXISTS `{db}`;'
            cursor.execute(sql)
            print(f'База данных {db} создана!')


    except Exception as ex:
        print(f'Не удалось создать базу данных {db}!', ex, sep='\n')







if __name__ == '__main__':
    drop_db()
    create_db()