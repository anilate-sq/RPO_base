from main import(
    load_books,
    save_books,
    add_book,
    delete_book,
    update_book,
    find_book
)

def test_load_books(temp_books_file):
    books = load_books(temp_books_file)
    assert len(books) == 2
    assert books[0]["title"] == 'Dune'

def test_add_book(temp_books_file):
    new = {"id": 3, "title": "Lord of Rings", "author": "George Tolkien"}
    add_book(temp_books_file, new)
    books = load_books(temp_books_file)
    assert len(books) == 3
    assert books[-1]["title"] == "Lord of Rings" 

# Самостоятельно дописать тесты на удаление, изменение и поиск и прикрепить скриншоты выполненных тестов