# Является неким мозгом проекта, в котором связывается взаимодействие данных с интерфейсом 

# Например

class BookController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_book(self):
        # Получение данных пользователя
        title = input('Название: ')
        author = input('Автор: ')
        year = int(input('Год: '))

        # Вызов модели
        success, message = self.model.add_book(title, author, year)

        # Отображение результата
        self.view.show_message(message)