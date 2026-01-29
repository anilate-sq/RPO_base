from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QApplication, QWidget
import sys

# Второй способ без преобразования файлов

class MainWindow(QWidget):
        def __init__(self):
                super().__init__()
                loadUi('recipe_ui.ui', self)

if __name__ == "__main__":
        application = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(application.exec())