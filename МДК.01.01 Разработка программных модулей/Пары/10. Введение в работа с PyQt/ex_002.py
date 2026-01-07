import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QBoxLayout, QVBoxLayout, QPushButton

app = QApplication(sys.argv) # Создаем приложение
window = QWidget() # Создаем окно
window.setWindowTitle('Окно моего первого приложение') # Заголовок окна
window.resize(480, 400) # Размеры окна

# Обработка нажатия на кнопку
def click():
    print('Кнопка тыкнута')

layout = QVBoxLayout() # Создаем вертикальный контейнер
button = QPushButton("Тыкни") # Создаем кнопку
button.clicked.connect(click) # Связываем кнопку с функцией
layout.addWidget(button) # Добавляем кнопку на созданный layout
window.setLayout(layout) # Добавляем layout на окно
window.show() # Демонстрация окна
sys.exit(app.exec()) # Выход из приложения
