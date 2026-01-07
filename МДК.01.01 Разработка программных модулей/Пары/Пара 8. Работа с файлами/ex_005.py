# write() - вписать в файл текстовое поле
with open('Пара 8. Работа с файлами/file2.txt', 'w', encoding="UTF-8") as file:
    print(file.write('Какой-то текст'))

# writelines() - вписать в файл список строк
with open('Пара 8. Работа с файлами/file2.txt', 'w', encoding="UTF-8") as file:
    print(file.writelines(['Какой-то текст1\n', 'Какой-то текст2']))
