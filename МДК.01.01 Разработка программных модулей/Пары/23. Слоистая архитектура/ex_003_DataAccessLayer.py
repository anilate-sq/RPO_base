# data_layer/db.py
# Пример на базе SQLite, а не PostgreSQL
import sqlite3

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
    
    def connect(self):
        # Подключение к БД
        self.connection = sqlite3.connect(self.db_name)
        self.connection.row_factory = sqlite3.Row
        return self.connection
    
    def close(self):
        # Закрытие подключения
        if self.connection:
            self.connection.close()
    
    # Данные, которые будут изначально в приложении можно загрузить в него сразу
    def get_all_books(self):
        # Получение книг
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM books')
        return cursor.fetchall()
    
    def add_book(self, title, author, year):
        # Добавление книжки
        cursor = self.connection.cursor()
        cursor.execute(
            'INSERT INTO books (title, author, year) VALUES (?, ?, ?)',(title, author, year)
        )
        self.connection.commit()
        return cursor.lastrowid # Вернуть елемент с последним id
    
    def delete_book(self, book_id):
        # Удаление книжки
        cursor = self.connection.cursor()
        cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
        self.connection.commit()