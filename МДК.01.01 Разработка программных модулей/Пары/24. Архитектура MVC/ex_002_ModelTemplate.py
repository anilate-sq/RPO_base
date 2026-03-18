# Пример модели

class BookModel:
    def __init__(self, title, ):
        self.book = []

    def add_book(self, title, author, year, genre):
        self.books.append({
            'id': len(self.books) + 1,
            'title': title,
            'author': author,
            'year': year,
            'genre': genre
        })

    def update_book(self, book_id, title, author, year, genre):
        pass

    def delete_book(self, book_id):
        pass

# В проецировании на слоистую архитектуру, это что-то вроде Data Layer + Business Layer