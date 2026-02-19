# Тут должны описываться основные операции с таблицей "ingridients"

import db.db as db

# Создаем класс
class IngridientsService:
        # Внутри класса описываем базовые функции
        @staticmethod
        def get_all():
                # Функция для получения данных об ингридиентах
                pass
        
        @staticmethod
        def add_recipe():
                # Функция для добавления ингридиента
                pass
'''
Пример
class IngridientsService:
        
        @staticmethod
        def get_all():
                conn = db.get_conn()
                cursor = conn.cursor()
                try:
                        cursor.execute() # Запрос в базу
                except:
                        raise
                cursor.close()
                conn.close()
                return "Запрос выполнен"
'''
