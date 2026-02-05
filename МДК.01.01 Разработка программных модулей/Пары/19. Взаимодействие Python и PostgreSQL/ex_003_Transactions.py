import psycopg2 # Модуль для работы

# Подключение к базе данных
conn = psycopg2.connect(
        dbname="postgres", # Название базы
        user="postgres", # Имя пользователя
        password="123", # Пароль пользователя
        host="localhost", # Сервер, на котором находится база
        port=5432 # Используемый порт
)

"""
cursor - объект для оптравки запросов в БД
"""
cursor = conn.cursor()

try:
     cursor.execute("SELECT * FROM recipes")
     recipes = cursor.fetchall()
     for item in recipes:
          print(*item)
except Exception as e:
        conn.rollback() # Откат, если произошла ошибка
        print("Ошибка: ", e)

# Закрытие соединения(Делать обязательно), нужно делать после каждого запроса
cursor.close()
conn.close()
