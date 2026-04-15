# Конфигурация проекта
import os
from pathlib import Path
from dotenv import load_dotenv

# Загрузка переменных окружжения
load_dotenv()

# Базовая директория проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Настройка БД
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "lifeguide")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "123")

# Строка подключения
DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Настройка приложения
APP_NAME = os.getenv("APP_NAME", "Ультимативный гайд на жизнь")
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")
APP_ENV = os.getenv("APP_ENV", "development")

# Пути
QML_DIR = BASE_DIR / "app" / "ui" / "qml"
RESOURCE_DIR = BASE_DIR / "app" / "resources"