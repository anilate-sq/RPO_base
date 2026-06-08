#include <iostream>
#include <thread> // Потоки
#include <atomic> // Атомарные операции
#include <vector>
#include <chrono>
#include <stdexcept>
using namespace std;

atomic<bool> stop_flag{false}; // Атомарный флаг управления жизненным циклом
atomic<int> completed_tasks{0};

// Фоновая задача, работающая в цикле до получения сингала остановки
void background_worker(int id){
    cout << "[workder " << id << "] приступил к работе" << endl;
    while(!stop_flag.load(memory_order_acquire)){ // Цикл работает пока флаг false; load() атомарно читает значение с барьером памяти
        this_thread::sleep_for(chrono::milliseconds(200));
        completed_tasks.fetch_add(1, memory_order_relaxed); // Атомарно увеличиваем счетчик задач 
    }
    cout << "[worker " << id << "] отдыхает. Выполнено задач: " << completed_tasks.load() << endl;
}

int main(){
    setlocale(LC_ALL, "ru");
    const int WORKER_COUNT{3}; // Количество фоновых потоков
    vector<thread> workers;
    try{
        for(int i = 0; i < WORKER_COUNT; ++i){
            workers.emplace_back(background_worker, i);
        }
        cout << "Пауза 2 секунды" << endl;
        this_thread::sleep_for(chrono::seconds(2));
        cout << "Остановим сигнал остановки" << endl;
        stop_flag.store(true, memory_order_release);
        cout << "Ожидаем корректного завершения работы всех потоков" << endl;
        for (auto& t : workers){
            if(t.joinable()){
                t.join();
            }
        }
        cout << "Программа работает отлично" << endl;
    } 
    catch(const exception& e){
        cerr << "Ошибка работы: " << e.what() << endl;
    }
}