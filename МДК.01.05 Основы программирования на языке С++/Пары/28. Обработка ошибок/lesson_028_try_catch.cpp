#include <iostream>
#include <stdexcept>
#include <fstream>

using namespace std;

// Проверка на наличие файла
bool readFile(const string& name){
    ifstream file(name);
    if(!file){
        throw runtime_error("Не удалось открыть файл");
    }
}

int main(){
    // Синтаксис
    /*
    try{
        код, который нужно обработать
    }
    catch(тип_ошибки e){
        обработка
    }
    */

    // Генерация исключения
    // trow тип_ошибки()

    // Пример: обработка файла
    try{
        readFile("data.txt");
    }
    catch(const exception& e){
        cout << "Ошибка: " << e.what();  
    }
}