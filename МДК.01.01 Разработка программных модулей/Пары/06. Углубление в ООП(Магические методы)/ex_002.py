# Методы __len__ и __getitem__

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    # Использование метода __len__
    def __len__(self):
        return self.pages
    
    def __str__(self):
        return f'Книга: {self.title}'

b1 = Book('1984', 480)
print(b1, len(b1))

class Team:
    def __init__(self, members):
        self.members = members

    def __getitem__(self, index):
        return self.members[index]

t1 = Team(['Гриша', 'Миша', 'Ваня'])
print(t1[2])