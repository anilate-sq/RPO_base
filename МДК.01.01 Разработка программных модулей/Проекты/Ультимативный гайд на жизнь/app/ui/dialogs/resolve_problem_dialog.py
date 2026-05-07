from PySide6.QtWidgets import(
    QDialog, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QFrame, QScrollArea, QWidget
)

from PySide6.QtCore import Qt, Signal
from app.core.database import SessionLocal
from app.services import problem_service, user_service

class ResolveProblemDialog(QDialog):
    problemResolved = Signal(dict)

    def __init__(self, problem: dict, parent=None):
        super().__init__(parent)
        self.problem = problem
        self.setWindowTitle(f'Решить: {problem['title']}')
        self.setMinimumWidth(600)
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Выберите действие:", objectName="titleName"))
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea {border: none; background: transparent; }")
        content = QWidget()
        self.actions_layout = QVBoxLayout(content)
        scroll.setWidget(content)
        layout.addWidget(scroll)


        try: 
            db = SessionLocal()
            actions = self.problem.get("actions", [])
            if not actions:
                self.actions_layout.addWidget(QLabel("Нет доступных действий", alignment=Qt.AlignCenter))
            else:
                for act in actions:
                    self._add_action_card(act)
        except Exception as e:
            print(f"Ошибка: {e}")
        finally:
            if 'db' in locals():
                db.close()

        btn_cancel = QPushButton("Отмена")
        btn_cancel.clicked.connect(self.reject)
        layout.addWidget(btn_cancel)

    def _add_action_card(self, act):
        card = QFrame()
        card.setStyleSheet("QFrame{background: #16213E; border-radius: 8px; border-left: 4px solid #4ECDC4; padding: 10px;}")
        lay = QHBoxLayout(card)
        lay.setContentsMargins(10, 8, 10, 8)
        print("Я тут...")
        info = QVBoxLayout()
        info.addWidget(QLabel(act["title"], objectName="titleLabel"))
        meta = QLabel(f'{act['success_chance']}% | 30-60 мин. | {act['balance_change']} руб. | {act['energy_change']} | {act['stress_change']}')
        meta.setObjectName('subtitleLabel')
        info.addWidget(meta)

        btn = QPushButton("Выбрать", objectName="primaryButton")
        btn.setFixedWidth(100)
        btn.clicked.connect(lambda: self._resolve(act))

        lay.addLayout(info, 1)
        lay.addWidget(btn)
        self.actions_layout.addWidget(card)

    def _resolve(self, action):
        try:
            db = SessionLocal()
            res = problem_service.resolve_problem(db, 1, self.problem['id'], action['id'])
            user_service.update_user_state(db, 1,
                                            balance=res['stat_changes']['balance'],
                                            energy=res['stat_changes']['energy'],
                                            stress_level=res['stat_changes']['stress'],
                                            experience=res['xp_gained']
                                            )
            self.problemResolved.emit({
                "balance": res["stat_changes"]["balance"],
                "energy": res['stat_changes']['energy'],
                "stress": res['stat_changes']['stress'],
                "experience": res['xp_gained']
            })
            self.accept()
        except Exception as e:
            print(f"Ошибка: {e}")
        finally:
            if 'db' in locals(): db.close()
