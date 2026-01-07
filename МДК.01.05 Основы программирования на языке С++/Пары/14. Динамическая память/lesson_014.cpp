#include <iostream>

// Рабочий примерчик
void getA() {
    int a = 10;
    std::cout << &a << std::endl;
}

void getB() {
    int b = 10;
    std::cout << &b << std::endl;
}

/// <summary>
/// Создание массива из n-элементов
/// </summary>
/// <param name="n">Количество элементов</param>
/// <returns></returns>
int* createArr(int n) {
    return new int[n];
}

int main()
{
    setlocale(LC_ALL, "ru");

    // Потенциально рабочий пример 
    int a = 15;
    std::cout << &a << std::endl;
    if (a > 10) {
        int b = 12;
        std::cout << &b << std::endl;
    }

    int c = 21;
    std::cout << &c << std::endl;

    getA();
    getB();
    
    // Потенциально рабочий пример 
    {
        int a = 10;
        std::cout << &a << std::endl;
    }

    {
        int b = 10;
        std::cout << &b << std::endl;
    }

    // Работа с динамической памятью
    int* p = new int(21);
    int* p1 = new int(142);
    std::cout << p << std::endl;
    std::cout << p1 << std::endl;

    // Без инициализации

    int* p2 = new int; // Ячейка выделилась
    *p2 = 141; // Заполняем ячейку

    /*
        Адреса в стеке:
        00000004C6FCF774
        00000004C6FCF794
        00000004C6FCF7B4
        00000004C6FCF654
        00000004C6FCF654
        00000004C6FCF7D4
        00000004C6FCF7F4

        Адреса в куче:
        0000013EC79DE080
        00000218131FE3C0
    */

    // Удаление
    delete p1;
    delete p;
    delete p2;
    // delete[] - удаление массива;

    // Практические примеры
    // Пример 1. Наполнение и чистка массива;

    int size = 5;
    int* arr = new int[size];
    
    for (int i = 0; i < size; i++) {
        std::cin >> arr[i]; // Заполнение
    }

    delete[] arr; // Очищаем

    // Пример 2. Поиск минимального элемента
    int n;
    std::cin >> n;
    arr = new int[n];

    for (int i = 0; i < n; i++) {
        std::cin >> arr[i];
    }
    
    int min = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] < min) {
            min = arr[i];
        }
    }

    std::cout << "Минимальный элемент: " << min;
    delete[] arr;

    // Про висячий указатель
    int* p3 = new int(21);
    delete p3;
    std::cout << *p3; // ОПАСНО: лучше не повторять
    p3 = nullptr; // Разыменование

    // Пример работы с функцией

    arr = createArr(10);
    delete[] arr;
    arr = nullptr;
}