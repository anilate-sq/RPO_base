class Student:
      def __init__(self, name, age):
            # Аттрибуты объекта
            self.name = name 
            self.age = age
      surname = 'Попов' # Аттрибут класса

std1 = Student('Иван', 17)
print(std1.surname) # Значение аттрибута класса у нас для всех экземпляров 
print(std1.name) # Значение аттрибут объекта уникально для каждого объекта
std1.surname = 'Иванов' # Смена аттрибута surname


