import psycopg2
import db

class RecipeService:
    # Получение всех рецептов
    def get_all(self):
        conn = db.get_conn()
        psycopg2.cursor.conn.cursor()
        psycopg2.cursor.execute('SELECT * FROM recipes.recipes')
        rows = psycopg2.cursor.fetchall()
        psycopg2.cursor.close()
        conn.close()
        return rows
    
    # Добавление нового рецепта
    def add(self, name, category, level, description):
        conn = db.get_conn()
        psycopg2.cursor.conn.cursor()
        try:
            category_id = psycopg2.cursor.execute('SELECT category_id FROM categories WHERE id = %s', (category)) # Получаем id категории, по её названию

            psycopg2.cursor.execute('INSERT INTO recipes.recipes VALUES(NULL, %s, %s, %s, %s)', (name, category_id, level, description)) # Добавляем новый рецепт
            psycopg2.cursor.commit()
        except:
            psycopg2.cursor.rollback()
            raise
    
    # Редактирование рецепта по id
    def edit(self, id, name, category, level, description):
        conn = db.get_conn()
        psycopg2.cursor.conn.cursor()
        try:
            category_id = psycopg2.cursor.execute('SELECT category_id FROM categories WHERE id = %s', (category)) # Получаем id категории, по её названию

            psycopg2.cursor.execute('UPDATE recipes.recipes SET name = %s, category_id = %s, level = %s, description = %s WHERE id = %s', (name, category_id, level, description, id)) # Редактируем рецепт по id
            psycopg2.cursor.commit()
        except:
            psycopg2.cursor.rollback()
            raise
    
    # Удаление рецепта по id
    def drop(self, id):
        conn = db.get_conn()
        psycopg2.cursor.conn.cursor()
        try:
            psycopg2.cursor.execute('DROP FROM recipes.recipes WHERE id = %s', (id)) # Удаляем рецепт по id
            psycopg2.cursor.commit()
        except:
            psycopg2.cursor.rollback()
            raise
    
    # Получение рецепта по категории
    def get_by_category(self, category):
        pass