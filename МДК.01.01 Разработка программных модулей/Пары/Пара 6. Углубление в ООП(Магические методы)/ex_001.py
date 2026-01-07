# Создаем класс Point для работы с графиком координатом
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Магический методы для оператора +
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    # Магический метод для функции print()
    def __str__(self,):
        return f'X: {self.x}\nY: {self.y}'
    
p1 = Point(2, 3)
p2 = Point(7, 5)

print(p1 + p2)