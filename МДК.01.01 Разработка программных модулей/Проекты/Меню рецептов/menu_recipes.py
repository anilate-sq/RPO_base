import sys
import json
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QListWidget,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QComboBox,
    QPushButton,
    QMessageBox
)

PATH = 'recipes.json'

class RecipeService:
    def __init__(self):
        self.recipes = {}
        self.load_recipes()

    # Выгрузка рецептов с recipes.json
    def load_recipes(self):
        try:
            with open(PATH, 'r', encoding='UTF-8') as file:
                self.recipes = json.load(file)
        except(FileNotFoundError, json.JSONDecodeError):
            # Проверка на наличие файлы и корректность json
            self.recipes = {
            "Блинчики": {
                "category": "Десерты",
                "description": "Ингредиенты: мука, молоко, яйца, сахар. Жарить на сковороде до золотистой корочки."
            },
            "Салат Цезарь": {
                "category": "Салаты",
                "description": "Ингредиенты: курица, салат, пармезан, сухарики, соус Цезарь."
            }
        }  

    # Выгрузка рецептов в recipes.json
    def save_recipes(self):
        with open(PATH, 'w', encoding='utf-8') as file:
            json.dump(self.recipes, file, ensure_ascii=False, indent=4)
    
    # Получение списка рецептов с учетом фильтров
    def get_recipes(self, category_filter=None, search_filter=None):
        results = []
        for name, info in self.recipes.items():
            if category_filter and info['category'] != category_filter:
                continue
            if search_filter and search_filter.lower() not in name.lower():
                continue
            results.append(name)
        return results
    
    # Получения описания конкретного рецепта
    def get_recipe_detail(self, name):
        return self.recipes.get(name, {}).get("description", "Рецепт не найден")
    
    # Добавления рецепта, с проверкой на его отсутствие в списке
    def add_recipe(self, name, category, description):
        if name in self.recipes:
            return False
        self.recipes[name] = {"category": category, "description": description}
        self.save_recipes()
        return True
# GUI
class RecipeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Меню рецептов')
        self.resize(300, 200)
        self.service = RecipeService()
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout()
        
        # Интерфейс поиска
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText('Поиск')
        self.search_input.textChanged.connect(self.refresh_list)
        search_layout.addWidget(QLabel("Поиск:"))
        search_layout.addWidget(self.search_input)
        main_layout.addLayout(search_layout)

        # Фильтрация по категориям
        filter_layout = QHBoxLayout()
        self.category_filter = QComboBox()
        self.category_filter.addItem('Все')
        self.category_filter.addItems(['Супы', 'Салаты', 'Десерты'])        
        self.category_filter.currentTextChanged.connect(self.refresh_list)
        filter_layout.addWidget(QLabel('Категория:'))
        filter_layout.addWidget(self.category_filter)
        main_layout.addLayout(filter_layout)
        
        # Список рецептов
        self.list_widget = QListWidget()
        self.list_widget.currentTextChanged.connect(self.show_recipe)
        main_layout.addWidget(self.list_widget)

        # Описание рецепта
        self.detail_label = QLabel('Выбранный рецепт')
        self.detail_label.setWordWrap(True)
        main_layout.addWidget(self.detail_label)
     

        # Добавление рецепта
        add_layout = QVBoxLayout()
        self.new_name = QLineEdit()
        self.new_name.setPlaceholderText('Название рецепта')
        self.new_category = QComboBox()
        self.new_category.addItems(['Супы', 'Салаты', 'Десерты'])
        self.new_description = QLineEdit()
        self.new_description.setPlaceholderText('Описание рецепта')
        self.add_button = QPushButton('Добавить кнопку')
        self.add_button.clicked.connect(self.add_recipe)
        add_layout.addWidget(QLabel("Добавить рецепт"))
        add_layout.addWidget(self.new_name)
        add_layout.addWidget(self.new_category)
        add_layout.addWidget(self.new_description)
        add_layout.addWidget(self.add_button)
        main_layout.addLayout(add_layout)

        self.setLayout(main_layout)

    # Просмотр всех рецептов
    def refresh_list(self):
        category = self.category_filter.currentText()
        if category == 'Все':
            category = None
        search = self.search_input.text()
        recipes = self.service.get_recipes(category_filter=category, search_filter=search)
        self.list_widget.clear()
        self.list_widget.addItems(recipes)
        self.detail_label.setText('Выберите рецепт')


    # Вывод информации о рецепте
    def show_recipe(self, name):
        detail = self.service.get_recipe_detail(name)
        self.detail_label.setText(detail)

    # Добавление рецепта
    def add_recipe(self):
        name = self.new_name.text().strip()
        category = self.new_category.currentText()
        description = self.new_description.text().strip()

        if not name or not description:
            QMessageBox.warning(self, "Ошибка", "Введите название рецепта")

        if self.service.add_recipe(name, category, description):
            QMessageBox.information(self, "Победа", f"Рецепт {name} был добавлен")
            self.new_name.clear()
            self.new_description.clear()
            self.refresh_list()

        else:
            QMessageBox.warning(self, 'Ошибка', f'Рецепт \'{name}\' уже существует')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RecipeWindow()
    window.show()
    sys.exit(app.exec())