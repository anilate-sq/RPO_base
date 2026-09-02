"""
Диалоговое окно для редактирования проблемы
"""
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QTextEdit, QSpinBox, QPushButton, QComboBox, QMessageBox
)
from PySide6.QtCore import Qt
from app.core.database import SessionLocal
from app.services.problem_service import update_problem
from app.core.app_context import app_context

class EditProblemDialog(QDialog):
    def __init__(self, problem: dict, parent=None):
        super().__init__(parent)
        self.problem = problem
        self.setWindowTitle(f"️ Редактировать: {problem['title']}")
        self.setMinimumWidth(450)
        self._build_ui()
        self._populate_fields()  # Заполняем поля данными из проблемы

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(12)

        # Заголовок
        layout.addWidget(QLabel("Название *", objectName="subtitleLabel"))
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Название проблемы")
        self.title_input.setObjectName("primaryInput")
        layout.addWidget(self.title_input)

        # Описание
        layout.addWidget(QLabel("Описание", objectName="subtitleLabel"))
        self.desc_input = QTextEdit()
        self.desc_input.setPlaceholderText("Детали проблемы (не обязательно)")
        self.desc_input.setMaximumHeight(80)
        self.desc_input.setObjectName("primaryInput")
        layout.addWidget(self.desc_input)

        # Приоритет
        prio_layout = QHBoxLayout()
        prio_layout.addWidget(QLabel("Приоритет (1-10):", objectName="subtitleLabel"))
        self.prio_spin = QSpinBox()
        self.prio_spin.setRange(1, 10)
        prio_layout.addWidget(self.prio_spin)
        prio_layout.addStretch()
        layout.addLayout(prio_layout)

        # Тип
        type_layout = QHBoxLayout()
        type_layout.addWidget(QLabel("Тип:", objectName="subtitleLabel"))
        self.type_combo = QComboBox()
        self.type_combo.addItems(["регулярная", "срочная", "длительная"])
        self.type_combo.setObjectName("primaryInput")
        type_layout.addWidget(self.type_combo)
        type_layout.addStretch()
        layout.addLayout(type_layout)

        layout.addSpacing(10)

        # Кнопки
        btn_layout = QHBoxLayout()
        btn_cancel = QPushButton("Отмена")
        btn_cancel.setObjectName("dangerButton")
        btn_cancel.clicked.connect(self.reject)

        self.btn_save = QPushButton("Сохранить изменения")
        self.btn_save.setObjectName("successButton")
        self.btn_save.clicked.connect(self._submit)

        btn_layout.addWidget(btn_cancel)
        btn_layout.addWidget(self.btn_save)
        layout.addLayout(btn_layout)

    def _populate_fields(self):
        """Предзаполняем поля текущими значениями проблемы"""
        self.title_input.setText(self.problem.get("title", ""))
        self.desc_input.setPlainText(self.problem.get("description", ""))
        self.prio_spin.setValue(self.problem.get("priority", 5))

        p_type = self.problem.get("type", "регулярная")
        if p_type in ["регулярная", "срочная", "длительная"]:
            self.type_combo.setCurrentText(p_type)

    def _submit(self):
        title = self.title_input.text().strip()
        if not title:
            self.title_input.setStyleSheet("QLineEdit { border: 1px solid #E74C3C; }")
            QMessageBox.warning(self, "Ошибка", "Введите название проблемы")
            return

        # Сброс стиля ошибки
        self.title_input.setStyleSheet("")

        try:
            db = SessionLocal()
            user_id = app_context.get_user_id()

            update_problem(
                db,
                problem_id=self.problem["id"],
                user_id=user_id,
                title=title,
                description=self.desc_input.toPlainText().strip(),
                priority=self.prio_spin.value(),
                p_type=self.type_combo.currentText()
            )
            
            QMessageBox.information(self, "Успех", "Проблема успешно обновлена")
            self.accept()  # Закрываем диалог с кодом Accepted
            
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить:\n{e}")
            print(f"Debug EditProblem: {e}")
        finally:
            if 'db' in locals():
                db.close()