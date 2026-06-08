#include <iostream>  
#include <thread>       // Многопоточность
#include <mutex>        // Мьютексы для защиты общих данных
#include <condition_variable> // Условные переменные для ожидания событий между потоками
#include <queue>        // Очередь (FIFO) для буферизации задач
#include <chrono>       
using namespace std;    

mutex mtx;              
condition_variable cv;  
queue<string> task_queue; 
bool production_done = false; 

// Функция производителя (Producer): генерирует задачи и кладёт их в очередь
void producer(int id, int count) {
    cout << "[Producer " << id << "] Запущен. Генерируем " << count << endl; 
    for (int i = 0; i < count; ++i) { 
        this_thread::sleep_for(chrono::milliseconds(100)); 
        string task = "Задача-" + to_string(id * 100 + i); 
        unique_lock<mutex> lock(mtx); 
        task_queue.push(task);        
        cout << "[Producer " << id << "] Добавлена: " << task << " (размер очереди: " << task_queue.size() << ")" << endl; 
        cv.notify_one();              
    }
    unique_lock<mutex> lock(mtx);     
    production_done = true;           
    cv.notify_all();                  // Уведомляем ВСЕ ожидающие потоки, что производство завершено (консьюмеры выйдут из цикла)
    cout << "[Producer " << id << "] Завершил производство." << endl; 
} 

// Функция потребителя (Consumer): берёт задачи из очереди и обрабатывает их
void consumer(int id) {
    cout << "[Consumer " << id << "] Запущен. Ожидаю задачи..." << endl;
    while (true) { 
        unique_lock<mutex> lock(mtx);
        // cv.wait блокирует поток и одновременно отпускает мьютекс, пока лямбда не вернёт true
        // Лямбда проверяет: есть ли задачи ИЛИ производство завершено (защита от ложных пробуждений)
        cv.wait(lock, [] { return !task_queue.empty() || production_done; });
        while (!task_queue.empty()) { 
            string task = move(task_queue.front()); // Забираем задачу из головы очереди (move избегает лишнего копирования строки)
            task_queue.pop();          
            cout << "[Consumer " << id << "] Обработка: " << task << "..." << endl; 
        } 
        if (production_done && task_queue.empty()) { 
            cout << "[Consumer " << id << "] Очередь пуста и производство завершено. Выход." << endl; 
            break; 
        } 
    } 
} 

int main() { 
    setlocale(LC_ALL, "Russian"); 
    thread prod(producer, 1, 5);    
    thread cons1(consumer, 1);      
    thread cons2(consumer, 2);      
    cout << "Потоки запущены." << endl; 
    prod.join();                    
    cons1.join();                   
    cons2.join();                   
}