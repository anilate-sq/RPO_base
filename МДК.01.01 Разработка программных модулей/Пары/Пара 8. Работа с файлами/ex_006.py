with open('Пара 8. Работа с файлами/file3.txt', 'a', encoding="UTF-8") as file:
    file.write('\nСообщение')

with open('Пара 8. Работа с файлами/file.txt', 'x', encoding='UTF-8') as file:
    file.write('ТЕКСТ')