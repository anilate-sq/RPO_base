with open('Пара 8. Работа с файлами/carassius.jpg', 'rb') as file:
    img_data = file.read()

with open('Пара 8. Работа с файлами/carassius_copy.jpg', 'wb') as file:
    file.write(img_data)