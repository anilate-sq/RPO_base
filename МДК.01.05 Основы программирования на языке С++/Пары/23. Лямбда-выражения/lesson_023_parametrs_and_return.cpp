#include <iostream>
#include <vector>

using namespace std;

int main(){

    // Использование параметров

    auto sum = [](int a, int b){
        return a + b;
    };

    cout << "Сумма чисел a и b = " << sum(18, 21) << endl;
    
    // Тип возращаемого значения

    // Без указания типа(определяется автоматически)
    auto f1 = [](int x){
        return x * x;
    };

    // Со строгим указанием типа
    auto f2 = [](int x) -> double{
        return x / 2.0;
    };

    cout << "Результат f1 = " << f1(3) << "\n" << "Результат f2 = " << f2(3) << endl;
}