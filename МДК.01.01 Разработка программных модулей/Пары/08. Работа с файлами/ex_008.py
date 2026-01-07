try:
    with open('Пара 8. Работа с файлами/file.txt', 'x', encoding='UTF-8') as file:
        file.write('ТЕКСТ')
except:
    print('Данный файл уже существует')