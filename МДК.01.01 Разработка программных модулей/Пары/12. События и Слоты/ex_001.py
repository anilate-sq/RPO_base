import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout

# Создаем окно
class MainWindow(QWidget):
    # Базовая настройка окна
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Пример изменения текста') # Задаем заголовок окну
        self.resize(400, 300) # Выставляем размеры
        self.setup_ui() # Загружаем интерфейс

    def setup_ui(self):
        layout = QVBoxLayout() # Создаем контейнер
        self.label = QLabel("Тут будет показываться вводимый текст") # Создаем текстовую метку
        layout.addWidget(self.label) # Добавляем текстовую метку, на созданный контейнер

        self.entry = QLineEdit() # Создаем поле ввода
        self.entry.textChanged.connect(self.on_text_changed) # Обрабатываем изменение текста
        layout.addWidget(self.entry) # Добавляем поле ввода на контейнер

        self.setLayout(layout) # Подружаем созданный контейнер

    def on_text_changed(self, text):
        self.label.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv) # Создаем приложение и цикл событий 
    window = MainWindow() # Создаем окно на базе созданного класса
    window.show() # Открываем/показывае окно
    sys.exit(app.exec()) # Корректный выход


