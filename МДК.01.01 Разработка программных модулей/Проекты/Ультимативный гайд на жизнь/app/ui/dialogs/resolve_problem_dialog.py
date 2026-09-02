"""
Диалог выбора действия для решения проблемы
"""
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QFrame, QScrollArea, QWidget, QMessageBox
)
from PySide6.QtCore import Qt, Signal
from app.core.database import SessionLocal
from app.services import problem_service, user_service
from app.core.app_context import app_context  # ← ДОБАВИТЬ

class ResolveProblemDialog(QDialog):
    problemResolved = Signal(dict)

    def __init__(self, problem: dict, parent=None):
        super().__init__(parent)
        self.problem = problem
        self.setWindowTitle(f"Решить: {problem['title']}")
        self.setMinimumWidth(600)
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Выберите действие:", objectName="titleLabel"))
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")
        
        content = QWidget()
        self.actions_layout = QVBoxLayout(content)
        scroll.setWidget(content)
        layout.addWidget(scroll)

        # Действия уже переданы в self.problem['actions'] из сервиса
        actions = self.problem.get("actions", [])
        if not actions:
            self.actions_layout.addWidget(
                QLabel("Нет доступных действий", alignment=Qt.AlignCenter, objectName="subtitleLabel")
            )
        else:
            for act in actions:
                self._add_action_card(act)

        # Кнопка отмены
        btn_cancel = QPushButton("Отмена")
        btn_cancel.setObjectName("dangerButton")
        btn_cancel.clicked.connect(self.reject)
        layout.addWidget(btn_cancel)

    def _add_action_card(self, act):
        card = QFrame()
        card.setObjectName("problemCard")  
        card.setStyleSheet(f"border-left-color: {'#00B894' if act['success_chance'] >= 80 else '#FDCB6E' if act['success_chance'] >= 50 else '#E74C3C'};")
        
        lay = QHBoxLayout(card)
        lay.setContentsMargins(10, 8, 10, 8)
        
        info = QVBoxLayout()
        info.addWidget(QLabel(act["title"], objectName="titleLabel"))
        
        meta = QLabel(
            f"{act['success_chance']}% |  30-60 мин |  {act['balance_change']} ₽ |  {act['energy_change']} |  {act['stress_change']}",
            objectName="subtitleLabel"
        )
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
            
            user_id = app_context.get_user_id()
            
            res = problem_service.resolve_problem(
                db, 
                user_id=user_id, 
                problem_id=self.problem['id'], 
                action_id=action['id']
            )
            
            user_service.update_user_state(
                db, 
                user_id=user_id,  # ← Динамический ID
                balance=res['stat_changes']['balance'],
                energy=res['stat_changes']['energy'],
                stress_level=res['stat_changes']['stress'],
                experience=res['xp_gained']
            )
            
            # Эмитим сигнал с изменениями для обновления сайдбара
            self.problemResolved.emit({
                "balance": res["stat_changes"]["balance"],
                "energy": res['stat_changes']['energy'],
                "stress": res['stat_changes']['stress'],
                "experience": res['xp_gained']
            })
            
            self.accept()
            
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось решить проблему:\n{e}")
            print(f"Debug: {e}")
        finally:
            if 'db' in locals():
                db.close()