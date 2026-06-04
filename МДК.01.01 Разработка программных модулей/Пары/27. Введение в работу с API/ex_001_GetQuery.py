# Отправка get-запроса

import requests

url = "https://jsonplaceholder.typicode.com/users" # Ресурс для получения данных(API, обрабатывающий запросы по ресурсам)

response = requests.get(url)
print("Код ответа - ", response.status_code)

data = response.json() # Парсинг данных

# Структурирование информации
for user in data:
        print(f"Пользователь {user["name"]}, Почта{user["email"]}")