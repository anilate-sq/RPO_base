#include <iostream>
#include <fstream>

using namespace std;

int main(){
       // Файловые потоки
       ifstream fin("data.txt"); // Считывание данных из файлов
       ofstream fout("out.txt"); // Запись данных в файл
       fstream file("data.txt"); // Общий поток для чтения и записи

       // Проверка открытия файла
       if(!fin.is_open()){
              cout << "Файл не найден";
       }

       // Упрощенная версия
       if(!fin){
              cout << "Файл не найден";
       }
}