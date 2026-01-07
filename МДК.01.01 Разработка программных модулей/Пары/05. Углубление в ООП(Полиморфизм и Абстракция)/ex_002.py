from abc import *

class Payment(ABC):    
    @abstractmethod
    def pay(self, amount):
        pass

class cardPayment(Payment):
    def pay(self, amount):
        return f'Оплата картой: {amount}'

class cashPayment(Payment):
    def pay(self, amount):
        return f'Оплата наличными: {amount}'
    
payments = [cardPayment(), cashPayment()]

for pay in payments:
    print(pay.pay(250))