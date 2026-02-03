#include <iostream>
#include <fstream>

using namespace std;

int main(){
        // Поток для чтения
        ifstream fin("data.txt"); // Считывание данных из файлов
        int x;
        fin >> x; // Запись в переменную содержимого файла
        cout << x;

        string line;
        getline(fin, line); // Считывания текста
        cout << line;

        while(getline(fin, line)){
                cout << line << endl;
        }

}