#include <iostream>
# include <cstring>

using namespace std;

class MyString{
public:
        // Конструктор по умолчанию
        MyString(){
                str = new char[1];
                str[0] = '\0';
                cout << "Конструктор по умолчанию" << endl;
        }

        // Конструктор с параметрами
        MyString(const char* s){
                str = new char[strlen(s) + 1];
                strcpy(str, s);
                cout << "Конструктор с параметрами: " << str << endl;
        }

        // Конструктор копирования
        MyString(const MyString& other){
                str = new char[strlen(other.str) + 1];
                strcpy(str, other.str);
                cout << "Конструктор копирования: " << str << endl;
        }

        // Оператор присваивания
        MyString& operator=(const MyString& other){
                if(this == &other)
                        return *this;
                
                delete[] str;
        }

        // Деструктор
        ~MyString(){
                cout << "Деструктор: " << str << endl;
        }

        void print(){
                cout << "Строка: " << str << endl;
        }

private:
        char* str;
};

int main(){
        MyString s1("Привет!");
        MyString s2(s1);        
        MyString s3 = s1;
        s1.print();
        s2.print();
        s3.print();
}