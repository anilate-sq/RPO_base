"""
Диалог входа в систему
"""
from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                               QLineEdit, QPushButton)
from PySide6.QtCore import Qt
from app.core.database import SessionLocal
from app.services import auth_service
from app.core.app_context import app_context
from app.ui.dialogs.register_dialog import RegisterDialog

class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(" Вход в Ultimate Life Guide")
        self.setFixedSize(400, 320)
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(15)

        layout.addWidget(QLabel("Логин или Email", objectName="subtitleLabel"))
        self.login_input = QLineEdit()
        self.login_input.setPlaceholderText("username или email")
        layout.addWidget(self.login_input)

        layout.addWidget(QLabel("Пароль", objectName="subtitleLabel"))
        self.pass_input = QLineEdit()
        self.pass_input.setPlaceholderText("Пароль")
        self.pass_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.pass_input)

        self.error_label = QLabel("", objectName="trendDown")
        self.error_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.error_label)

        btn_layout = QHBoxLayout()
        self.btn_register = QPushButton("Регистрация")
        self.btn_register.setObjectName("infoButton")
        self.btn_register.clicked.connect(self._open_register)
        btn_layout.addWidget(self.btn_register)

        self.btn_login = QPushButton("Войти")
        self.btn_login.setObjectName("primaryButton")
        self.btn_login.clicked.connect(self._attempt_login)
        btn_layout.addWidget(self.btn_login)

        layout.addLayout(btn_layout)

    def _open_register(self):
        dlg = RegisterDialog(self)
        if dlg.exec():
            self.login_input.setText(dlg.registered_username)
            self.pass_input.setFocus()

    def _attempt_login(self):
        self.error_label.setText("")
        username = self.login_input.text().strip()
        password = self.pass_input.text().strip()

        if not username or not password:
            self.error_label.setText("Заполни все поля")
            return

        try:
            db = SessionLocal()
            user = auth_service.login(db, username, password)
            if user:
                app_context.login(user.id, user.username)
                self.accept()  # Закрываем диалог с кодом Accepted
            else:
                self.error_label.setText("Неверный логин или пароль")
        except Exception as e:
            self.error_label.setText(f"Ошибка подключения: {e}")
        finally:
            if 'db' in locals(): db.close()