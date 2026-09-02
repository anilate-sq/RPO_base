"""
Диалог регистрации
"""
import traceback
from PySide6.QtWidgets import (QDialog, QVBoxLayout, QLabel, QLineEdit, 
                               QPushButton, QMessageBox)
from PySide6.QtCore import Qt
from app.core.database import SessionLocal
from app.services import auth_service

class RegisterDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Регистрация")
        self.setFixedSize(400, 400)
        self.registered_username = ""
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(12)

        fields = [
            ("Username", "username_input", "Придумай никнейм", False),
            ("Email", "email_input", "email@example.com", False),
            ("Пароль", "pass_input", "Минимум 4 символа", True),
            ("Повтори пароль", "pass_confirm", "Подтверждение", True)
        ]

        self.inputs = {}
        for label, attr, ph, is_pass in fields:
            layout.addWidget(QLabel(label, objectName="subtitleLabel"))
            inp = QLineEdit()
            inp.setPlaceholderText(ph)
            if is_pass: inp.setEchoMode(QLineEdit.Password)
            setattr(self, attr, inp)
            self.inputs[attr] = inp
            layout.addWidget(inp)

        self.error_label = QLabel("", objectName="trendDown")
        self.error_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.error_label)

        self.btn_create = QPushButton("Создать аккаунт")
        self.btn_create.setObjectName("successButton")
        self.btn_create.clicked.connect(self._attempt_register)
        layout.addWidget(self.btn_create)

    def _attempt_register(self):
        self.error_label.setText("")
        username = self.username_input.text().strip()
        email = self.email_input.text().strip()
        p1 = self.pass_input.text().strip()
        p2 = self.pass_confirm.text().strip()

        if not all([username, email, p1, p2]):
            self.error_label.setText("Заполни все поля")
            return
        if p1 != p2:
            self.error_label.setText("Пароли не совпадают")
            return
        if len(p1) < 4:
            self.error_label.setText("Пароль слишком короткий")
            return

        try:
            db = SessionLocal()
            auth_service.register(db, username, email, p1)
            self.registered_username = username
            QMessageBox.information(self, "Успех", f"Аккаунт {username} создан!\nТеперь войди.")
            self.accept()
        except ValueError as e:
            self.error_label.setText(str(e))
        except Exception as e:
            traceback.print_exc()
            self.error_label.setText(f"Ошибка: {e}")
        finally:
            if 'db' in locals():
                db.close()