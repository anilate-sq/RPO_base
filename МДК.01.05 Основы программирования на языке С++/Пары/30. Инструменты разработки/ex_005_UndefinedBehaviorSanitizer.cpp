#include <iostream>
#include <vector>
#include <windows.h> // Для PowerShell

using namespace std;

int main(){
    SetConsoleOutputCP(65001); // Для PowerShell

    int a = INT_MAX;
    int b = a + 1; // Неопределенное поведение при signed integer overflow
    cout << "Результат: " << b << endl;

// Компиляция: g++ ex_005_UndefinedBehaviorSanitizer.cpp -o example_005 -fsanitize=undefined    
}
