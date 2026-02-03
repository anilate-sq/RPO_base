#include <iostream>
#include <fstream>

using namespace std;

int main(){
        // Поток для чтения
        ofstream fout("data.txt"); // Считывание данных из файлов
        fout << "Здарова дурак\n";
        fout << 12 << " / " << 21; 
}