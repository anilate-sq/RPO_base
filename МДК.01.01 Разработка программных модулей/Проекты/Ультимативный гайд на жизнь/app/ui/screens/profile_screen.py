# Профиль пользователя
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel, QProgressBar
from PySide6.QtCore import Qt
from app.core.database import SessionLocal
from app.services.user_service import get_user_profile, get_user_skills

class ProfileScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.refresh()
        
    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        self.container = QWidget()
        self.profile_layout = QVBoxLayout(self.container)
        layout.addWidget(self.container)

    def refresh(self):
        while self.profile_layout.count(): self.profile_layout.takeAt().widget().deleteLater()
        try:
            db = SessionLocal()
            profile = get_user_profile(db, 1)
            if not profile:
                self.profile_layout.addWidget(QLabel("Профиль не найден", alignment=Qt.AlignCenter))
                return

            header = QFrame()
            header.setStyleSheet("background: #16213E; border-radius: 12px; padding: 20px;")
            h = QHBoxLayout(header)
            h.addWidget(QLabel("Будет позже", styleSheet="font-size: 48px; coloer: #4eCDC4;"))
            info = QVBoxLayout()
            info.addWidget(QLabel(profile["username"], objectName="titleLabel"))
            info.addWidget(QLabel(f"Уровень {profile['level']} Баланс: {profile['balance']:.0f} руб."))
            bar = QProgressBar()
            bar.setValue((profile['experience'] / max(profile['experience_to_next_level'], 1)) * 100)
            bar.setTextVisible(True); bar.setObjectName("xpBar")
            info.addWidget(bar)
            h.addLayout(info)
            self.profile_layout.addWidget(header)
            skills = get_user_skills(db, 1)
            if skills:
                self.profile_layout.addWidget(QLabel("Список навыков: ", objectName="titleLabel", styleSheet="margin-top: 20px;"))
                for s in skills[:5]:
                    row = QHBoxLayout()
                    row.addWidget(QLabel(f'{s.get('icon', '')} {s['name']} Уровень{s['level']}'))
                    p = QProgressBar(); p.setMaximum(100); p.setValue(s['progress_percent']); p.setObjectName('energyBar')
                    row.addWidget(p)
                    f = QFrame(); f.setLayout(row); f.setStyleSheet("background: transparent;")
                    self.profile_layout.addWidget(f)
        except Exception as e:
            self.profile_layout.addWidget(QLabel("Ошибка загрузки профиля", alignment=Qt.AlignCenter))
        finally:
            if 'db' in locals(): db.close()