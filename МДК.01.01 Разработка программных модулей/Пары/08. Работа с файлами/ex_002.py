# Через контекстный менеджер with as
with open('Пара 8. Работа с файлами/file2.txt', 'w', encoding="UTF-8") as file:
    file.write('Очень важное сообщение')

with open('Пара 8. Работа с файлами/file2.txt', 'r', encoding="UTF-8") as file:
    print(file.read())
