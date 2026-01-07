#include <iostream>

void AddValue(int& n) {
    n++;
}

void ConstValue(const int& n) {
    int b = 5;
    std::cout << "a + b = " << n + b << "\n";
}

int& getElement(int arr[], int index) {
    return arr[index];
}

int main()
{
    int a = 10;
    for (int i = 0; i < 10; i++) {
        AddValue(a);
    }
    std::cout << "a = " << a << "\n";
    ConstValue(a);
    int arr[3] = { 1, 2, 3 };
    getElement(arr, 1) = 12; // идентично arr[1] = 12
    getElement(arr, 0) = 10; // идентично arr[0] = 10 
    for (int i = 0; i < 3; i++) {
        std::cout << "arr[" << i << "] = " << arr[i] << std::endl;
    }

    for (auto& x : arr) {
        x += 2;
        std::cout << x << std::endl;
    }
}