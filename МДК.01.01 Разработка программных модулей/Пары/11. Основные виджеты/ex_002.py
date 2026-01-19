import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout

# Создаем окно
class MainWindow(QWidget):
    # Базовая настройка окна
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Модульное GUI') # Задаем заголовок окну
        self.resize(400, 300) # Выставляем размеры
        self.setup_ui() # Загружаем интерфейс

    def setup_ui(self):
        layout = QVBoxLayout() # Создаем контейнер
        self.label = QLabel("Введите ваше имя: ") # Создаем текстовую метку
        layout.addWidget(self.label) # Добавляем текстовую метку, на созданный контейнер

        self.entry = QLineEdit() # Создаем поле ввода
        layout.addWidget(self.entry) # Добавляем поле ввода на контейнер

        self.button = QPushButton("Поприветствовать") # Создаем кнопку
        self.button.clicked.connect(self.say_hello) # Создаем обработчик событий
        layout.addWidget(self.button) # Добавляем кнопку на контейнер

        self.setLayout(layout) # Подружаем созданный контейнер

    # Создаем слот(метод, который обрабатывает действие при нажатии на кнопку)
    def say_hello(self):
        name = self.entry.text() # Заносим в переменную, значение введенное в LineEdit
        print(f'Привет, {name}!') # Выводим результат в консоль
        self.label.setText(f'Привет, {name}') # Выводим результат в текстовую метку

if __name__ == "__main__":
    app = QApplication(sys.argv) # Создаем приложение и цикл событий 
    window = MainWindow() # Создаем окно на базе созданного класса
    window.show() # Открываем/показывае окно
    sys.exit(app.exec()) # Корректный выход


