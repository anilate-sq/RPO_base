"""
Главный экран (Dashboard)
"""
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QScrollArea,
    QGridLayout, QFrame, QLabel, QPushButton
)
from PySide6.QtCore import Qt
from app.core.database import SessionLocal
from app.services import user_service, problem_service
from app.ui.dialogs.resolve_problem_dialog import ResolveProblemDialog
from app.core.app_context import app_context

class HomeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.refresh()

    def init_ui(self):
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(20)

        # Кнопка быстрого добавления проблемы
        self.btn_add = QPushButton("Добавить проблему", objectName="successButton")
        self.btn_add.setFixedWidth(200)
        self.btn_add.clicked.connect(self._open_add_dialog)
        self.main_layout.addWidget(self.btn_add, alignment=Qt.AlignRight)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")

        content = QWidget()
        self.content_layout = QVBoxLayout(content)
        self.content_layout.setSpacing(20)

        self.status_grid = QGridLayout()
        self.status_grid.setSpacing(15)
        self.content_layout.addLayout(self.status_grid)

        self.problems_title = QLabel(" Активные проблемы", objectName="titleLabel")
        self.problems_title.setStyleSheet("font-size: 20px; margin-top: 10px;")
        self.content_layout.addWidget(self.problems_title)

        self.problem_container = QVBoxLayout()
        self.problem_container.setSpacing(12)
        self.content_layout.addLayout(self.problem_container)

        self.content_layout.addStretch()
        scroll.setWidget(content)
        self.main_layout.addWidget(scroll)

    def refresh(self):
        while self.status_grid.count():
            item = self.status_grid.takeAt(0)
            if item.widget(): item.widget().deleteLater()
        while self.problem_container.count():
            item = self.problem_container.takeAt(0)
            if item.widget(): item.widget().deleteLater()

        try:
            db = SessionLocal()
            user_id = app_context.get_user_id()  
            
            profile = user_service.get_user_profile(db, user_id)
            if profile:
                self._add_status("Баланс", f"{profile['balance']:.0f} ₽", "⬇ 500 ₽", -500, "#FF6B6B")
                self._add_status("Энергия", f"{profile['energy']} / 100", " 5%", 5, "#00B894")
                self._add_status("Стресс", f"{profile['stress_level']} %", "⬇ 5%", -5, "#E74C3C")
                self._add_status("Уровень", f"Lvl {profile['level']} ({profile['experience']}/{profile['experience_to_next_level']} XP)", "До след.: +150 XP", 0, "#FDCB6E")

            problems = problem_service.get_active_problems(db, user_id, status_filter="active")
            if not problems:
                empty = QLabel("Нет активных проблем. Отдыхай или изучай гайды 😉", alignment=Qt.AlignCenter, objectName="subtitleLabel")
                empty.setStyleSheet("margin-top: 20px;")
                self.problem_container.addWidget(empty)
            else:
                for p in problems:
                    self._add_problem_card(p)
        except Exception as e:
            print(f"HomeScreen DB error: {e}")
            # Демо-фоллбэк, чтобы интерфейс не падал при проблемах с БД
            self._add_status("💰 Баланс", "-2 500 ₽", "Демо", 0, "#FF6B6B")
            self._add_status("⚡ Энергия", "75 / 100", "Демо", 0, "#00B894")
        finally:
            if 'db' in locals():
                db.close()

    def _add_status(self, title, value, trend, trend_val, color):
        card = QFrame()
        card.setObjectName("statusCard")
        card.setStyleSheet(f"border-left: 4px solid {color};")
        layout = QVBoxLayout(card)
        layout.addWidget(QLabel(title, objectName="subtitleLabel"))
        layout.addWidget(QLabel(value, objectName="valueLabel"))
        layout.addWidget(QLabel(trend, objectName="trendUp" if trend_val > 0 else "trendDown"))

        row, col = divmod(self.status_grid.count(), 3)
        self.status_grid.addWidget(card, row, col)

    def _add_problem_card(self, problem):
        card = QFrame()
        card.setObjectName("problemCard")
        color = "#FF6B6B" if problem["priority"] >= 7 else ("#FDCB6E" if problem["priority"] >= 4 else "#00B894")
        card.setStyleSheet(f"border-left: 4px solid {color};")

        layout = QHBoxLayout(card)
        layout.setContentsMargins(12, 10, 12, 10)

        left = QVBoxLayout()
        left.addWidget(QLabel(f"[{problem['priority']}/10] {problem['title']}", objectName="titleLabel"))
        left.addWidget(QLabel(problem.get("description", ""), objectName="subtitleLabel"))
        layout.addLayout(left, 1)  

        btn = QPushButton("Решить", objectName="successButton")
        btn.setFixedWidth(100)
        btn.clicked.connect(lambda _, p=problem: self._resolve_problem(p))
        layout.addWidget(btn)  

        self.problem_container.addWidget(card)

    def _resolve_problem(self, problem):
        dialog = ResolveProblemDialog(problem, parent=self)
        dialog.problemResolved.connect(self._on_problem_resolved)
        if dialog.exec():
            self.refresh()

    def _on_problem_resolved(self, changes: dict):
        """Обновление сайдбара после решения проблемы"""
        parent_window = self.window()
        if hasattr(parent_window, 'update_sidebar_stats'):
            try:
                db = SessionLocal()
                user_id = app_context.get_user_id() 
                profile = user_service.get_user_profile(db, user_id)
                if profile:
                    parent_window.update_sidebar_stats(
                        profile["balance"],
                        profile["energy"],
                        profile["stress_level"]
                    )
            except Exception as e:
                print(f"Sidebar update error: {e}")
            finally:
                if 'db' in locals():
                    db.close()

    def _open_add_dialog(self):
        from app.ui.dialogs.add_problem_dialog import AddProblemDialog
        dlg = AddProblemDialog(self)
        if dlg.exec():
            self.refresh()