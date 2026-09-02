"""
Диалог просмотра и завершения гайда
"""
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
    QProgressBar, QPushButton, QTextEdit, QScrollArea, QMessageBox
)
from PySide6.QtCore import Qt
from app.core.database import SessionLocal
from app.services import guide_service
from app.core.app_context import app_context

class GuideViewDialog(QDialog):
    def __init__(self, guide: dict, parent=None):
        super().__init__(parent)
        self.guide = guide
        self.setWindowTitle(f"{guide['title']}")
        self.setMinimumSize(700, 600)
        self._build_ui()
        self._load_progress()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(15)

        # Заголовок
        title_lbl = QLabel(self.guide["title"], objectName="titleLabel")
        title_lbl.setStyleSheet("font-size: 20px;")
        layout.addWidget(title_lbl)

        # Прогресс-бар
        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setObjectName("xpBar")
        layout.addWidget(self.progress_bar)

        # Контент гайда (скроллируемый)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")

        self.content_text = QTextEdit()
        self.content_text.setReadOnly(True)
        self.content_text.setObjectName("primaryInput")
        # Заглушка контента (в проде тут будет JSON из guide['content'])
        self.content_text.setHtml(f"""
        <h3>{self.guide.get('short_description', 'Описание гайда')}</h3>
        <p><b>Время чтения:</b> {self.guide.get('read_time', '?')} мин</p>
        <p><b>Сложность:</b> {self.guide.get('difficulty', 'средняя')}</p>
        <p><b>Награда:</b> +{self.guide.get('xp_reward', 0)} XP</p>
        <hr>
        <p>1. Внимательно прочитай материал.</p>
        <p>2. Примени на практике.</p>
        <p>3. Отметь прогресс, когда будешь готов.</p>
        <p>💡 <i>Совет: Делай перерывы каждые 25 минут.</i></p>
        """)
        scroll.setWidget(self.content_text)
        layout.addWidget(scroll, 1)

        # Кнопки действий
        btn_layout = QHBoxLayout()
        
        self.btn_save = QPushButton("+20% прогресса", objectName="infoButton")
        self.btn_save.clicked.connect(self._add_progress)
        btn_layout.addWidget(self.btn_save)

        self.btn_complete = QPushButton("Завершить гайд", objectName="successButton")
        self.btn_complete.clicked.connect(self._complete_guide)
        btn_layout.addWidget(self.btn_complete)

        btn_close = QPushButton("Закрыть", objectName="dangerButton")
        btn_close.clicked.connect(self.reject)
        btn_layout.addWidget(btn_close)

        layout.addLayout(btn_layout)

    def _load_progress(self):
        """Загрузка текущего прогресса из БД"""
        try:
            db = SessionLocal()
            user_id = app_context.get_user_id()
            progress = guide_service.get_progress(db, user_id, self.guide["id"])
            if progress:
                self.progress_bar.setValue(progress["progress_percent"])
        except Exception as e:
            print(f"Error loading progress: {e}")
        finally:
            if 'db' in locals():
                db.close()

    def _add_progress(self):
        """Добавить 20% к прогрессу"""
        try:
            db = SessionLocal()
            user_id = app_context.get_user_id()
            
            # Получаем текущий прогресс
            progress = guide_service.get_progress(db, user_id, self.guide["id"])
            current = progress["progress_percent"] if progress else 0
            
            # Увеличиваем на 20%
            new_percent = min(100, current + 20)
            guide_service.update_progress(db, user_id, self.guide["id"], new_percent)
            
            self.progress_bar.setValue(new_percent)
            QMessageBox.information(self, "Прогресс сохранён", f"Твой прогресс: {new_percent}%")
            
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить прогресс:\n{e}")
        finally:
            if 'db' in locals():
                db.close()

    def _complete_guide(self):
        """Завершить гайд и получить награду"""
        try:
            db = SessionLocal()
            user_id = app_context.get_user_id()
            
            # Сначала обновляем прогресс до 100%
            guide_service.update_progress(db, user_id, self.guide["id"], 100)
            
            # Завершаем гайд и получаем награду
            result = guide_service.complete_guide(db, user_id, self.guide["id"])
            
            if result["rewarded"]:
                QMessageBox.information(
                    self, 
                    " Гайд завершён!", 
                    f"Ты получил:\n+{result['xp_earned']} XP\n\nНавыки обновлены: {len(result.get('skill_updated', []))}"
                )
                self.accept()  # Закрываем диалог
            else:
                QMessageBox.warning(self, "Внимание", result.get("message", "Награда уже получена"))
                
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось завершить гайд:\n{e}")
        finally:
            if 'db' in locals():
                db.close()