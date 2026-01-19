import sys
from PyQt6.QtWidgets import(
    QApplication,
    QWidget,
    QPushButton,
    QLineEdit,
    QLabel,
    QVBoxLayout
)

from PyQt6.QtCore import Qt

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Авторизация')
        self.resize(400, 300)
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.title = QLabel('Вход')
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.title)

        self.login_input = QLineEdit()
        self.login_input.setPlaceholderText('Логин')
        layout.addWidget(self.login_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText('Пароль')
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        self.button = QPushButton('Войти')
        self.button.clicked.connect(self.check_login)
        layout.addWidget(self.button)

        self.message = QLabel('')
        self.message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.message)

        self.password_input.returnPressed.connect(self.check_login)
        self.setLayout(layout)
        
    def check_login(self):
        login = self.login_input.text()
        password = self.password_input.text()

        if not login or not password:
            self.message.setText('Введите логин и пароль')
            return

        if login == 'admin' and password == '123':   
            self.message.setText('Добро пожаловать Admin')
        else:
            self.message.setText('Неверный логин или пароль')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())