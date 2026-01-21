#include <iostream>
#include <array>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

int main(){

    // Объявляем переменные
    string name = "Ivan";
    array<int, 5> numbers {1, 2, 5, 3, 4};
    vector<int> new_numbers {2, 5, 3, 9};
    map<string, int> map_users{
        {"Victor", 21},
        {"Ilya", 73},
        {"Grisha", 19}};

    // Общие методы
    cout << "Длина массива: " << numbers.size() << endl;
    cout << "Длина вектора: " << new_numbers.size() << endl;
    cout << "Длина map: " << map_users.size() << endl;

    cout << "Массив пустой: " << numbers.empty() << endl;
    cout << "Вектор пустой: " << new_numbers.empty() << endl; 
    cout << "Имя есть: " << name.empty() << endl; 

    cout << "Cписок первых элементов" << endl;
    cout << "Массив: " << numbers.front() << endl;
    cout << "Имя: " << name.front() << endl;
    
    cout << "Cписок последних элементов" << endl;
    cout << "Массив: " << numbers.back() << endl;
    cout << "Вектор: " << new_numbers.back() << endl;
    cout << "Имя: " << name.back() << endl;

    // Способы доступа

    // Первый способ: []
    cout << "Первый элемент массива: " << numbers[0] << endl;
    cout << "Второй элемент вектора: " << new_numbers[1] << endl;
    
    // Второй способ: at()
    cout << "Первый элемент массива: " << numbers.at(0) << endl;
    cout << "Второй элемент вектора: " << new_numbers.at(1) << endl;
    
    // Проверка
    cout << *numbers.begin() << endl;  
    cout << *numbers.end() << endl; // Адресная ячейка после последнего элемента
    
    for (auto i = numbers.begin(); i != numbers.end(); i++){
        cout << "Тип i:" << typeid(i).name() << endl;
        cout << "Текущий элемент: " << i << endl; 
    }

    sort(numbers.begin(), numbers.end()); // Сортировка

    for(int item : numbers){
        cout << item << endl;
    }
}