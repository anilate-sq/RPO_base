LIST_LOG= []

class LogMixin:
      def log_message(self, message, list):
            print(f'[LOG: {message} ]')
            list.append(message)
class Database:
      def save(self):
            print('Данные сохранены')

class DatabaseOperation(Database, LogMixin):
      def get_data(self):
            super().save()
            self.log_message('Запрос на получение данных', LIST_LOG)
      def set_data(self):
            super().save()
            self.log_message('Запрос на отправку данных', LIST_LOG)

do = DatabaseOperation()
do.get_data()
do.set_data()
print(LIST_LOG)