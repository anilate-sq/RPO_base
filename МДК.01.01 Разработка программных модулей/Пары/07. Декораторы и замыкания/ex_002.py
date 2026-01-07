# Создаем замыкание
def power(value):
    def inner(base):
        return base ** value
    return inner

# Пример использования замыканий
square = power(2)
print('Первый вызов:', square(2)) 
cube = power(3)
print('Второй вызов:', cube(2))
