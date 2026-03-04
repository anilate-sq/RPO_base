'''
Модуль для работы с данными
Data Access Layer(DAL)
Адаптировано под PostgreSQL + psycopg2
'''

import psycopg2
from psycopg2 import sql, extras
from psycopg2.extras import RealDictCursor
from typing import List, Optional, Dict, Any
from contextlib import contextmanager

class Database:
    # Класс для работы с базой данных
    
    # Конфигурация по умолчанию
    DEFAULT_CONFIG = {
        'host': 'localhost',
        'port': 5432,
        'database': 'library',
        'user': 'postgres',
        'password': 'password'
    }

    def __init__(self, config: Optional[Dict[str, any]] = None):
        '''
        Инициализация подключения
        Args:
            config: Словарь с параметрами подключения
        '''
        self.config = {**self.DEFAULT_CONFIG, **{config or {}}}
        self.connection = None
    
    def connect(self):
        # Подключение
        try:
            self.connection = psycopg2.connect(
                host=self.config['host'],
                port=self.config['port'],
                database=self.config['database'],
                user=self.config['user'],
                password=self.config['password']
            )
            return self.connection
        except psycopg2.Error as e:
            print('Ошибка подключение к БД', e)
            raise

    def close(self):
        # Закрытие подключения
        if self.connection:
            self.connection.close()
            self.connection = None
    
    @contextmanager
    def cursor(self, dict_cursor=True):
        '''
        Котнекстный менеджер для курсора
        Args:
            dict_cursor: Если True, использует RealDictCursor(возвращает словари)
        Yields:
            Курсор базы данных
        '''
        if not self.connection:
            self.connect()
        
        cursor_type = RealDictCursor if dict_cursor else psycopg2.cursor
        cursor = self.connection.cursor(cursor_factory=cursor_type)
        try:
            yield cursor
        finally:
            cursor.close()

    def init_database(self):
        # Тут создаем БД, на случай если её нет
        pass

    def get_all_books(self) -> List[Dict]:
        #  Получение всех книг
        with self.cursor() as cur:
            cur.execute('''
                select id, title, author, year, genre, is_available from books order by title;
            ''')
            return cur.fetchall()
        
    def get_book_by_id(self, book_id: int) -> Optional[Dict]:
        # Получение книги по её ID
        with self.cursor() as cur:
            cur.execute('''
            select id, title, author, year, genre, is_available from books where id = %s
            ''', (book_id,))
            return cur.fetchone()
        
    def get_book_by_author(self, author: str) -> List[Dict]:
        # Получение книги по Автору
        with self.cursor() as cur:
            cur.execute(
                '''
                select id, title, author, year, genre, is_available
                from books
                where author like %s
                order by title
                ''', (f'%{author}%')
            )
            return cur.fetchall()