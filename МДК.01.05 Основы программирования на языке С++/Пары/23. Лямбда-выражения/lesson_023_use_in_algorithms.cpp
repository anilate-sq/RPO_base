#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){

    // Примеры взаимодействия с алгоритмами

    // Пример с for_each
    vector<int> v = {1, 2, 3, 4, 5};
    for_each(v.begin(), v.end(), [](int x){
        cout << x << " ";
    });

    // Пример с find_if
    auto it = find_if(v.begin(), v.end(), [](int x){
        return x > 3;
    });

    // Пример с count_if
    auto count = count_if(v.begin(), v.end(), [](int x){
        return x % 2 != 0;
    });

    // Просмотр результата
    
    cout << "Элементы вектора, которые > 3: " << it[0] << " " << it[1];
    cout << "\nКоличество нечетных элементов в векторе: " << count;
}