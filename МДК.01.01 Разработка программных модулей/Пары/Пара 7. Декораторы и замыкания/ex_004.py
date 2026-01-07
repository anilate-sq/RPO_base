# Пример с использованием параметров
def logger(func):
    def innerFunc(*args, **kwargs):
        print(f'Вызываем функцию {func.__name__} с аргументами {args} и {kwargs}')
        result = func(*args, **kwargs)
        print(result)
        return result
    return innerFunc

# Создаем декоратор
@logger
def sum(a, b):
    return a + b

sum(5, 7)