# Только интерфейс, только отображение данных

'''
В основном включает в себя такие методы как:
- show_info();
- show_menu();
- add_click();
- update_click();
- delete_click().
'''

from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout
from PyQt6.QtCore import pyqtSignal

class ControlPanelWidget(QWidget):
        add_clicked = pyqtSignal()

        def __init__(self):
                super().__init__()
                layout = QHBoxLayout()
                add_button = QPushButton('Кнопка')
                add_button.clicked.connect(self.add_clicked)

                layout.addWidget(add_button)
                self.setLayout(layout)