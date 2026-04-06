# Пример зависимости

class db:
    def connect(self):
        return "Строка подключения"
    
    def get_user_data(self, name):
        print(f'Отображением информации о пользователе{name} из Базы данных')

    def get_department_data(self, name):
        print(f'Такой то департамент {name} с таким то количеством сотрудников')


# Сервайсы
class UserService:
    def __init__(self):
        self.db = db()

class Departments:
    def __init__(self):
        self.db = db()

    def get_user_info():
        db.get_user_data("Виталий")

    def get_department_info():
        db.get_department_data("Маркетинг")