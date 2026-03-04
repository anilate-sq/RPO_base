# bussines_layer/services.py

# from data_layer.database import Database - так будет в проекте
from ex_003_DataAccessLayer import Database

class BookService:
    def __init__(self, database):
        self.db = database
    
    def get_all_books(self):
        # Получение книжек
        return self.db.get_all_books()
    
    def add_book(self, title, author, year):
        '''
        Добавление книги с проверками
        Возвращает: (Положительно: bool, Данные: str)
        '''

        # Проверка 1. Название не пустое
        if not title or not title.strip():
            return False, "Название книги не может быть пустым"
        
        # Проверка 2. Автор не пустой
        if not author or not author.strip():
            return False, "Автор не должен быть пустым"
        
        # Проверка 3. Корректный год
        current_year = 2026
        if not isinstance(year, int) or year < 0 or year > current_year:
            return False, "Год должен быть от 0 до {current_year}"
        
        # Если проверки выполнились, то добавляем в базу
        book_id = self.db.add_book(title.strip(), author.strip(), year)
        return True, f"Книга добавлена, её ID: {book_id}"
    
    def delete_book(self, book_id):
        # Удаление книги
        if not isinstance(book_id, int) or book_id <= 0:
            return False, "Некорректный ID"
        
        self.db.delete_book(book_id)
        return True, "Книга удалена"