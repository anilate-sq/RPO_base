#include <iostream>
#include <algorithm> // Подключаем <algorithm>
#include <vector>
using namespace std;

int main() {
    setlocale(LC_ALL, "");

    // Список основных алгоритмов:
    // sort
    // find
    // count и count_if
    // find_if
    // for_each
    // remove и remove_if
    // all_of / any_of / none_of
    // min_element / max_element
    // transform
    // copy

    vector<int> v1 = { 71, 21, 13, 42, 15, 32, 90, 22, 13, 78, 13 };

    // Обычная сортировка
    sort(v1.begin(), v1.end());

    cout << "Сортировка без условия" << endl; 
    // Стандартный вывод
    for_each(v1.begin(), v1.end(), [](int x) {
        cout << x << endl;
    });

    // Сортировка с условием(обратная сортировка)
    sort(v1.begin(), v1.end(), [](int a, int b) {
        return a > b;
    });

    cout << "Сортировка с условием" << endl;
    for_each(v1.begin(), v1.end(), [](int x) {
        cout << x << endl;
    });

    // find
    auto it = find(v1.begin(), v1.end(), 10);

    cout << "Ссылка на искомое число: " << &it;
    
    // count
    int quantity1 = count(v1.begin(), v1.end(), 13);
    int quantity2 = count(v1.begin(), v1.end(), 90);

    cout << "Количество числа 13: " << quantity1 << endl;
    cout << "Количество числа 90: " << quantity2 << endl;

    // получение количества четных элементов
    int c = count_if(v1.begin(), v1.end(), [](int x) {
        return x % 2 == 0;
    });

    auto it2 = find_if(v1.begin(), v1.end(), [](int x) {
        return  x < 20;
    });

    cout << "Первый попавшийся элемент, который < 20: " << *it2 << endl;

    // remove

    remove(v1.begin(), v1.end(), 15);
    cout << "Сортировка с условием" << endl;

    for_each(v1.begin(), v1.end(), [](int x) {
        cout << x << endl;
    });

    // all_of, any_of, none_of

    all_of(v1.begin(), v1.end(), [](int x) {
        return x > 40;
    });

    none_of(v1.begin(), v1.end(), [](int x) {
        return x > 40;
    });

    any_of(v1.begin(), v1.end(), [](int x) {
        return x > 40;
    });

    // Получение минимального и максимального элементов
    auto min = min_element(v1.begin(), v1.end());
    auto max = max_element(v1.begin(), v1.end());

    // transform
    transform(v1.begin(), v1.end(), v1.begin(), [](int x) {
        return x / 2;
    });

    cout << "После преобразования: ";

    for_each(v1.begin(), v1.end(), [](int x) {
        cout << x << endl;
    });

    //copy - количество элементов должно совпадать
    vector<int> v2;
    copy(v1.begin(), v1.end(), back_inserter(v2));

    cout << "Вывод нового вектора: " << endl;
    for_each(v1.begin(), v1.end(), [](int x) {
        cout << x << endl;
        });
}