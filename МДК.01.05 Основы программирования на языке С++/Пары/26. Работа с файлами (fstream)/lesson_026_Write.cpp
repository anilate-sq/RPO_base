#include <iostream>
#include <fstream>

using namespace std;

int main(){
        // Поток для записи
        ofstream fout("data.txt"); // Запись данных из файлов
        fout << "Здарова дурак\n";
        fout << 12 << " / " << 21; 
}