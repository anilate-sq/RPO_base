import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout

class AuthService:
    def login(self, username, password):
        return username == 'admin' and password == '123'

# Создаем окно
class AuthWindow(QWidget):
    # Базовая настройка окна
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Пример разделения логики') # Задаем заголовок окну
        self.resize(400, 300) # Выставляем размеры
        self.setup_ui() # Загружаем интерфейс
        self.auth_service = AuthService() # Создаем экземпляр класса
 
    def setup_ui(self):
        layout = QVBoxLayout() # Создаем контейнер
        self.label = QLabel()
        self.login_input = QLineEdit() # Создаем поле ввода логина
        self.password_input = QLineEdit() # Создаем поле ввода пароля
        self.password_input.returnPressed.connect(self.handle_login) # Обрабатываем нажатие
        
        layout.addWidget(self.login_input) # Добавляем поле ввода на контейнер
        layout.addWidget(self.password_input) # Добавляем поле ввода на контейнер
        layout.addWidget(self.label) # Добавляем текстовую метку, на созданный контейнер

        self.setLayout(layout) # Подружаем созданный контейнер

    def handle_login(self):
        username = self.login_input.text()
        password = self.password_input.text()
        if self.auth_service.login(username, password):
            self.label.setText('Все гуд')
        else:
            self.label.setText('Отстой')
        

if __name__ == "__main__":
    app = QApplication(sys.argv) # Создаем приложение и цикл событий 
    window = AuthWindow() # Создаем окно на базе созданного класса
    window.show() # Открываем/показывае окно
    sys.exit(app.exec()) # Корректный выход


