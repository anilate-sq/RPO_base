# Комбинированный пример: Создание типа данных Array

class Array:
    def __init__(self, *components):
        self.components = list(components)

    # Реализуем суммирование
    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError('Длина массивов должна быть одинакововой')
        result = [a + b for a, b in zip(self.components, other.components)]
        return Array(*result)
    
    # Реализуем вычитание
    def __sub__(self, other):
        if len(self.components) !~= len(other.components):
            raise ValueError('Длина массивов должна быть одинаковой')
        result = [a - b for a, b in zip(self.components, other.components)]
        return Array(*result)
    
    # Реализуем получение длины массива
    def __len__(self):
        return len(self.components)
    
    # Реализуем получение значения по индексу из массива
    def __getitem__(self, index):
        return self.components[index]
    
    def __repr__(self):
        return f'Array({', '.join(map(str, self.components))})'

v1 = Array(1, 7, 21)
v2 = Array(14, 2, 43)

print(v1 + v2) # Суммирование массивов
print(v2 - v1) # Вычетание массивов
print(len(v1)) # Просмотр количества элементов в массиве
print(v1[2]) # Получение элемента по индексу из массива

# Примечание: добавить функции map(), reduce(), filter() в перечень тем для изучения