#include <iostream>
#include <vector>
#include<windows.h> // Для PowerShell

using namespace std;

int main(){
    SetConsoleOutputCP(65001); // Для PowerShell

    int arr[10];
    arr[10] = 123; // Ошибка: выход за границы массивы
    cout << arr[10] << endl;
    return 0;

    // Компиляция: g++ ex_004_AddressSanitizer.cpp -o example_004 -fsanitize=address
}
