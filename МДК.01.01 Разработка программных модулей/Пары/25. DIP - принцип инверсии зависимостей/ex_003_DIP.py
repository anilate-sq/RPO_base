# 1. Создание абстракции(интерфейса)
class DatabaseInterface:
    def get_user_data(self, name):
        pass

    def save_user(self, name):
        pass

# 2. Реализация конкретных классов
class PostgreSQLDatabase(DatabaseInterface):
    def get_user_data(self, name):
        query = 'Запрос в БД PostgreSQL'
        print('Отображение информации')

    def save_user():
        query = 'Запрос в БД PostgreSQL'
        print('Информация о успешном добавлении или вывод ошибки')

class MySQLDatabase(DatabaseInterface):
    def get_user_data(self, name):
        query = 'Запрос в БД MySQL'
        print('Отображение информации')

    def save_user():
        query = 'Запрос в БД MySQL'
        print('Информация о успешном добавлении или вывод ошибки')

class MongoDatabase(DatabaseInterface):
    def get_user_data(self, name):
        query = 'Запрос в БД MongoDB'
        print('Отображение информации')

    def save_user():
        query = 'Запрос в БД MongoDB'
        print('Информация о успешном добавлении или вывод ошибки')

# 3. Реализация абстракции в сервисе
class UserService:
    def __init__(self, db: DatabaseInterface):
        self.db = db

    def get_user_info(self, name):
        self.db.get_user_data(name)

    def register_user(self, name):
        self.db.save_user(name)