#include <iostream>
#include <chrono> // Для работы со временем
#include <vector>
#include <algorithm>

using namespace std;

// Сравнение алгоритмов

void test1(vector<int> a){
    auto new_vector = all_of(a.begin(), a.end(), [](int x){
        return x > 8;
    });
};

void test2(vector<int> a){
    auto it = max_element(a.begin(), a.end());
};

int main(){
    vector<int> nums{1, 2, 3, 4, 5};
    setlocale(LC_ALL, "ru");
    // Тестирование времени двух алгоритмов
    auto start_test1 = chrono::steady_clock::now();
    test1(nums); // Запускаем test1
    auto end_test1 = chrono::steady_clock::now();
    auto start_test2 = chrono::steady_clock::now();
    test2(nums); // Запускаем test2
    auto end_test2 = chrono::steady_clock::now();
    // Подсчет времени
    auto test1_mks = chrono::duration_cast<chrono::microseconds>(end_test1 - start_test1);
    auto test2_mks = chrono::duration_cast<chrono::microseconds>(end_test2 - start_test2);

    // Сравниваем время выполнения и выводим результат
    if (test1_mks > test2_mks){
        cout << "Выборка по условию работает дольше" << endl;
    }

    else if (test1_mks < test2_mks){
        cout << "Поиск максимального элемента работает дольше" << endl;
    }

    else{
        cout << "Алгоритмы равны";
    }

    cout << "Выборка по условию выполнялась: " << test1_mks.count() << " mks." << endl;;
    cout << "Поиск максимального элемента выполнялся: " << test2_mks.count() << " mks." << endl;
}