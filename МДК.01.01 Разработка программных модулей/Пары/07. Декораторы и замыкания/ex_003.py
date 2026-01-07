def decorator(func):
    def innerFunc():
        print('До вызова функции')
        func()
        print('После вызова функции')
    return innerFunc



@decorator
def message():
    print('Отправка сообщения')

message = decorator(message) # Старье
message()