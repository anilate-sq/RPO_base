class User:
   def __init__(self, name):
            self.name = name   

class Admin(User):
      def __init__(self, name):
            self.name = name
            self.permission = ['удаление', 'редактирование', 'просмотр']

class Moder(User):
      def __init__(self, name):
            self.name = name
            self.permission = ['удаление', 'просмотр']

class Visit(User):
      def __init__(self, name):
          self.name = name
          self.permission = ['просмотр']