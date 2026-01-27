# Простая система управления блюдами

import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QListWidget,
    QVBoxLayout
)

# Структура рецепта:
# {
#     название = рецепт,
# }

# Логика приложения
class RecipeService:
    def __init__(self):
        self.recipes = {
            "Блинчики": "Индгридиенты: Мука, Соль, Сахар, Молоко, Яйца. Жарить на сковородке.",
            "Цезарь(салат)": "Индгридиенты: Курица/Лосось/Бекон, Салат, Пармезан, Соус.",
            "Пицца Маргарита": "Индгридиенты: Тесто, Соус, Сыр."
        }

    # Получение списка рецептов
    def get_recipes(self):
        return list(self.recipes.keys())
    
    def get_recipe_detail(self, name):
        return self.recipes.get(name, "Рецепт не найден")
    
# GUI
class RecipeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Меню рецептов')
        self.resize(300, 200)
        self.service = RecipeService()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        self.list_widget = QListWidget()
        self.list_widget.addItems(self.service.get_recipes()) # Добавляем рецепты в список(ListWidget)
        self.list_widget.currentTextChanged.connect(self.show_recipe)
        layout.addWidget(self.list_widget)

        self.detail_label = QLabel('Выбранный рецепт')
        self.detail_label.setWordWrap(True)
        layout.addWidget(self.detail_label)

        self.setLayout(layout)

    def show_recipe(self, name):
        detail = self.service.get_recipe_detail(name)
        self.detail_label.setText(detail)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RecipeWindow()
    window.show()
    sys.exit(app.exec())

# Идеи по развитию:
# 1. Добавление рецепта;
# 2. Удаление рецепта;
# 3. Категории;
# 4. Экспорт из файла;
# 5. Поиск.