"""
Диалоговое окно для добавления новой проблемы
"""
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QTextEdit, QSpinBox, QPushButton, QComboBox, QMessageBox
)
from PySide6.QtCore import Qt
from app.core.database import SessionLocal
from app.services.problem_service import create_problem
from app.core.models import ActionOption
from app.core.app_context import app_context  # ← ДОБАВИТЬ

class AddProblemDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Добавить проблему")
        self.setMinimumWidth(450)
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Название проблемы *")
        self.title_input.setObjectName("primaryInput")  # Для стилей
        
        self.desc_input = QTextEdit()
        self.desc_input.setPlaceholderText("Описание (не обязательно)")
        self.desc_input.setMaximumHeight(80)
        self.desc_input.setObjectName("primaryInput")

        # Приоритет
        prio_layout = QHBoxLayout()
        prio_layout.addWidget(QLabel("Приоритет (1-10):", objectName="subtitleLabel"))
        self.prio_spin = QSpinBox()
        self.prio_spin.setRange(1, 10)
        self.prio_spin.setValue(5)
        prio_layout.addWidget(self.prio_spin)

        # Тип
        type_layout = QHBoxLayout()
        type_layout.addWidget(QLabel("Тип:", objectName="subtitleLabel"))
        self.type_combo = QComboBox()
        self.type_combo.addItems(["регулярная", "срочная", "длительная"])
        self.type_combo.setObjectName("primaryInput")
        type_layout.addWidget(self.type_combo)

        # Кнопки
        btn_layout = QHBoxLayout()
        btn_cancel = QPushButton("Отмена")
        btn_cancel.setObjectName("dangerButton")
        btn_cancel.clicked.connect(self.reject)
        
        self.btn_add = QPushButton("Добавить")
        self.btn_add.setObjectName("successButton")
        self.btn_add.clicked.connect(self._submit)
        
        btn_layout.addWidget(btn_cancel)
        btn_layout.addWidget(self.btn_add)

        # Сборка
        layout.addWidget(QLabel("Заголовок *", objectName="subtitleLabel"))
        layout.addWidget(self.title_input)
        layout.addWidget(QLabel("Описание", objectName="subtitleLabel"))
        layout.addWidget(self.desc_input)
        layout.addLayout(prio_layout)
        layout.addLayout(type_layout)
        layout.addLayout(btn_layout)

    def _submit(self):
        title = self.title_input.text().strip()
        if not title:
            self.title_input.setStyleSheet("QLineEdit { border: 1px solid #E74C3C; }")
            QMessageBox.warning(self, "Ошибка", "Введите название проблемы")
            return
        
        # Сброс стилей
        self.title_input.setStyleSheet("")

        try:
            db = SessionLocal()
            
            user_id = app_context.get_user_id()
            
            p_type = self.type_combo.currentText()
            priority = self.prio_spin.value()
            desc = self.desc_input.toPlainText().strip()

            problem = create_problem(
                db, 
                user_id=user_id,  # ← Динамический ID
                title=title, 
                description=desc, 
                priority=priority, 
                p_type=p_type
            )
            
            # Добавляем демо-действия (одна транзакция)
            self._add_demo_actions(db, problem.id)
            
            self.accept()
            
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось создать проблему:\n{e}")
            print(f"Debug: {e}")  # Для консоли разработчика
        finally:
            if 'db' in locals():
                db.close()

    def _add_demo_actions(self, db, problem_id):
        """Создаёт 2 стандартных варианта действий для быстрой демонстрации"""
        defaults = [
            {"title": "Быстрый вариант", "chance": 60, "xp": 15, "bal": -100, "energy": -5, "stress": 5},
            {"title": "Долгий вариант", "chance": 90, "xp": 25, "bal": -50, "energy": -15, "stress": 0},
        ]

        for a in defaults:
            db.add(ActionOption(
                problem_id=problem_id,
                title=a["title"],
                success_chance=a["chance"],
                xp_reward=a["xp"],
                balance_change=a["bal"],
                energy_change=a["energy"],
                stress_change=a["stress"]
            ))
        
        db.commit()