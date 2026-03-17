#include <iostream>

using namespace std;

class Student{
        public:
                static int count; // static-переменная
                Student(){
                        count++;
                }
};

int Student::count = 0; // Инициализация проводится вне класса

int main(){
        Student s1;
        cout << Student::count << endl;
        Student s2;
        cout << Student::count << endl;
        Student s3;

        // Просмотр данных объектов
        cout << Student::count << endl;
        cout << "Студент 1: " << s1.count << endl;
        cout << "Студент 2: " << s1.count << endl;
        cout << "Студент 3: " << s1.count << endl;

        s2.count = 15; // Меняю count у 2 объекта, но значение меняется у всех 3
        
        cout << Student::count << endl;
        cout << "Студент 1: " << s1.count << endl;
        cout << "Студент 2: " << s1.count << endl;
        cout << "Студент 3: " << s1.count << endl;
}