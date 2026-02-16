import psycopg


def get_conn():
    # Прямое соединение с PostgreSQL через psycopg (v3)
    return psycopg.connect(
        host='localhost',
        port=5432,
        user='postgres',
        password='123',
        dbname='rpo_db'
    )
