"""
Экран управления проблемами
"""
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QTableWidget, QTableWidgetItem, QHeaderView, QLabel, QMessageBox
)
from PySide6.QtCore import Qt
from app.core.database import SessionLocal
from app.services import problem_service
from app.ui.dialogs.resolve_problem_dialog import ResolveProblemDialog
from app.ui.dialogs.edit_problem_dialog import EditProblemDialog
from app.core.app_context import app_context

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
        self.btn_urgent = QPushButton("Срочные (7+)")
        self.btn_resolved = QPushButton("Решённые")

        for b in [self.btn_all, self.btn_urgent, self.btn_resolved]:
            b.setFixedWidth(150)

        self.btn_all.clicked.connect(lambda: self.load_problems("all"))
        self.btn_urgent.clicked.connect(lambda: self.load_problems("urgent"))
        self.btn_resolved.clicked.connect(lambda: self.load_problems("resolved"))

        top_bar = QHBoxLayout()
        top_bar.addWidget(self.btn_all)
        top_bar.addWidget(self.btn_urgent)
        top_bar.addWidget(self.btn_resolved)
        top_bar.addStretch()
        layout.addLayout(top_bar)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Приоритет", "Проблема", "Статус", "Дата", "Действия"])
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
        self.table.verticalHeader().setVisible(False)
        self.table.setAlternatingRowColors(True)
        layout.addWidget(self.table)

    def refresh(self):
        print("ProblemsScreen.refresh() вызван")
        self.load_problems("all")

    def load_problems(self, filter_type: str = "all"):
        print(f"Загрузка проблем: фильтр={filter_type}")
        self.table.setRowCount(0)

        try:
            db = SessionLocal()
            user_id = app_context.get_user_id()
            print(f"Пользователь: user_id={user_id}")
            
            problems = problem_service.get_active_problems(db, user_id=user_id, status_filter=filter_type)
            print(f"Найдено проблем: {len(problems)}")

            if not problems:
                print("Список проблем пуст")
                empty_lbl = QLabel(
                    f"Нет проблем с фильтром '{filter_type}'. Добавь первую!",
                    alignment=Qt.AlignCenter,
                    objectName="subtitleLabel"
                )
                empty_lbl.setStyleSheet("margin-top: 50px;")
                self.table.setRowCount(1)
                self.table.setSpan(0, 0, 1, 5)
                self.table.setCellWidget(0, 0, empty_lbl)
                return

            for i, p in enumerate(problems):
                print(f"  [{i}] Рендерим проблему: {p['title']}")
                self.table.insertRow(i)
                
                prio_icon = "" if p["priority"] >= 7 else ("" if p["priority"] >= 4 else "")
                self.table.setItem(i, 0, QTableWidgetItem(f"{prio_icon} {p['priority']}/10"))
                self.table.setItem(i, 1, QTableWidgetItem(p["title"]))

                status_text = "Решена" if p["status"] == "разрешенная" else "⏳ Активна"
                self.table.setItem(i, 2, QTableWidgetItem(status_text))
                self.table.setItem(i, 3, QTableWidgetItem(p["created_at"][:10] if p.get("created_at") else "-"))

                # Контейнер для кнопок действий
                actions_widget = QWidget()
                actions_layout = QHBoxLayout(actions_widget)
                actions_layout.setContentsMargins(2, 0, 2, 0)
                actions_layout.setSpacing(4)

                if p["status"] == "активная":
                    btn_resolve = QPushButton("Успешно")
                    btn_resolve.setObjectName("successButton")
                    btn_resolve.setToolTip("Решить проблему")
                    btn_resolve.setFixedWidth(32)
                    btn_resolve.clicked.connect(lambda _, prob=p: self._open_resolve_dialog(prob))
                    actions_layout.addWidget(btn_resolve)

                btn_edit = QPushButton("Редактировать")
                btn_edit.setObjectName("infoButton")
                btn_edit.setToolTip("Редактировать")
                btn_edit.setFixedWidth(32)
                btn_edit.clicked.connect(lambda _, prob=p: self._open_edit_dialog(prob))
                actions_layout.addWidget(btn_edit)

                btn_delete = QPushButton("️")
                btn_delete.setObjectName("dangerButton")
                btn_delete.setToolTip("Удалить")
                btn_delete.setFixedWidth(32)
                btn_delete.clicked.connect(lambda _, prob=p: self._confirm_delete(prob))
                actions_layout.addWidget(btn_delete)

                self.table.setCellWidget(i, 4, actions_widget)
                print(f"Проблема {p['title']} отрендерена")

        except Exception as e:
            print(f"ProblemsScreen DB error: {e}")
            import traceback
            traceback.print_exc()
        finally:
            if 'db' in locals():
                db.close()
            print("load_problems() завершён")

    def _open_resolve_dialog(self, problem: dict):
        dialog = ResolveProblemDialog(problem, parent=self)
        if dialog.exec():
            self.refresh()

    def _open_edit_dialog(self, problem: dict):
        dialog = EditProblemDialog(problem, parent=self)
        if dialog.exec():
            self.refresh()

    def _confirm_delete(self, problem: dict):
        reply = QMessageBox.question(
            self, "Удаление проблемы",
            f"Удалить «{problem['title']}»?\nЭто действие нельзя отменить.",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            try:
                db = SessionLocal()
                user_id = app_context.get_user_id()
                problem_service.delete_problem(db, problem["id"], user_id)
                self.refresh()
            except Exception as e:
                print(f"Ошибка удаления: {e}")
            finally:
                if 'db' in locals():
                    db.close()