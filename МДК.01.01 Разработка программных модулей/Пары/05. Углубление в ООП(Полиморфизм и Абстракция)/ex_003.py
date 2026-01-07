from abc import *

class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotifier(Notifier):
    def send(self, message):
        print(f'Сообщение {message} пришло на почту')
    
class SMSNotifier(Notifier):
    def send(self, message):
        print(f'Сообщение {message} на телефон')

def notifyAll(notifiers, message):
    for n in notifiers:
        n.send(message)

notifyAll([EmailNotifier(), SMSNotifier()], 'Текст сообщения')