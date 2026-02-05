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

#==================SELECT====================#
cursor = conn.cursor() # Создаем cursor
cursor.execute("SELECT * FROM public.recipes;") # Отправляем запрос 
recipes = cursor.fetchall() # Считывае полученные данные
# Выводим данные на экран
for item in recipes:
        print("Рецепт: ", *item)

