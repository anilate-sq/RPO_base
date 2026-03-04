'''
Библиотека книг - простое приложение для управления книгами с целью демонстрации слоистой архитектуры

Структура проекта:
|_data_layer/           - Уровень доступа к данным(DAL)
|_business_layer/       - Уровень бизнес-логики(BLL)
|_presentation_layer/   - Уровень интерфейса(UI)
|_main.py               - Точка входа

Предварительные требования:
1. Установлен PostgreSQL
2. Наличие базы данных library/library_db
3. Установлен psycopg2: pip install psycopg2-binary
'''

import sys
from pathlib import Path

# Добавление корень проекта в путь импортов
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

'''
DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'library',
    'user': 'postgres',
    'password': 'password'
}
'''
def main():
    pass

if __name__ == '__main__':
    main()