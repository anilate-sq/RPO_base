import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from app.config import APP_NAME, APP_VERSION
from app.core.database import init_db
from app.ui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    app.setApplicationVersion(APP_VERSION)

    font_name = "Helvetica"
    app.setFont(QFont(font_name, 12))

    app.setStyle("Fusion") # Нужно для стабильной работы QSS

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    init_db()
    main()