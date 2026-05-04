#include <iostream>
#include <fstream>
#include <mutex>
#include <thread>
#include <vector>

using namespace std;

mutex log_mutex;

void write_log(const string& worker_name, const string& message){
    ofstream log_file("app_log.txt", ios::app);
    if(!log_file.is_open()){
        cout << "Не удалось открыть файл" << endl;
        return;
    }

    lock_guard<mutex> lock(log_mutex);
    log_file << "\"" << worker_name << "\" " << message << endl; 
}

void worker_task(int id){
    string name = "Stuff-" + to_string(id);
    write_log(name, "Начал работу");
    this_thread::sleep_for(chrono::milliseconds(100)); // Пауза
    write_log(name, "Завершил работу");
}

int main(){
    setlocale(LC_ALL, "ru");

    vector<thread> workers;
    for(int i = 1; i <= 3; ++i){
        workers.emplace_back(worker_task, i);
    }

    for(auto& t : workers){
        t.join();
    }
}