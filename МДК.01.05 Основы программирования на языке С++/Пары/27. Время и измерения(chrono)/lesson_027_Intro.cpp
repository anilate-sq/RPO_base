#include <iostream>
#include <chrono> // Для работы со временем
#include <vector>
#include <algorithm>

using namespace std;

// Базовая работа со временем

void test(vector<int> a){
    transform(a.begin(), a.end(), a.begin(), [](int x){
        return x * 2;
    });

    auto it = find_if(a.begin(), a.end(), [](int x){
        return x > 3;
    });
};

int main(){
    vector<int> nums{1, 2, 3, 4, 5};
    setlocale(LC_ALL, "ru");
    auto time_in = chrono::steady_clock::now();
    test(nums);
    auto time_out = chrono::steady_clock::now();
    auto duration = time_out - time_in;
    auto ms = chrono::duration_cast<chrono::microseconds>(duration); 
    cout << "Затраченное время на выполнения test составляет: " << ms.count() << "ms." << endl;
}