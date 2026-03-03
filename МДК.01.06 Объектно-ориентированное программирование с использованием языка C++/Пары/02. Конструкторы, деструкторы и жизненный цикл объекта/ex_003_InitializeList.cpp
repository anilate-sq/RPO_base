#include <iostream>

using namespace std;

// Список инициалазации - последовательность вызова свойств

class Student{
        public:
                // Использование списка инициализации является самым ПРАВИЛЬНЫМ подходом
                Student(string n, int a) : name(n), age(a){
                        cout << "Студент создан!" << endl;
                }
                // Большой плюс заключается в том, что список работает быстрее классического присваивания
        private:
                string name;
                int age;
        };
int main(){
        Student s1("Иван", 17);
        
}