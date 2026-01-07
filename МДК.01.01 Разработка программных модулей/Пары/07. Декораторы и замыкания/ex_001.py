# Пример простого замыкания
def outer():
    message = 'Какое-то сообщение'
    # Создаем замыкание
    def inner():
        print(message)
    return inner

result = outer()
result()