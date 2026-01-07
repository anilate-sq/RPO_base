class User:
      def __init__(self, name, password):
            self.name = name
            self.__password = password

user1 = User('Победа', 'qweqwe123')
print(user1.__password) # Ошибка
print(user1._User__password) # Доступ есть