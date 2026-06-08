#include <iostream> 
#include <thread>       // Потоки
#include <shared_mutex> // Мьютекс чтения/записи (C++17), позволяет множественное чтение
#include <mutex>        // Стандартный мьютекс (для сравнения и защиты вывода в консоль)
#include <vector>       
#include <chrono>       // Время
#include <random>   

using namespace std;   

shared_mutex config_mtx; 
string config_data = "v1.0"; 
mutex cout_mtx;           

// Функция читателя (Reader): читает данные, не блокируя других читателей
void reader(int id) { 
    while (true) { 
        this_thread::sleep_for(chrono::milliseconds(rand() % 100 + 50)); 
        shared_lock<shared_mutex> lock(config_mtx); 
        string local_copy = config_data; 
        lock.unlock();                   
        lock_guard<mutex> c_lock(cout_mtx);
        cout << "[Reader " << id << "] Прочитано: " << local_copy << endl; 
    } 
} 

// Функция писателя (Writer): модифицирует данные, блокируя и читателей, и других писателей
void writer(int id) { 
    for (int i = 0; i < 3; ++i) {
        this_thread::sleep_for(chrono::milliseconds(rand() % 200 + 100)); 
        string new_version = "v" + to_string(id) + "." + to_string(i); 
        unique_lock<shared_mutex> lock(config_mtx); 
        config_data = new_version;  
        lock_guard<mutex> c_lock(cout_mtx);
        cout << "[Writer " << id << "] ОБНОВЛЕНО на: " << config_data << endl; 
    } 
} 

int main() { 
    setlocale(LC_ALL, "Russian"); 
    srand(static_cast<unsigned>(time(nullptr))); 
    vector<thread> workers;      
    for (int i = 1; i <= 3; ++i) { workers.emplace_back(reader, i); } 
    for (int i = 1; i <= 2; ++i) { workers.emplace_back(writer, i); } 
    cout << "Потоки запущены. Наблюдаем за параллельным чтением и эксклюзивной записью" << endl; 

    this_thread::sleep_for(chrono::seconds(1));
    cout << "\nВремя вышло. Завершаем потоки (в реальном приложении используется atomic flag)" << endl;
} 