import sys
import json
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QListWidget, QLineEdit,
    QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, QMessageBox
)

from PyQt6.QtCore import pyqtSignal

# Шапка
class HeaderWidget(QWidget):
        def __init__(self, title:str):
                super().__init__()
                layout = QVBoxLayout()
                label = QLabel(title)
                label.setStyleSheet('font-size: 18px; font-weight: bold;')
                layout.addWidget(label)
                self.setLayout(layout)

# Рецепт                 
class RecipeCardWidget(QWidget):
        selected = pyqtSignal(str)
        
        def __init__(self, name, category):
                super().__init__()
                self.name = name
                self.category = category
                self.setup_ui()
        
        def setup_ui(self):
                layout = QVBoxLayout()
                name_label = QLabel(self.name)
                name_label.setStyleSheet('font-weight: bold;')
                category_label = QLabel(f'Категория: {self.category}')

                button = QPushButton('Выбрать')
                button.clicked.connect(self.emit_selected)
                
                layout.addWidget(name_label)
                layout.addWidget(category_label)
                layout.addWidget(button)

                self.setLayout(layout)

        def emit_selected(self):
                self.selected.emit(self.name)

# Список рецептов
class RecipeListWidget(QWidget):
        recipe_selected = pyqtSignal(str)

        def __init__(self):
                super().__init__()
                self.layout = QVBoxLayout()
                self.setLayout(self.layout)
        
        def add_recipe(self, name, category):
                card = RecipeCardWidget(name, category)
                card.selected.connect(self.recipe_selected.emit)
                self.layout.addWidget(card)


# Панель управления
class ControlPanelWidget(QWidget):
        add_clicked = pyqtSignal()
        def __init__(self):
                super().__init__()
                layout = QHBoxLayout()

                add_button = QPushButton('Добавить рецепт')
                add_button.clicked.connect(self.add_clicked.emit)

                layout.addWidget(add_button)
                self.setLayout(layout)            

class MainWindow(QWidget):
        def __init__(self):
                super().__init__()
                self.setWindowTitle('Кулинарное меню')
                self.resize(500, 400)
                self.setup_ui()
        
        def setup_ui(self):
                main_layout = QVBoxLayout()

                self.header = HeaderWidget('Меню рецептов')
                self.recipe_list = RecipeListWidget()
                self.controls = ControlPanelWidget()

                self.recipe_list.recipe_selected.connect(self.on_recipe_selected)
                self.controls.add_clicked.connect(self.on_add_recipe)

                main_layout.addWidget(self.header)
                main_layout.addWidget(self.recipe_list)
                main_layout.addWidget(self.controls)

                self.setLayout(main_layout)

                self.recipe_list.add_recipe('Борщ', 'Супы')
                self.recipe_list.add_recipe('Торт "Наполеон"', 'Сладости')
                self.recipe_list.add_recipe('Индейка', 'Мясное')
        def on_recipe_selected(self, name):
                QMessageBox.information(self, 'Рецепт выбран', f'Вы выбрали: {name}')
        
        def on_add_recipe(self):
                QMessageBox.information(self, 'Добавление', 'Тут будет форма добавления рецепта')

if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec())