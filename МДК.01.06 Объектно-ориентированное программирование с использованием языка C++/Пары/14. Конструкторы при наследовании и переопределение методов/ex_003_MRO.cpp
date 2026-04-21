#include <iostream>

using namespace std;

class Person{
    protected:
        string name;

    public:
        Person(string n){
            name = n;
            cout << "Человек создан" << endl;
        }

        virtual void info(){
            cout << "Имя: " << name << endl;
        }
};

class Employee : public Person {
    protected:
        int salary;

    public:
        Employee(string n, int s) : Person(n){
            salary = s;
            cout << "Сотрудник создан" << endl;
        }

        void info() override{
            cout << "Имя: " << name << ", Зарплата: " << salary << endl;
        }
};

class Manager : public Employee{
    private:
        string department;

    public:
        Manager(string n, int s, string d) : Employee(n, s){
            department = d;
            cout << "Менеджер создан" << endl;
        }

        void info() override{
            cout << "Менеджер: " << name << ", Зарплата: " << salary << ", Отдел: " << department << endl;

        }
};

int main(){
    Manager m("Виталик", 80000, "Testing");
    m.info();
}