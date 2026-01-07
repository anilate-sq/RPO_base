class Book:
      def __init__(self, name, author):
            self.name = name
            self.author = author
      # срабатывает при вызове print() для пользователя приложения
      def __str__(self):
            return f'Название: {self.name}\nАвтор: {self.author}'
      # срабатывает при вызове print() для разработчика
      def __repr__(self):
            return f'({self.name}) ({self.author})'
book1 = Book('Метро', 'Дмитрий Глуховский')
print(book1) # срабатывает __str__()
print([book1]) # срабатывает __repr__()