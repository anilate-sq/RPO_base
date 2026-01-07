import pytest
from module import(
    add,
    sub,
    div
)

def test_func():
    assert add(2, 3) == 5

def test_func2():
    assert add(6, 3) == 9

def test_func3():
    assert sub(5, 3) == 2

def test_func3():
    assert sub(14, 3) == 10

# Использование параметров
# @pytest.mark.parametrize - создание параметров для теста

@pytest.mark.parametrize("a, b, result", [
    (2, 3, 5),
    (6, 3, 9),
    (5, 3, 8)
])
def test_add(a, b, result):
    assert add(a, b) == result

@pytest.mark.parametrize("a, b, result", [
    (3, 2, 1),
    (12, 3, 9),
    (92, 14, 78)
])
def test_sub(a, b, result):
    assert sub(a, b) == result

# Исключения
def test_div():
    with pytest.raises(ZeroDivisionError):
        div(123, 0)
    
@pytest.mark.parametrize("a, b", [
    (3, 0),
    (12, 3),
    (92, 0)
])
def test_param_div(a, b):
    with pytest.raises(ZeroDivisionError):
        div(a, b)

# Фикстура - заготовка для теста
def test_fixture(music_data):
    assert music_data[0]["name"] == 'track_1'
    assert len(music_data) > 1

# В идеале фикстуры нужно создавать в отдельном файле conftest.py