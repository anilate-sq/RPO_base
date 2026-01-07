def create_duplicate(source, duplicate):
    with open(source, 'rb') as inner_file:
        with open(duplicate, 'wb') as outter_file:
            outter_file.write(inner_file.read())
    
create_duplicate('Пара 8. Работа с файлами/carassius.jpg', 'Пара 8. Работа с файлами/carassius_dublicate.jpg')
