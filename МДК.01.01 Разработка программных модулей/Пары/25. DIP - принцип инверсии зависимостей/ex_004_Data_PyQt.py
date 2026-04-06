# Хранение данных для приложения PyQt

from abc import ABC, abstractmethod
from PyQt6.QtWidgets import (
    QApplication
)


# Абстрактный класс
class StorageInterface(ABC):
    @abstractmethod
    def save(self, data: dict) -> bool:
        pass

    @abstractmethod
    def load(self) -> dict:
        pass

# Конкретные реализации
class DatabaseStorage(StorageInterface):
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def save(self, data: dict) -> bool:
        print('Сохранение данных в БД', data)
        # Сюда можно добавить работу с psycopg2
        return True
    
    def load(self) -> dict:
        print('Выгрузка из БД')
        return {
            # Полученные данные
        }
    
class FileStorage(StorageInterface):
    def __init__(self, file):
        self.file = file

    def save(self, data: dict) -> bool:
        print('Сохранение данных в Файл', self.file,  data)
        # Сюда можно добавить работу с json
        return True
    
    def load(self) -> dict:
        print('Выгрузка из Файла')
        return {
            # Полученные данные
        }
    
class CloudStorage(StorageInterface):
    def __init__(self, api_key):
        self.api_key = api_key

    def save(self, data: dict) -> bool:
        print('Сохранение данных в Облако', data)
        # Сюда можно добавить работу с API облака
        return True
    
    def load(self) -> dict:
        print('Выгрузка из облака')
        return {
            # Полученные данные
        }
    
# Сервис для приложения
class DataService:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def save_data(self, data):
        return self.storage.save(data)
    
    def load_data(self):
        return self.storage.load()
    
# Итоговая реализация
class MainWindow(QApplication):
    def __init__(self):
        super().__init__()

        # Выбор того где хранить данные
        storage = DatabaseStorage("postgresql://user:pass@localhost/db_name")
        storage = FileStorage("data.json")
        storage = CloudStorage("api-key-qwe")

        self.data_service = DatabaseStorage(storage)