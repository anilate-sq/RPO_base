#include <iostream>
#include <vector>
using namespace std;

/*
    Функции объявляются вот здесь 

    Синтаксис:
    <тип_возвращаемых_данных><название_функции>(<список_параметров>){
        <тело_функции>
    }
*/

int a{ 10 };

/// <summary>
/// Функция для суммирования целых чисел
/// </summary>
/// <param name="a">Первое число для суммирования</param>
/// <param name="b">Второе число для суммирования</param>
/// <returns>Сумма a и b</returns>
int sum(int b) {
    return a + b;
}

double sum(double a, double b) {
    return a + b;
}

string sum(string a, string b) {
    return a + b;
}

void main()
{
    cout << sum(12, 15);
}


