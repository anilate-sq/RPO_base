#include <iostream>
#include <thread> // Библиотека для работы с потоками
#include <vector> 
#include <chrono> // Библиотека для работы с временем и задержками
#include <string>

using namespace std;

// Функция для выполнения в отдельном потоке
void worker_task(int id, const string& task_name){
        cout << "[Поток: " << this_thread::get_id() << " ] Начало: " << task_name << endl;
        this_thread::sleep_for(chrono::milliseconds(300 + id * 100));
        cout << "[Поток: " << id << "] Завершение " << task_name << endl;
}

int main(){
        setlocale(LC_ALL, "ru");
        vector<thread> thread_pool;
        for(int i = 0; i < 4; i++){
                thread_pool.emplace_back(worker_task, i, "Задача-" + to_string(i));
        }
        for (auto& t : thread_pool){
                if (t.joinable()) t.join();
        }
        cout << "Все работает";
        
}