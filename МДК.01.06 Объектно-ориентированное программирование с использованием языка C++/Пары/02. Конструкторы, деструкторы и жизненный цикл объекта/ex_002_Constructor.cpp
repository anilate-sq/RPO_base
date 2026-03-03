#include <iostream>

using namespace std;

// Пример создания простого конструктора
class Phone{
       public:
              // Конструктор
              Phone(){
                     brand = "Unknow";
                     price = 0;
              }

       private:
              string brand;
              int price;
};

// Виды конструкторов:
// 1. Конструктор по умолчанию(без параметров)

class Student{
public:
       Student(){
              name = "Без имени";
              age = 0;
              cout << "Создан студент по умолчанию!" << endl;
       }

private:
       string name;
       int age;
};


// 2. Конструктор с параметрами

class StudentParams{
public:
       StudentParams(string n, int a){
              name = n;
              age = a;
              cout << "Создан студент: " << name << ", возраст: " << age  << endl;
       }

private:
       string name;
       int age;
};

// 3. Конструктор с параметрами по умолчанию
class StudentParamsDefault{
public:
       StudentParamsDefault(string n = "Неизвестно", int a = 0){
              name = n;
              age = a;
              cout << "Создан студент: " << name << ", возраст: " << age  << endl;
       }

private:
       string name;
       int age;
};

int main(){
       // Использование Student
       Student s1; // Вызывается конструктор по умолчанию
       StudentParams s2("Иван", 17); // Вызывается параметризированный конструктор
       StudentParamsDefault s3; // Вызываем конструкор с параметрами по умолчанию
       StudentParamsDefault s4("Анна");
       StudentParamsDefault s5("Гриша", 21);
}