"""
Главное окно приложения (Связь UI и Авторизации)
"""
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QListWidget, 
    QListWidgetItem, QStackedWidget, QLabel, QMessageBox
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont
from app.config import APP_NAME  # ← Берем название из конфига
from app.ui.styles import MAIN_STYLES
from app.ui.dialogs.add_problem_dialog import AddProblemDialog
from app.core.app_context import app_context  # ← Нужно для выхода
import traceback # Безопасная загрузка экранов (с диагностикой)

try: 
    from app.ui.screens.home_screen import HomeScreen
except Exception as e:
    print(f"Не удалось загрузить HomeScreen: {e}")
    traceback.print_exc()
    HomeScreen = None

try: 
    from app.ui.screens.problems_screen import ProblemsScreen
except Exception as e:
    print(f"Не удалось загрузить ProblemsScreen: {e}")
    traceback.print_exc()
    ProblemsScreen = None

try: 
    from app.ui.screens.guides_screen import GuidesScreen
except Exception as e:
    print(f"Не удалось загрузить GuidesScreen: {e}")
    traceback.print_exc()
    GuidesScreen = None

try: 
    from app.ui.screens.skills_screen import SkillsScreen
except Exception as e:
    print(f"Не удалось загрузить SkillsScreen: {e}")
    traceback.print_exc()
    SkillsScreen = None

try: 
    from app.ui.screens.profile_screen import ProfileScreen
except Exception as e:
    print(f"Не удалось загрузить ProfileScreen: {e}")
    traceback.print_exc()
    ProfileScreen = None

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(APP_NAME)  # ← Используем имя из конфига
        self.setMinimumSize(1280, 800)
        self.setStyleSheet(MAIN_STYLES)
        self._setup_ui()

    def _setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)

        self.sidebar = self._create_sidebar()
        main_layout.addWidget(self.sidebar)

        self.content_stack = QStackedWidget()
        self.content_stack.setObjectName("contentStack")
        main_layout.addWidget(self.content_stack, 1)

        self._init_screens()
        # По умолчанию открываем "Проблемы" (индекс 2)
        self.sidebar.setCurrentRow(4) 

    def _create_sidebar(self) -> QListWidget:
        sidebar = QListWidget()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(250)
        sidebar.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        sidebar.setSelectionMode(QListWidget.SingleSelection)
        sidebar.setFocusPolicy(Qt.ClickFocus)

        def add_item(text, is_clickable: bool = True, size_hint: QSize = None, font_size: int = 12):
            item = QListWidgetItem(text)
            item.setTextAlignment(Qt.AlignCenter)
            if size_hint: item.setSizeHint(size_hint)
            item.setFont(QFont("Arial", font_size, QFont.Bold if font_size > 13 else QFont.Normal))
            if not is_clickable:
                item.setFlags(item.flags() & ~Qt.ItemIsSelectable & ~Qt.ItemIsEnabled)
            sidebar.addItem(item)
            return item

        # Заголовок
        add_item(" ULTIMATE\nLIFE GUIDE", False, QSize(250, 60), 14)
        add_item("─" * 28, False, QSize(250, 10), 10)

        # Навигация (текст, индекс в QStackedWidget)
        menu_map = [
            ("Главная", 0),
            ("Гайды", 1),
            ("Проблемы", 2),
            ("Навыки", 3),
            ("Статистика", 4),
            ("Достижения", 5),
            ("Профиль", 6),  # ← ДОБАВЛЕНО: Доступ к профилю
        ]

        for text, stack_idx in menu_map:
            add_item(text, True, QSize(250, 45), 12).setData(Qt.UserRole, stack_idx)

        add_item("─" * 28, False, QSize(250, 10), 10)
        add_item(" Добавить проблему").setData(Qt.UserRole, "add")
        add_item("Выход").setData(Qt.UserRole, "logout")  # ← ДОБАВЛЕНО: Кнопка выхода

        # Статистика внизу (для обновления через update_sidebar_stats)
        self.stats_ref = add_item("Загрузка...", False, QSize(250, 40), 11)

        sidebar.currentRowChanged.connect(self._on_sidebar_clicked)
        return sidebar

    def _init_screens(self):
        """Заполнение стека экранами"""
        # Индексы 0-6 соответствуют menu_map
        self.content_stack.addWidget(HomeScreen() if HomeScreen else self._placeholder("Главная"))
        self.content_stack.addWidget(GuidesScreen() if GuidesScreen else self._placeholder("Гайды"))
        self.content_stack.addWidget(ProblemsScreen() if ProblemsScreen else self._placeholder("Проблемы"))
        self.content_stack.addWidget(SkillsScreen() if SkillsScreen else self._placeholder("Навыки"))
        self.content_stack.addWidget(self._placeholder("Статистика"))
        self.content_stack.addWidget(self._placeholder("Достижения"))
        self.content_stack.addWidget(ProfileScreen() if ProfileScreen else self._placeholder("Профиль"))

    def _placeholder(self, title: str) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setAlignment(Qt.AlignCenter)
        lbl = QLabel(title, objectName="titleLabel")
        lbl.setStyleSheet("font-size: 32px;")
        layout.addWidget(lbl)
        layout.addWidget(QLabel("В разработке...", objectName="subtitleLabel"))
        return widget

    def _on_sidebar_clicked(self, row_index: int):
        if row_index == -1 or not hasattr(self, 'sidebar'):
            return

        item = self.sidebar.item(row_index)
        if not item: return
        target = item.data(Qt.UserRole)

        # 1. Переключение экранов (индексы 0-6)
        if isinstance(target, int) and 0 <= target < self.content_stack.count():
            self.content_stack.setCurrentIndex(target)
            
        # 2. Кнопка "Добавить"
        elif target == "add":
            dlg = AddProblemDialog(self)
            if dlg.exec():
                # Обновляем все экраны, у которых есть метод refresh
                for i in range(self.content_stack.count()):
                    w = self.content_stack.widget(i)
                    if hasattr(w, 'refresh'): w.refresh()

        # 3. Кнопка "Выход"
        elif target == "logout":
            reply = QMessageBox.question(
                self, "Выход", "Вы уверены, что хотите выйти?",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                app_context.logout()  # Сбрасываем контекст
                self.close()          # Закрываем окно → main.py завершит работу

    def update_sidebar_stats(self, bal: float, eng: int, stress: int):
        """Обновление цифр в сайдбаре"""
        if hasattr(self, 'stats_ref'):
            # Форматируем красиво
            text = f" {bal:.0f} ₽ |  {eng}% |  {stress}%"
            self.stats_ref.setText(text)