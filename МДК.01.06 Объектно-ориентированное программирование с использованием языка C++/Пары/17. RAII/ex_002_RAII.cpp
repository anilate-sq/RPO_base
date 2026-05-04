#include <iostream>

using namespace std;

void process_data(){
    int* data = new int[1000]; // Выделение
    if(true){
        return; // Без delete будет утечка памяти
    }
    delete[] data; // Освобождение памяти
}