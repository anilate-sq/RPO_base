# Диалоговое окно для добавления новой проблемы

from PySide6.QtWidgets import(QDialog, QVBoxLayout, QHBoxLayout, QLabel,
                              QLineEdit, QTextEdit, QSpinBox, QPushButton, QComboBox)
from PySide6.QtCore import Qt
from app.core.database import SessionLocal
from app.services.problem_service import create_problem
from app.core.models import ActionOption

class AddProblemDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Добавить проблему")
        self.setMinimumWidth(450)
        self._build_ui()

    # Создание интерфейса
    def _build_ui(self):
        layout = QVBoxLayout(self)
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Название проблемы")
        self.desc_input = QTextEdit()
        self.desc_input.setPlaceholderText("Описание проблемы(не обязательно)")
        self.desc_input.setMaximumHeight(80)

        #Приоритетность
        prio_layout = QHBoxLayout()
        prio_layout.addWidget(QLabel("Приоритет (1-10):"))
        self.prio_spin = QSpinBox()
        self.prio_spin.setRange(1,10); self.prio_spin.setValue(5)
        prio_layout.addWidget(self.prio_spin)

        type_layout = QHBoxLayout()
        type_layout.addWidget(QLabel("Тип:"))
        self.type_combo = QComboBox()
        self.type_combo.addItems(["регулярная", "срочная", "длительная"])
        type_layout.addWidget(self.type_combo)

        btn_layout = QHBoxLayout()
        btn_cancel = QPushButton("Отмена")
        btn_cancel.clicked.connect(self.reject)
        self.btn_add = QPushButton("Добавить")
        self.btn_add.setObjectName("successButton")
        self.btn_add.clicked.connect(self._submit)
        btn_layout.addWidget(btn_cancel); btn_layout.addWidget(self.btn_add)

        layout.addWidget(self.title_input)
        layout.addWidget(self.desc_input)
        layout.addLayout(prio_layout)
        layout.addLayout(type_layout)
        layout.addLayout(btn_layout)

    # Отправка формы
    def _submit(self):
        title = self.title_input.text().strip()
        if not title:
            self.title_input.setStyleSheet("QLineEdit {border: 1px solid #E74C3C;}")
            return
        
        try:
            db = SessionLocal()
            p_type = self.type_combo.currentText()
            priority= self.prio_spin.value()
            desc = self.desc_input.toPlainText()

            problem = create_problem(db, user_id=1, title=title, description=desc, priority=priority, p_type=p_type)
            self._add_demo_actions(db, problem.id)
            self.accept()
        except Exception as e:
            print(f"Ошибка выполнения... {e}")
        finally:
            if 'db' in locals(): db.close()

    # Создание тестовых действий
    def _add_demo_actions(self, db, problem_id):
        default= {
            {"title": "Быстрый вариант", "chance": 60, "xp": 15, "bal": -100, "energy": -5, "stress": 5},
            {"title": "Долгий вариант", "chance": 90, "xp": 25, "bal": -50, "energy": -15, "stress": 0}
        }

        for a in default:
            db.add(ActionOption(problem_id=problem_id, title=a["title"]), success_chance=a["chance"],
                   xp_reward=a["xp"], balance_change=a["bal"], energy_change=a["energy"], stress_change=a["stress"])
            db.commit()

from PySide6.QtWidgets import(QDialog, QVBoxLayout, QHBoxLayout, QLabel,
                              QLineEdit, QTextEdit, QSpinBox, QPushButton, QComboBox)
