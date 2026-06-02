#include <iostream>
#include <thread>
#include <mutex> // Синхронизация
#include <vector>
#include <chrono>
using namespace std;

int shared_counter = 0; // Общая переменная для всех потоков
mutex mtx; //Объект мьютекса

// Функция, увеличивающая счетчик в цикле
void increment_counter(int iteration, int thread_id){
        for(int i = 0; i < iteration; i++){
                lock_guard<mutex> lock(mtx);
                ++shared_counter;
        }
        cout << "[Поток: " << thread_id << "] Закончил. Локальный цикл завершен." << endl;
}

int main(){
        setlocale(LC_ALL, "ru");
        const int THREAD_COUNT = 5;
        const int ITERATIONS = 10000;
        vector<thread> workers;
        for(int i = 0; i < THREAD_COUNT; i++){
                workers.emplace_back(increment_counter, ITERATIONS, i);
        }
        cout << "Потоки работают" << endl;
        for(auto& t : workers){
                t.join();
        }
        int expected = THREAD_COUNT * ITERATIONS;
        cout << "Ожидаемый результат: " << expected << endl;
        cout << "Фактический результат: " << shared_counter << endl;
        if (shared_counter == expected){
                cout << "Мьютекс предатвратил гонку данных";
        } else{
                cout << "Обнаружена гонка данных";
        }
}