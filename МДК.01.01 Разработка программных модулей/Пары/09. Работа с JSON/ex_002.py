# Работа с файликами
import json
data = {
       "users": ['Витек', 'Ванек']
}

# Создание JSON-файла с записью в него словаря
with open('users.json', 'w', encoding='UTF-8') as file:
     json.dump(data, file, ensure_ascii=False, indent=4)

# Получение данных с JSON-файла
with open('users.json', 'r', encoding='UTF-8') as file:
     data = json.load(file)
     print(data)