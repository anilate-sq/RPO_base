# Способы чтения 1

# read() - вывод всего
with open('Пара 8. Работа с файлами/file2.txt', 'r', encoding="UTF-8") as file:
    print(file.readline())
    print('\n')
    print(file.read())

# readline() - вывод одной строчки
with open('Пара 8. Работа с файлами/file2.txt', 'r', encoding="UTF-8") as file:
    print(file.readline())

# readlines()- вывод всех строк файла списком
with open('Пара 8. Работа с файлами/file2.txt', 'r', encoding="UTF-8") as file:
    print(file.readlines())