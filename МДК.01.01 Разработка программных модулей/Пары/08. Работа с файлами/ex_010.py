with open('Пара 8. Работа с файлами/logs.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        if 'ERROR' in line:
            print(line)