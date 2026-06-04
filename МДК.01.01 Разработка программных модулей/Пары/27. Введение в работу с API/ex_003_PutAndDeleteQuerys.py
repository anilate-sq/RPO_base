# PUT и DELETE запросы

import requests

url = "https://jsonplaceholder.typicode.com/posts/2" # Ресурс для получения данных(API, обрабатывающий запросы по ресурсам)

response = requests.put(url, json={"title": "Обновленный пост"})
print("Код ответа - ", response.status_code)

post = response.json()
print(post)

# Структурирование информации
print(f"Обновленный пост\nНазвание: {post["title"]}")

response = requests.delete(url)
print(response.json())