import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout

# Создаем окно
class MainWindow(QWidget):
    # Базовая настройка окна
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Пример ввода') # Задаем заголовок окну
        self.resize(400, 300) # Выставляем размеры
        self.setup_ui() # Загружаем интерфейс

    def setup_ui(self):
        layout = QVBoxLayout() # Создаем контейнер
        self.label = QLabel()
        self.label.setStyleSheet("""font-size: 24pt;
                                 color: green;
                                 font-family: Verdana;
                                 """)


        self.entry = QLineEdit() # Создаем поле ввода
        self.entry.returnPressed.connect(self.say_hello) # Обрабатываем нажатие
        layout.addWidget(self.entry) # Добавляем поле ввода на контейнер
        layout.addWidget(self.label) # Добавляем текстовую метку, на созданный контейнер

        self.setLayout(layout) # Подружаем созданный контейнер

    def say_hello(self):
        name = self.entry.text() # Считываем текст с поля ввода и заносим его в переменную

        # Мини-проверка на то, что пользователь что-то ввел
        if not name:
            self.label.setText("Введите ваше имя")
        
        self.user_name = name # Создаем переменную внутри класса, для хранения имени пользователя
        self.label.setText(f'Добро пожаловать, {name}!') # Выводим приветственное сообщение



if __name__ == "__main__":
    app = QApplication(sys.argv) # Создаем приложение и цикл событий 
    window = MainWindow() # Создаем окно на базе созданного класса
    window.show() # Открываем/показывае окно
    sys.exit(app.exec()) # Корректный выход


