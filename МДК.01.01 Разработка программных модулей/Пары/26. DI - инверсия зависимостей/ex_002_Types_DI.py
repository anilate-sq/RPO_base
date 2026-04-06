#1. Конструкторная инъекция(Constructor Injection);

class EmailService:
    def send(self, message):
        print('Отравлено сообщение: ', message)
    
class NotificationService:
    def __init__(self, email_service: EmailService):
        self.email_service = email_service

    def notify(self, message):
        self.email_service.send(message)

# Использование
email = EmailService()
notifier = NotificationService(email) # Внедрение зависимости
notifier.notify("Сообщение")

#2. Внедрение через метод(Setter Injections/Method Injections);
class EmailService:
    def send(self, message):
        print('Отравлено сообщение: ', message)
    
class NotificationService:
    def __init__(self):
        self.email_service = None

    def set_email_service(self, email_service: EmailService):
        self.email_service = email_service

    def notify(self, message):
        if self.email_service:
            self.email_service.send(message)

# Использование
email = EmailService()
notifier = NotificationService() 
notifier.set_email_service(email) # Внедрение через метод
notifier.notify("Сообщение")

#3. Внедрение через аттрибут(Interface Injection). P.s. Нету в презентации
class NotificationService:
    def __init__(self):
        self.email_service = None

# Использование
email = EmailService()
notifier.email_service = EmailService()# Прямое присваивание
notifier.notify("Сообщение")