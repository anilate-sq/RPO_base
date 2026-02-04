#include <iostream>
#include <chrono> // Для работы со временем
#include <vector>
#include <algorithm>

using namespace std;

void test(vector<int> a){
    auto new_vector = all_of(a.begin(), a.end(), [](int x){
        return x > 8;
    });
};

int main(){

    // Пользовательская длительность
    vector<int> nums{34, 1234, 32, 452, 12999};
    auto time_in = chrono::steady_clock::now();
    test(nums);
    auto time_out = chrono::steady_clock::now();
    chrono::duration<double> seconds = time_out - time_in; // Используем свой формат
};