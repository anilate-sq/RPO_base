from services.recipesService import (
    get_all,
    add,
    edit,
    drop,
    get_by_category
)


recipes = get_all()

name = input('Введите название рецепта: ')
category = input("Тут будет select/combo box, а пока что напишите название: ")
level = input("Тут будет select/combo box, а пока что напишите уровень сложности: ")
description = ('Введите описание или нажмите 0, если хотите оставить его пустым: ')
if description == '0':
    description = None

add(name, category, level, description)

# Можно сделать меню