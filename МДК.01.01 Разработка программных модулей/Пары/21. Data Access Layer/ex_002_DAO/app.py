import os
import sys

sys.path.append(os.path.abspath('C:/Users/Андрей/Desktop/РПО-git/RPO_base/МДК.01.01 Разработка программных модулей/Пары/21. Data Access Layer'))

from ex_002_DAO.services.recipesService import (
    RecipeService
)


recipes = RecipeService.get_all()

name = input('Введите название рецепта: ')
category = input("Тут будет select/combo box, а пока что напишите название: ")
level = input("Тут будет select/combo box, а пока что напишите уровень сложности: ")
description = input('Введите описание или нажмите 0, если хотите оставить его пустым: ')
if description == '0':
    description = None

RecipeService.add(name, category, level, description)

# Можно сделать меню