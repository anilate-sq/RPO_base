# Главный экран

from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QScrollArea, QGridLayout, QFrame, QLabel, QPushButton
from PySide6.QtCore import Qt
from app.core.database import SessionLocal
from app.services import user_service, problem_service
from app.ui.dialogs.resolve_problem_dialog import ResolveProblemDialog

class HomeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.refresh()
    
    def init_ui(self):
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(20)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea {border: none; background: transparent;}")

        content = QWidget()
        self.content_layout = QVBoxLayout(content)
        self.content_layout.setSpacing(20)

        self.status_grid = QGridLayout()
        self.status_grid.setSpacing(15)
        self.content_layout.addLayout(self.status_grid)

        self.problems_title = QLabel("Активные проблемы", objectName="titleLabel")
        self.problems_title.setStyleSheet("font-size: 20px; margin-top: 10px;")
        self.content_layout.addWidget(self.problems_title)

        self.problem_container = QVBoxLayout()
        self.problem_container.setSpacing(12)
        self.content_layout.addLayout(self.problem_container)

        self.content_layout.addStretch()
        scroll.setWidget(content)
        self.main_layout.addWidget(scroll)

    def refresh(self):
        # Очистка данных
        while self.status_grid.count(): self.status_grid.takeAt(0)
        while self.problem_container.count(): self.problems_container.takeAt(0)

        db = SessionLocal()
        try:
            profile = user_service.get_user_profile(db, 1)
            if profile:
                self._add_status("Баланс", f'{profile['balance']:.0f} руб.', "-500 руб.", -500, '#FF6B6B')
                self._add_status("Энергия", f'{profile['energy']} /100', "+5%", 5, '#00B894')
                self._add_status("Стресс", f'{profile['stress_level']}%', "-5%.", -5, '#E74C3C')
                self._add_status("Уровень", f'Уровень: {profile['level']} ({profile['experience']}/{profile['experience_to_next_level']} XP)', "До след.: +150 XP", 150, '#FDCB6E')

            problems = problem_service.get_active_problems(db, 1)
            if not problems:
                empty = QLabel("Нет активных проблем, зачилься")
                empty.setObjectName("subtitleLabel")
                self.problem_container.addWidget(empty)
            else:
                for p in problems:
                    self._add_problem_card(p)
        finally:
            db.close()

    def _add_status(self, title, value, trend, trend_val, color):
        card = QFrame()
        card.setObjectName("statusCard")
        card.setStyleSheet(f"border-left: 4px solid {color}")
        layout = QVBoxLayout(card)

        title_lbl = QLabel(f'{title}', objectName="subtitleLabel")
        value_lbl = QLabel(value, objectName="valueLabel")
        trend_lbl = QLabel(trend, objectName="trendUp" if trend_val > 0 else "trendDown")

        layout.addWidget(title_lbl)
        layout.addWidget(value_lbl)
        layout.addWidget(trend_lbl)

        row, col = divmod(self.status_grid.count(), 3)
        self.status_grid.addWidget(card, row, col)

    def _add_problem_card(self, problem):
        card = QFrame()
        card.setObjectName("problemCard")
        color = "#FF6B6B" if problem["priority"] >=7 else ("#FDCB6E" if problem["priority"] >= 4 else "#00B894")

        layout = QHBoxLayout(card)
        layout.setContentsMargins(12, 10, 12, 10)

        left = QVBoxLayout()
        left.addWidget(QLabel(f'[{problem['priority']}/10] {problem['title']}', objectName="titleLabel"))
        left.addWidget(QLabel(problem['description'], objectName="subtitleLabel"))
        
        user_role = user_service.get_user_role()
        if user_role == 1:
            btn = QPushButton("Решить", objectName="successButton")
            btn.setFixedWidth(100)
            btn.clicked.connect(lambda _, p=problem: self._resolve_problem(p))

            layout.addWidget(btn)
        layout.addLayout(left, 1)

        self.problem_container.addWidget(card)

    def _resolve_problem(self, problem):
        print(f'Открываем выбор действий для {problem['title']}')
        dialog = ResolveProblemDialog(problem, parent=self)
        dialog.problemResolved.connect(self._on_problem_resolved)
        if dialog.exec():
            self.refresh()
    
    def _on_problem_resolved(self, changes: dict):
        parent_window = self.window()
        if hasattr(parent_window, 'update_sidebar_stats'):
            from app.core.database import SessionLocal
            from app.services import user_service
            db = SessionLocal()
            try:
                profile = user_service.get_user_profile(db, 1)
                if profile:
                    parent_window.update_sidebar_stats(
                        profile['balance'],
                        profile['energy'],
                        profile['stress_level']
                    )
            finally:
                db.close()
    
    def _open_add_dialog(self):
        from app.ui.dialogs.add_problem_dialog import AddProblemDialog
        dlg = AddProblemDialog(self)
        if dlg.exec():
            self.refresh()