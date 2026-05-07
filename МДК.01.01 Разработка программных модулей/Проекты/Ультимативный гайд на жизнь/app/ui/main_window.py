# Главное окно

from PySide6.QtWidgets import(
    QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QListWidget, QListWidgetItem,
    QStackedWidget, QLabel
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont
from app.ui.styles import MAIN_STYLES
from app.ui.dialogs.add_problem_dialog import AddProblemDialog

# Безопасная загрузка
try: from app.ui.screens.home_screen import HomeScreen
except ImportError: HomeScreen = None
try: from app.ui.screens.problems_screen import ProblemsScreen
except: ProblemsScreen = None
try: from app.ui.screens.profile_screen import ProfileScreen
except: ProfileScreen = None

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Пушка")
        self.setMinimumSize(1280, 800)

        self.setStyleSheet(MAIN_STYLES)
        self._setup_ui()

    def _setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Главный layout
        main_layout = QHBoxLayout(central_widget)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Сайдбар
        self.sidebar = self._create_sidebar()
        main_layout.addWidget(self.sidebar)

        # Стек контента
        self.content_stack = QStackedWidget()
        self.content_stack.setObjectName("contentStack")
        main_layout.addWidget(self.content_stack, 1)

        self._init_screens()

    def _create_sidebar(self) -> QListWidget:
        # Создание сайдбара
        sidebar = QListWidget()
        sidebar.setObjectName('sidebar')
        sidebar.setFixedWidth(250)
        sidebar.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        sidebar.setSelectionMode(QListWidget.SingleSelection)
        sidebar.setFocusPolicy(Qt.ClickFocus)

        def add_item(text, is_clickable: bool = True, size_hint: QSize = None, font_size: int = 12):
            item = QListWidgetItem(text)
            item.setTextAlignment(Qt.AlignCenter)
            if size_hint:
                item.setSizeHint(size_hint)
            item.setFont(QFont("Helvetica", font_size, QFont.Bold if font_size > 13 else QFont.Normal))
            if not is_clickable:
                item.setFlags(item.flags() & ~Qt.ItemIsSelectable & ~Qt.ItemIsEnabled)
            sidebar.addItem(item)
            return item
        
        add_item('ЗАПАХ\nУСПЕХА', False, QSize(250, 60), 14)

        menu_map = [
            ("Главная", 0),
            ("Гайды", 1),
            ("Проблемы", 2),
            ("Навыки", 3),
            ("Статистика", 4),
            ("Достижения", 5)
        ]
        for text, stack_idx in menu_map:
            item = add_item(text, True, QSize(250, 45), 12)
            item.setData(Qt.UserRole, stack_idx)

        add_item("Добавить проблему").setData(Qt.UserRole, "add")

        sidebar.currentRowChanged.connect(self._on_click)
        sidebar.setCurrentRow(2)

        return sidebar

    def _init_screens(self):
        self.content_stack.addWidget(HomeScreen() if HomeScreen else self._placeholder('Главная'))
        self.content_stack.addWidget(self._placeholder("Гайды"))
        self.content_stack.addWidget(ProblemsScreen() if ProblemsScreen else self._placeholder("Проблемы"))
        self.content_stack.addWidget(self._placeholder("Навыки"))
        self.content_stack.addWidget(self._placeholder("Статистика"))
        self.content_stack.addWidget(self._placeholder("Достижения"))
        self.content_stack.addWidget(ProfileScreen() if ProfileScreen else self._placeholder("Достижения"))

    def _placeholder(self, title: str) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setAlignment(Qt.AlignCenter)

        lbl = QLabel(title)
        lbl.setObjectName("titleLabel")
        lbl.setStyleSheet("font-size: 32px;")
        layout.addWidget(lbl)

        sub = QLabel("В разработке ...")
        sub.setObjectName("subtitleLabel")
        layout.addWidget(sub)

        return widget
    
    def _on_click(self, row):
        if row == -1 or not hasattr(self, 'sidebar'): return
        item = self.sidebar.item(row)
        if not item: return
        target = item.data(Qt.UserRole)

        if isinstance(target, int) and 0 <= target < self.content_stack.count():
            self.content_stack.setCurrentIndex(target)

        elif target == "add":
            dlg = AddProblemDialog(self)
            if dlg.exec():
                for i in range(self.content_stack.count()):
                    w = self.content_stack.widget(i)
                    if hasattr(w, 'refresh'): w.refresh()
        
    def update_sidebar_stats(self, bal, eng, stress):
        if hasattr(self, 'stats_ref'):
            self.stats_ref.setText(f'{bal:.0f} руб.\n{eng}% {stress}%')