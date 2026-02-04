#include <iostream>
#include <stdexcept>
#include <fstream>

using namespace std;

// Проверка на наличие файла
bool readFile(const string& name){
    ifstream file(name);
    if(!file){
        return false;
    }
    return true;
}

int main(){
    // Обработка ошибок

    // Классический вариант: код возврата
    if (!readFile("data.txt")){
        cout << "Ошибка открытия файла" << endl;
    }
}
