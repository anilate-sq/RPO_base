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
%s - параметр(на его место будет передаваться значение)
"""

#==================INSERT====================#
cursor = conn.cursor() # Создаем cursor
cursor.execute("INSERT INTO public.recipes(name, category_id, characters, duration) VALUES('Наполеон', 3, 'Характеристика 5', '02:30:00')") # Отправляем запрос 
conn.commit() # Фиксируем изменения

#==================UPDATE====================#
cursor.execute("UPDATE public.recipes SET characters = %s, duration = %s where id = %s", ('Характеристика 6','03:00:00', 6))
conn.commit()

#==================DELETE====================#
cursor.execute("DELETE FROM recipes WHERE id = %s", (6,))
conn.commit()