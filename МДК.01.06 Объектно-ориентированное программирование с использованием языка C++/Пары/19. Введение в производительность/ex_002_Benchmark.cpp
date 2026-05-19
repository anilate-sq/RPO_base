#include <iostream>
#include <vector>
#include <chrono>
#include <numeric>
#include <algorithm>
using namespace std;

const size_t SIZE = 1000000;
const int ITERATIONS = 5;

template <typename Func>
double benchmark(Func&& func, int iterations = ITERATIONS){
        for(int i = 0; i < 3; i++) func();
        std::vector<long long> times;
        for (int i = 0; i < iterations; i++){
                auto start = chrono::high_resolution_clock::now();
                func();
                auto end = chrono::high_resolution_clock::now();
                times.push_back(chrono::duration_cast<chrono::microseconds>(end-start).count());
        }

        long long sum = accumulate(times.begin(), times.end(), 0LL);
        return static_cast<double>(sum) / times.size() / 1000.0;
}

// Заполнение вектора без предварительного заполнения памяти
void test_without_reserve(){
        vector<int> vec;
        volatile size_t sink = 0; // volatile - блокирует удаление переменной
        for(size_t i = 0; i < SIZE; i++){
                vec.push_back(i);
                sink += vec.back();
        }
}

// Заполнение вектора с предварительным выделением памяти
void test_with_reserve(){
        vector<int> vec;
        vec.reserve(SIZE);
        volatile size_t sink = 0;
        for(size_t i = 0; i < SIZE; i++){
                vec.push_back(i);
                sink += vec.back();
        }
}

int main(){
        setlocale(LC_ALL, "ru");
        cout << "Размер: " << SIZE << " Количество итераций: " << ITERATIONS << endl;
        double t1 = benchmark(test_without_reserve);
        double t2 = benchmark(test_with_reserve);
        cout << "Без reserve: " << t1 << "мс." << endl;
        cout << "С reserve: " << t2 << "мс." << endl;
}