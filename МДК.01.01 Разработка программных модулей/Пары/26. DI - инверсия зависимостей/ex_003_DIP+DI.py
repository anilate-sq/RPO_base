from abc import ABC, abstractmethod


# DIP: Абстракция
class StorageInterface(ABC):
    @abstractmethod
    def save(self, data):
        pass


# DIP: Конкретные реализации
class DatabaseStorage(StorageInterface):
    def save(self, data):
        print(f"Сохраняем в БД: {data}")


class FileStorage(StorageInterface):
    def save(self, data):
        print(f"Сохраняем в файл: {data}")


# DI: Сервис получает зависимость извне
class DataService:
    def __init__(self, storage: StorageInterface):
        # внедряем абстракцию
        self.storage = storage
    
    def save_data(self, data):
        return self.storage.save(data)


# Использование
db_storage = DatabaseStorage()
data_service = DataService(db_storage)  # DI с DIP
data_service.save_data({"name": "Alice"})

# Легко сменить реализацию
file_storage = FileStorage()
data_service = DataService(file_storage)  # Другая реализация
data_service.save_data({"name": "Bob"})