class User:
   def __init__(self, name):
            self.name = name
   def greeting(self):
         return f'Привет пользователь {self.name}'

class Admin(User):
      def __init__(self, name, permission=["чтение"]):
          super().__init__(name)
          self.permission = permission

      def greeting(self):
            return f'{super().greeting()} - теперь ты администратор'

class Moder(User):
      def __init__(self, name, permission=["чтение", "удаление"]):
            super().__init__(name)
            self.permission = permission
      def greeting(self):
            text = ''.join([f'\n{item}' for item in self.permission])
            return f'{super().greeting()} - теперь ты модератор и имеешь следующие функции: {text}'

class Visit(User):
      def __init__(self, name, permission=["чтение", "редактирование", "удаление"]):
            super().__init__(name)
            self.permission = permission

admin = Admin('Петр')
visitor = Visit('Степан')
moder = Moder('Иван')

print(admin.permission)
print(visitor.permission)
print(moder.permission)

user = User('Александр')
print(user.greeting())
print(admin.greeting())
print(moder.greeting())