"""
Ultimate Life Guide - Точка входа
"""
import sys
from pathlib import Path

# Фикс путей: добавляем корень проекта в sys.path ДО любых импортов
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFont
from app.config import APP_NAME, APP_VERSION
from app.core.database import init_db
from app.ui.main_window import MainWindow
from app.ui.dialogs.login_dialog import LoginDialog

def main():
    """Запуск приложения"""
    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    app.setApplicationVersion(APP_VERSION)

    # Кроссплатформенный шрифт (Helvetica нет на Windows)
    font_name = "Segoe UI" if sys.platform == "win32" else "Arial"
    app.setFont(QFont(font_name, 12))
    
    # Fusion гарантирует одинаковый рендер QSS на Windows/macOS/Linux
    app.setStyle("Fusion")

    # Сначала показываем окно входа
    login_dialog = LoginDialog()
    if login_dialog.exec() == LoginDialog.Accepted:
        # Успешный вход → открываем главное окно
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
    else:
        # Закрыли окно входа без авторизации → выходим
        print("Выход из приложения")
        sys.exit(0)

if __name__ == "__main__":
    # init_db() - Только при первом запуске   
    main()