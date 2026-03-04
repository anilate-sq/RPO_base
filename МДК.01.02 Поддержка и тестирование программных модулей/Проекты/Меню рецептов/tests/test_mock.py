import pytest
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.append(os.path.abspath('C:\\RPO-git\\RPO_base\\МДК.01.02 Поддержка и тестирование программных модулей\\Проекты\\Меню рецептов'))
from service.recipe_service import RecipeService

class TestRecipeGetAll:
        def test_get_all_return_list(self, mock_conn, mock_cursor):
                # Настраиваем поведение mock-объекта
                mock_cursor.fetchall.return_value = [
                        (1, "Том Ям", "Суп", "meduim", "Основное блюдо"),
                        (2, "Пельмени", "Сибирское блюдо", "enum", "Основное блюдо")
                ]

                # Выполнение тестируемого кода
                with patch('db.db.get_conn', return_value=mock_conn):
                        result = RecipeService.get_all()
                
                # Проверка результата
                assert isinstance(result, list)
                assert len(result) == 2
                assert result[0][1] == 'Том Ям'

        # Проверка вызова методов
        def test_get_all_calls_correct_query(self, mock_conn, mock_cursor):
                with patch('db.db.get_conn', return_value=mock_conn):
                        RecipeService.get_all()
                
                # Проверка что execute был вызван
                mock_cursor.execute.assert_called_once()

                # Проверка содержимого запроса
                call_args = mock_cursor.execute.call_args[0][0]
                assert 'SELECT' in call_args.upper()
                assert 'recipes.recipes' in call_args
                assert 'JOIN' in call_args.upper()
                assert 'recipes.categories' in call_args

        # Тестирование ошибок
        def test_add_recipe_rollback_on_error(self, mock_conn, mock_cursor):
                # Имимация ошибки
                mock_cursor.fetchall.side_effect = Exception('DB Error')
                with patch('db.db.get_conn', return_value=mock_conn):
                        with pytest.raises(Exception):
                                RecipeService.add_recipe('Рецепт', 1, 'easy') # Допускаем ошибку

                # Проверяем rollback
                mock_conn.rollback.assert_called_once()

        # Тест на закрытие соединения
        def test_get_all_closes_resources(self, mock_conn, mock_cursor):
                mock_cursor.fetchall.return_values = []
                with patch('db.db.get_conn', return_value=mock_conn):
                        RecipeService.get_all()
                mock_cursor.close.assert_called_once()
                mock_conn.close.assert_called_once()

# Задание описать классы TestRecipeAddRecipe и TestRecipeGetById и написать для них тесты на примере класса TestRecipeGetAll