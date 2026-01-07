class User:
      def __init__(self, name, password):
            self.name = name
            self.password = password

      def getPassword(self):
            return self.password
      def setPassword(self, value):
            if len(value) > 3:
                  self.password = value
            else:
                  print('Фигня переделывай')

# Выше устаревший вариант, ниже современный вариант

class User:
      def __init__(self, name, password):
            self.name = name
            self.password = password
     
      @property
      def getPassword(self):
            return self.password # Возвращаем результат
      @getPassword.setter
      def setPassword(self, value): # Фиксируем получение данных
            if len(self.password) > 3:
                  self.password = value
            else:
                  print('Мимо')
