import sys
import os
sys.path.append(os.path.abspath('C:/Users/Андрей/Desktop/РПО-git/RPO_base/МДК.01.01 Разработка программных модулей/Пары/21. Data Access Layer'))

import ex_002_DAO.db as db

class RecipeService:
    # Получение всех рецептов
    @staticmethod
    def get_all():
        with db.get_conn() as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT * FROM recipes.recipes')
                return cursor.fetchall()

    # Добавление нового рецепта
    @staticmethod
    def add(name, category, level, description):
        with db.get_conn() as conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute('SELECT category_id FROM categories WHERE name = %s', (category,))
                    category_id = cursor.fetchone()[0]

                    cursor.execute('INSERT INTO recipes.recipes VALUES(DEFAULT, %s, %s, %s, %s)', (name, category_id, level, description))
                    conn.commit()
                except:
                    conn.rollback()
                    raise

    # Редактирование рецепта по id
    @staticmethod
    def edit(id, name, category, level, description):
        with db.get_conn() as conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute('SELECT category_id FROM categories WHERE name = %s', (category,))
                    category_id = cursor.fetchone()[0]

                    cursor.execute('UPDATE recipes.recipes SET name = %s, category_id = %s, level = %s, description = %s WHERE id = %s', (name, category_id, level, description, id))
                    conn.commit()
                except:
                    conn.rollback()
                    raise

    # Удаление рецепта по id
    @staticmethod
    def drop(id):
        with db.get_conn() as conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute('DELETE FROM recipes.recipes WHERE id = %s', (id,))
                    conn.commit()
                except:
                    conn.rollback()
                    raise

    # Получение рецепта по категории
    @staticmethod
    def get_by_category(category):
        pass
