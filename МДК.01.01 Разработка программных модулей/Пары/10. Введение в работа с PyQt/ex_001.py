import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv) # Создаем приложение
window = QMainWindow() # Создаем окно
window.setWindowTitle('Окно моего первого приложение') # Заголовок окна
window.resize(480, 400) # Размеры окна
window.show() # Демонстрация окна
sys.exit(app.exec_()) # Выход