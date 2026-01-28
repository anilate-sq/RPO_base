#include <iostream>
#include <vector>
#include <algorithm>
#include <functional> // Для того чтобы можно было использовать функцию как параметр
 
using namespace std;

/// @brief Функция, которая принимает вектор и возвращает четные элементы
/// @param v передаваемый вектор
/// @param pred функция для вывода массива
void process(const vector<int>& v, function<bool(int)> pred) {
    for(int x : v){
        if(pred(x)){
            cout << x << " ";
        }
    }
};

int main(){
    // Лямбда как параметр функции
    vector<int> v = {1, 2, 3, 4, 5};
    process(v, [](int x){
        return x % 2 == 0;
    });  
}