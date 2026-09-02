"""
Экран навыков пользователя
"""
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QScrollArea,
    QFrame, QLabel, QProgressBar
)
from PySide6.QtCore import Qt
from app.core.database import SessionLocal
from app.services.user_service import get_user_skills
from app.core.app_context import app_context

class SkillsScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.refresh()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # Заголовок
        title = QLabel("Твои навыки", objectName="titleLabel")
        title.setStyleSheet("font-size: 24px; margin-bottom: 10px;")
        layout.addWidget(title)

        # Скроллируемый контейнер для навыков
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")

        self.skills_container = QWidget()
        self.skills_layout = QVBoxLayout(self.skills_container)
        self.skills_layout.setSpacing(12)
        self.skills_layout.addStretch()
        scroll.setWidget(self.skills_container)

        layout.addWidget(scroll, 1)

    def refresh(self):
        """Обновление списка навыков"""
        # Очистка контейнера (кроме stretch в конце)
        while self.skills_layout.count() > 1:
            item = self.skills_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        try:
            db = SessionLocal()
            user_id = app_context.get_user_id()
            
            skills = get_user_skills(db, user_id)
            
            if not skills:
                empty_lbl = QLabel(
                    "Навыков пока нет. Изучай гайды и решай проблемы, чтобы прокачать навыки!",
                    alignment=Qt.AlignCenter,
                    objectName="subtitleLabel"
                )
                empty_lbl.setStyleSheet("margin-top: 50px;")
                self.skills_layout.insertWidget(0, empty_lbl)
                return

            # Рендерим карточки навыков
            for skill in skills:
                self._add_skill_card(skill)

        except Exception as e:
            print(f"SkillsScreen DB error: {e}")
            # Демо-данные на случай ошибки
            self._add_demo_skills()
        finally:
            if 'db' in locals():
                db.close()

    def _add_skill_card(self, skill: dict):
        """Создание карточки навыка"""
        card = QFrame()
        card.setObjectName("statusCard")
        
        layout = QVBoxLayout(card)
        layout.setContentsMargins(15, 12, 15, 12)

        # Верхняя часть: название и уровень
        header_layout = QHBoxLayout()
        
        icon = skill.get('icon', '')
        name = skill.get('name', 'Навык')
        level = skill.get('level', 1)
        category = skill.get('category', '')
        
        title_lbl = QLabel(f"{icon} {name}", objectName="titleLabel")
        title_lbl.setStyleSheet("font-size: 16px;")
        header_layout.addWidget(title_lbl)
        
        header_layout.addStretch()
        
        level_lbl = QLabel(f"Lvl {level}", objectName="valueLabel")
        level_lbl.setStyleSheet("font-size: 18px; color: #4CA885;")
        header_layout.addWidget(level_lbl)
        
        layout.addLayout(header_layout)

        # Категория
        if category:
            cat_lbl = QLabel(f"Категория: {category}", objectName="subtitleLabel")
            cat_lbl.setStyleSheet("font-size: 12px; margin-bottom: 8px;")
            layout.addWidget(cat_lbl)

        # Прогресс-бар
        progress_percent = skill.get('progress_percent', 0)
        exp = skill.get('experience', 0)
        exp_next = skill.get('experience_to_next_level', 100)
        
        bar = QProgressBar()
        bar.setMaximum(100)
        bar.setValue(int(progress_percent))
        bar.setTextVisible(True)
        bar.setFormat(f"{exp} / {exp_next} XP")
        bar.setObjectName("xpBar")
        layout.addWidget(bar)

        self.skills_layout.insertWidget(self.skills_layout.count() - 1, card)

    def _add_demo_skills(self):
        """Демо-данные на случай ошибки БД"""
        demo = [
            {"name": "Программирование", "icon": "", "level": 3, "category": "профессиональные", "experience": 45, "experience_to_next_level": 100, "progress_percent": 45},
            {"name": "Готовка", "icon": "", "level": 2, "category": "жизненные", "experience": 60, "experience_to_next_level": 100, "progress_percent": 60},
            {"name": "Тайм-менеджмент", "icon": "", "level": 1, "category": "здоровье", "experience": 20, "experience_to_next_level": 100, "progress_percent": 20},
        ]
        for s in demo:
            self._add_skill_card(s)