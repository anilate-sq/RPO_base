import json
import pytest

# Фикстура для организации json-файла
@pytest.fixture
def temp_books_file(tmp_path):
    books = [
        {"id": 1, "title": "Dune", "author": "Frank Gerbert"},
        {"id": 2, "title": "1984", "author": "George Oruell"}
    ]
    file = tmp_path / 'books.json'
    file.write_text(json.dumps(books, ensure_ascii=False, indent=2))
    return str(file)