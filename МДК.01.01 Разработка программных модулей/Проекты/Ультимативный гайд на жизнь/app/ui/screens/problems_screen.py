# Экран для работы с проблемами

from PySide6.QtWidgets import(
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QTableWidget, QTableWidgetItem, QHeaderView, QLabel
)

from PySide6.QtCore import Qt
from app.core.database import SessionLocal
from app.services import problem_service
from app.ui.dialogs.resolve_problem_dialog import ResolveProblemDialog

class ProblemsScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.refresh()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        self.btn_all = QPushButton("Все")
        self.btn_urgent = QPushButton("Срочные(+7)")
        self.btn_resolved = QPushButton("Решенные")

        for b in [self.btn_all, self.btn_urgent, self.btn_resolved]:
            b.setFixedWidth(150)

        self.btn_all.clicked.connect(lambda: self.load_problems("all"))
        self.btn_all.clicked.connect(lambda: self.load_problems("urgent"))
        self.btn_all.clicked.connect(lambda: self.load_problems("resolved"))

        top_bar = QHBoxLayout()
        top_bar.addWidget(self.btn_all)
        top_bar.addWidget(self.btn_urgent)
        top_bar.addWidget(self.btn_resolved)
        top_bar.addStretch()
        layout.addLayout(top_bar)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Приоритет", "Проблема", "Статус", "Дата", "Действие"])
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
        self.table.verticalHeader().setVisible(False)
        layout.addWidget(self.table)

    def refresh(self):
        self.load_problems("all")

    def load_problems(self, filter_types: str = "all"):
        self.table.setRowCount(0)

        try:
            db = SessionLocal()
            problems = problem_service.get_active_problems(db, user_id=1)

            for i, p in enumerate(problems):
                self.table.insertRow(i)
                self.table.setItem(i, 0, QTableWidgetItem(f'{p['priority']}/10'))
                self.table.setItem(i, 1, QTableWidgetItem(p['title']))

                status_text = 'Решена' if p['status'] == 'разрешенная' else 'активная'
                self.table.setItem(i, 2, QTableWidgetItem(status_text))
                self.table.setItem(i, 3, QTableWidgetItem(p['created_at'][:10] if p.get('created_at') else '-'))
                print(p['status'])
                if p['status'] == 'активная':
                    btn = QPushButton("Решить", objectName="successButton")
                    btn.setFixedWidth(90)
                    btn.clicked.connect(lambda _, prob=p: self._open_resolve_dialog(prob))
                    self.table.setCellWidget(i, 4, btn)
                else:
                    self.table.setCellWidget(i, 4, QLabel("Просмотр", aligment=Qt.AlignCenter))

        except Exception as e:
            print("Ошибка: ", e)
        finally:
            if 'db' in locals(): db.close()
    
    def _open_resolve_dialog(self, problem: dict):
        dialog = ResolveProblemDialog(problem, parent=self)
        if dialog.exec():
            self.refresh()