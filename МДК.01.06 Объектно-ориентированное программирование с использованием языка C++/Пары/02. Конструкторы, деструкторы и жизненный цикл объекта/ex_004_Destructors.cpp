#include <iostream>

using namespace std;

class Student{
public:
        Student(string n) : name(n){
                cout << name + " создан!" << endl;
        }

        ~Student(){
                cout << name + " уничтожен!" << endl;
        }

private:
        string name;
};

// Реализация
void function(){
        Student s1("Алексей"); // Создаем Алексея
        Student s2("Олеся"); // Создаем Олесю
} // Алексей и Олеся удаляться при завершении работы функции

int main(){
        function(); // Демонстрация работы
        
}
