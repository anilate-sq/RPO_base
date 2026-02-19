import psycopg2

# Тут реализуется подключение к базе
def get_conn():
        pass

'''
Пример

def get_conn():
        return psycopg2.connect(
        host='localhost',
        port=5432,
        user='postgres',
        password='password',
        database='db_name',
        client_encoding='utf-8'
        ) 
''' 