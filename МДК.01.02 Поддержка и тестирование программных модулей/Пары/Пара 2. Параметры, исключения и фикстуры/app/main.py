import json

# Выгрузка из JSON
def load_books(file_path):
    with open(file_path, 'r', encoding="UTF-8") as file:
        return json.load(file)

# Выгрузка в JSON
def save_books(file_path, books):
    with open(file_path, 'w', encoding="UTF-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=2)

# Добавление книжки
def add_book(file_path, book):
    books = load_books(file_path)
    books.append(book)
    save_books(file_path, books)
    return book

# Удаление книжки
def delete_book(file_path, book_id):
    books = load_books(file_path)
    new_books = [book for book in books if books[id] != book_id]
    save_books(file_path, new_books)
    return new_books

# Изменение книжки
def update_book(file_path, book_id, update_data):
    books = load_books(file_path)
    for book in books:
        if book['id'] == book_id:
            book.update(update_data)
            save_books(file_path, books)
            return True
    return None

# Поиск
def find_book(file_path, book_title):
    books = load_books(file_path)
    for book in books:
        if book['title'] == book_title:
            return book
    return None