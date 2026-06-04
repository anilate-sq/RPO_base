# Отправка POST-запросов

import requests

url = "https://jsonplaceholder.typicode.com/posts" # Ресурс для получения данных(API, обрабатывающий запросы по ресурсам)

data = {
        'title':  "Тестовый пост",
        'body': "Отправляю пост для проверки корректности работы post-запроса",
        'userId':  1
}

response = requests.post(url, json=data)
print("Код ответа - ", response.status_code)

post = response.json()

# Структурирование информации
print(f"Новый пост\nНазвание: {post["title"]}, Содержимое: {post["body"]}")