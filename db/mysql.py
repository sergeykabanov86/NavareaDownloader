from venv import create

import pymysql
from pymysql import err
from redis.cluster import get_connection

from config import host, user, password, db_name, port

def create_connection(host=host, port = port, user= user, password = password, db_name = db_name) -> pymysql.connect:
    try:
        if(db_name):
            connection = pymysql.connect(
                host=host,
                port = port,
                user = user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
        else:
            connection = pymysql.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                cursorclass=pymysql.cursors.DictCursor
            )
        print('Connection to db successfully !')
    except Exception as ex:
        print(f'Connection error {ex} occured !')
    finally:
        pass
    return connection


def test_connection()->bool:
    print('Testing connection ...')
    res = False
    try:
        conn = create_connection(host, port, user, password, None)
        print('Test connection success!')
        res = True
    except Exception as ex:
        print(f'Test connection failed!\n{ex}')
        res = False
    finally:
        conn.close()
        print('Connection closed.')
    return res

def create_db_schema():
    print(f'Creating database {db_name} ...')
    sql = f'CREATE DATABASE {db_name} DEFAULT CHARACTER SET utf8 DEFAULT ENCRYPTION="N";'
    try:
        drop_db_schema()
        conn = create_connection(host, port, user, password, db_name=None)
        with conn.cursor() as cursor:
            cursor.execute(sql)
        print(f'Database {db_name} created!')
    except Exception as ex:
        print(f'Create database {db_name} error!\n{ex}')
    finally:
        conn.close()

def drop_db_schema():
    print('Dropping database ...')
    sql = f'DROP DATABASE IF EXISTS {db_name}'
    try:
        conn = create_connection(host, port, user, password, None)
        with conn.cursor() as cursor:
            cursor.execute(sql)
        print('Database dropped.')
    except Exception as ex:
        print(f'DROP Database {db_name} failed!\n{ex}')
    finally:
        conn.close()

def create_table_users():
    print('\nCreate table "users"')
    sql_query = ("CREATE TABLE IF NOT EXISTS  users (id int AUTO_INCREMENT PRIMARY KEY, " 
                                                    "name varchar(128), " 
                                                    "phone varchar(16), "
                                                    "email varchar(128));")
    print('sql', sql_query)
    try:
        conn = create_connection()
        with conn.cursor() as cursor:
            cursor.execute(sql_query)

        print('Table users has been created!')
    except Exception as ex:
        print(f'Запрос на добавление таблицы пользователей выдал ошибку!\n{ex}')
    finally:
        conn.close()

def create_table_navarea_versions():
    print(f'Creating table "version" of navarea ...')
    sql = ("CREATE TABLE versions (id int PRIMARY KEY, "
                                   "name varchar(16);")
    try:
        conn = create_connection()
        with conn.cursor() as cursor:
            cursor.execute(sql)
        print(f'Create table "versions" of navarea success!')
    except Exception as ex:
        print(f'Create table "versions" of navarea error!\n{ex}')
    finally:
        conn.close()

def add_table_navarea_versions_data():
    pass

def create_database():
    if (test_connection() is False): return;
    create_db_schema()
    create_table_users()
    create_table_navarea_versions()




def main():
    test_connection()
    create_database()






if __name__ == '__main__':
   main()