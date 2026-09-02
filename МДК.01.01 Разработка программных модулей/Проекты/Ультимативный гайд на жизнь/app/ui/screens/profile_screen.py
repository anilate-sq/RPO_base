"""
Экран профиля пользователя
"""
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel, QProgressBar
from PySide6.QtCore import Qt
from app.core.database import SessionLocal
from app.services.user_service import get_user_profile, get_user_skills
from app.core.app_context import app_context 

class ProfileScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.refresh()

    def init_ui(self):
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(30, 30, 30, 30)
        self.main_layout.setSpacing(20)

        # Контейнер для динамического контента
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setSpacing(15)
        self.main_layout.addWidget(self.content_widget)

    def refresh(self):
        while self.content_layout.count():
            item = self.content_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        try:
            db = SessionLocal()
            user_id = app_context.get_user_id()  
            
            profile = get_user_profile(db, user_id)
            if not profile:
                self.content_layout.addWidget(
                    QLabel("Профиль не найден", alignment=Qt.AlignCenter, objectName="subtitleLabel")
                )
                return

            header = QFrame()
            header.setObjectName("statusCard")  # Используем глобальный стиль
            header_layout = QHBoxLayout(header)
            header_layout.setContentsMargins(20, 20, 20, 20)

            # Аватар-заглушка
            avatar_lbl = QLabel("Профиль")
            avatar_lbl.setStyleSheet("font-size: 48px; color: #4CA885;") 
            header_layout.addWidget(avatar_lbl)

            info_layout = QVBoxLayout()
            info_layout.addWidget(QLabel(profile["username"], objectName="titleLabel"))
            
            stats_lbl = QLabel(f"Уровень {profile['level']}  |  Баланс: {profile['balance']:.0f} ₽")
            stats_lbl.setObjectName("subtitleLabel")
            info_layout.addWidget(stats_lbl)

            # Прогресс опыта
            xp_percent = int((profile["experience"] / max(profile["experience_to_next_level"], 1)) * 100)
            xp_bar = QProgressBar()
            xp_bar.setMaximum(100)
            xp_bar.setValue(xp_percent)  
            xp_bar.setTextVisible(True)
            xp_bar.setObjectName("xpBar")
            info_layout.addWidget(xp_bar)

            header_layout.addLayout(info_layout, 1)
            self.content_layout.addWidget(header)

            skills_lbl = QLabel("Твои навыки", objectName="titleLabel")
            skills_lbl.setStyleSheet("margin-top: 20px;")
            self.content_layout.addWidget(skills_lbl)

            skills = get_user_skills(db, user_id)
            if skills:
                for s in skills[:5]:  # Показываем топ-5
                    skill_row = QHBoxLayout()
                    skill_row.setContentsMargins(5, 5, 5, 5)

                    
                    name_lbl = QLabel(f"{s.get('icon', '')} {s['name']} [Lvl {s['level']}]")
                    name_lbl.setObjectName("subtitleLabel")
                    skill_row.addWidget(name_lbl)

                    skill_bar = QProgressBar()
                    skill_bar.setMaximum(100)
                    skill_bar.setValue(int(s["progress_percent"])) 
                    skill_bar.setTextVisible(True)
                    skill_bar.setObjectName("energyBar")
                    skill_row.addWidget(skill_bar, 1)

                    skill_frame = QFrame()
                    skill_frame.setLayout(skill_row)
                    skill_frame.setStyleSheet("background: transparent;")
                    self.content_layout.addWidget(skill_frame)
            else:
                self.content_layout.addWidget(
                    QLabel("Навыков пока нет. Изучай гайды и решай проблемы!", 
                           alignment=Qt.AlignCenter, objectName="subtitleLabel")
                )

        except Exception as e:
            print(f"ProfileScreen DB error: {e}")
            self.content_layout.addWidget(
                QLabel("Ошибка загрузки профиля. Попробуйте позже.", 
                       alignment=Qt.AlignCenter, objectName="trendDown")
            )
        finally:
            if 'db' in locals():
                db.close()