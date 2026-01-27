# Синтаксис виджета

class CustomWidget(QWidget):
        def __init__(self):
                super().__init__()
                self.setup_ui()
        def setup_ui(self):
                pass

# Пример создания виджета(карточка рецепта)
class RecipeCard(QWidget):
        clicked = pyqtSignal(str) # Создание пользовательского сигнала
        def __init__(self, name, category, description):
                super().__init__()
                self.name = name
                self.category = category
                self.description = description
                self.setup_ui()

card = RecipeCard('Борщ', 'Супы', 'Описание...')
layout.addWidget(card)


