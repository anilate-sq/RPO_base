# Тут должны описываться основные операции с таблицей "recipes"

import db.db as db

# Создаем класс
class RecipeService:
        # Внутри класса описываем базовые функции
        @staticmethod
        def get_all():
                # Функция для получения данных о рецептах
                pass
        
        @staticmethod
        def add_recipe():
                # Функция для добавление рецепта
                pass
'''
Пример
class RecipeService:
        
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
