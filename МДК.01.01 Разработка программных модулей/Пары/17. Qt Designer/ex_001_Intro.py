from recipe_ui import Ui_RecipeWindow
from PyQt6.QtWidgets import QApplication, QWidget
import sys

# Первый способ с преобразованием файлов

class MainWindow(QWidget):
        def __init__(self):
                super().__init__()
                self.ui = Ui_RecipeWindow()
                self.ui.setupUi(self)

if __name__ == "__main__":
        application = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(application.exec())