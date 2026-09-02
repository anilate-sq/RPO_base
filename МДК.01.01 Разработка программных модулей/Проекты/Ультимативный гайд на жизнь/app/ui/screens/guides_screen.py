"""
Экран гайдов с категориями и прогрессом
"""
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QScrollArea,
    QListWidget, QListWidgetItem, QFrame, QLabel, QProgressBar, QPushButton
)
from PySide6.QtCore import Qt
from app.core.database import SessionLocal
from app.services import guide_service
from app.core.app_context import app_context
from app.ui.dialogs.guide_view_dialog import GuideViewDialog

# Категории гайдов (хардкод, пока нет таблицы sections в БД)
CATEGORIES = [
    {"id": None, "title": "Все гайды", "icon": ""},
    {"id": 1, "title": "Быт", "icon": ""},
    {"id": 2, "title": "Финансы", "icon": ""},
    {"id": 3, "title": "Учеба", "icon": ""},
    {"id": 4, "title": "Менталка", "icon": ""},
    {"id": 5, "title": "Работа", "icon": ""},
]

class GuidesScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.current_section_id = None  # None = все гайды
        self.init_ui()
        self.refresh()

    def init_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        self.category_list = QListWidget()
        self.category_list.setObjectName("sidebar")
        self.category_list.setFixedWidth(220)
        self.category_list.currentRowChanged.connect(self._on_category_selected)
        layout.addWidget(self.category_list)
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")

        self.guides_container = QWidget()
        self.guides_layout = QVBoxLayout(self.guides_container)
        self.guides_layout.setSpacing(12)
        self.guides_layout.addStretch()
        scroll.setWidget(self.guides_container)

        layout.addWidget(scroll, 1)

    def refresh(self):
        """Обновление списка категорий и гайдов"""
        self._load_categories()
        self._load_guides()

    def _load_categories(self):
        """Загрузка категорий в левую панель"""
        self.category_list.clear()
        for cat in CATEGORIES:
            item = QListWidgetItem(cat["title"])
            item.setData(Qt.UserRole, cat["id"])  # Сохраняем section_id
            self.category_list.addItem(item)
        self.category_list.setCurrentRow(0)  # По умолчанию "Все гайды"

    def _on_category_selected(self, row):
        """Обработка выбора категории"""
        if row == -1:
            return
        item = self.category_list.item(row)
        self.current_section_id = item.data(Qt.UserRole)
        self._load_guides()

    def _load_guides(self):
        """Загрузка гайдов из БД"""
        # Очистка контейнера (кроме stretch в конце)
        while self.guides_layout.count() > 1:
            item = self.guides_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        try:
            db = SessionLocal()
            user_id = app_context.get_user_id()
            
            # Получаем гайды (с фильтрацией по section_id если нужно)
            guides = guide_service.get_guides(db, section_id=self.current_section_id)
            
            if not guides:
                empty_lbl = QLabel(
                    "Гайды пока не добавлены. Админ скоро наполнит контент",
                    alignment=Qt.AlignCenter,
                    objectName="subtitleLabel"
                )
                empty_lbl.setStyleSheet("margin-top: 50px;")
                self.guides_layout.insertWidget(0, empty_lbl)
                return

            # Рендерим карточки
            for guide in guides:
                # Получаем прогресс пользователя
                progress = guide_service.get_progress(db, user_id, guide["id"])
                progress_percent = progress["progress_percent"] if progress else 0
                
                self._add_guide_card(guide, progress_percent)

        except Exception as e:
            print(f"️ GuidesScreen DB error: {e}")
            # Демо-данные на случай ошибки
            self._add_demo_guides()
        finally:
            if 'db' in locals():
                db.close()

    def _add_guide_card(self, guide: dict, progress_percent: int):
        """Создание карточки гайда"""
        card = QFrame()
        card.setObjectName("guideCard")
        
        layout = QHBoxLayout(card)
        layout.setContentsMargins(12, 10, 12, 10)

        # Левая часть: информация
        left_layout = QVBoxLayout()
        left_layout.addWidget(QLabel(guide["title"], objectName="titleLabel"))
        
        if guide.get("short_description"):
            left_layout.addWidget(QLabel(guide["short_description"], objectName="subtitleLabel"))
        
        # Мета-информация
        meta_text = f"{guide.get('read_time', '?')} мин"
        if guide.get("difficulty"):
            diff_icon = "" if guide["difficulty"] == "easy" else "" if guide["difficulty"] == "medium" else "🔴"
            meta_text += f"  |  {diff_icon} {guide['difficulty']}"
        meta_text += f"  |  +{guide.get('xp_reward', 0)} XP"
        
        meta_lbl = QLabel(meta_text, objectName="subtitleLabel")
        left_layout.addWidget(meta_lbl)

        # Правая часть: прогресс и кнопка
        right_layout = QVBoxLayout()
        right_layout.addStretch()
        
        # Прогресс-бар
        bar = QProgressBar()
        bar.setMaximum(100)
        bar.setValue(progress_percent)
        bar.setTextVisible(True)
        bar.setObjectName("xpBar" if progress_percent > 0 else "energyBar")
        right_layout.addWidget(bar)
        
        # Кнопка
        btn_text = "Продолжить" if 0 < progress_percent < 100 else ("Завершено" if progress_percent >= 100 else "Открыть")
        btn = QPushButton(btn_text, objectName="primaryButton")
        btn.setFixedWidth(120)
        btn.clicked.connect(lambda _, g=guide: self._open_guide(g))
        right_layout.addWidget(btn, alignment=Qt.AlignBottom)

        layout.addLayout(left_layout, 1)
        layout.addLayout(right_layout)
        
        self.guides_layout.insertWidget(self.guides_layout.count() - 1, card)

    def _open_guide(self, guide: dict):
        """Открытие диалога просмотра гайда"""
        dialog = GuideViewDialog(guide, parent=self)
        if dialog.exec():
            self.refresh()  # Обновляем прогресс после закрытия

    def _add_demo_guides(self):
        """Демо-данные на случай ошибки БД"""
        demo = [
            {"id": 1, "title": "Как приготовить гречку", "short_description": "Базовые принципы выживания", "read_time": 5, "difficulty": "easy", "xp_reward": 25},
            {"id": 2, "title": "Бюджет на неделю", "short_description": "Как не потратить всё за день", "read_time": 7, "difficulty": "medium", "xp_reward": 40},
            {"id": 3, "title": "Тайм-менеджмент для студентов", "short_description": "Планирование без выгорания", "read_time": 10, "difficulty": "medium", "xp_reward": 50},
        ]
        for g in demo:
            self._add_guide_card(g, 0)