# Ультимативный гайд на жизнь

## Описание проекта

Приложение-гайд для студентов, по переходу в real life

## Инструкция по запуску

### 1. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 2. Настройка окружения
```bash
cp .env.example .env
# Отредактируйте .env, указав данные для подключение к PostgreSQL
```

### 3. Установка и настройка PostgreSQL
- Скачать установщик с https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
- Установить и запомнить пароль
- Создать БД через PgAdmin или psql

### 4. Импорт дампа БД

```bash
psql -U postgres -d lifeguide -f dump.sql
```

### 5. Проверка подключения

```bash
python test_db.py
```

### 6. Запуск приложения

```bash
python app/main.py
```

## Структура проекта

```bash

Ультимативный гайд на жизнь/
|— dump.sql                  # Дамп БД
|— requirements.txt          # Python завистимостей
|— .env.example              # Шаблон настроек проекта
|
|— app/
|  |— main.py                # Точка входа
|  |— config.py              # Конфигурация
|  |— core/
|  |   |— database.py        # Подключение к БД
|  |   |— models.py          # SQLAlchemy Модели
|  |— services/
|  |   |—                    # Бизнес-логика проекта
|  |— ui/
|     |— main_window.py      # Главное окно
|     |— styles.py           # QSS стили
|
|— docs/                     # Документация проекта
|— tests/                    # Тесты
```

## Технический стек

- **UI:** PySide6
- **СУБД:** PostgreSQL
- **ORM:** SQLAlchemy
- **Python:** 3.9.0+

## Документация

- [Техническое задание](docs/Техническое%20задание.md)
- [Описание ПО](docs/Описание%20ПО.md)
- [План проекта](docs/Ультимативный%20гайд%20на%20жизнь.%20ПЛАН.md)