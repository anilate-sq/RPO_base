#include <iostream>

using namespace std;

void getStr(const string& s){
        cout << "Строка = " + s << endl;
}

int main(){
        // Введение
        string  text{"Вводная информация"};
        cout << "Строка: " + text + "\nЕё длина: " << text.size() << endl;

        // Про копирование
        // Используем константные ссылки
        
        // Пример 1.
        const string *s = &text;
        
        // Пример 2.
        getStr(text);
        
}