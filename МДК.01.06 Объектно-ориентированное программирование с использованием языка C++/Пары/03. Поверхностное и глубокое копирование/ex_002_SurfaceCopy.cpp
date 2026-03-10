// ===================Поверхностное копирование===================

#include <iostream>

using namespace std;

class Student{
        
public:
        Student(string n, int a) : name(n), age(a){}
        
        // Конструктор копирования(поверхностное копирование)
        Student(const Student& other){
                name = other.name;
                age = other.age;
        }

        void show_info(){
                cout << "Имя студента: " << name << endl; 
        }

private:
        string name;
        int age;
};

// Проблема поверхностного копирования
class Array{
public:
        Array(int size) : size(size){
                data = new int[size];
        }

        // Плохо: поверхностное копирование
        Array(const Array& other){
                data = other.data;
                size = other.size;
        }

        ~Array(){
                int* data;
                int size;
        }
private:
        int* data;
        int size;
};


int main(){
        // Реализация класса Student
        Student s1("Алексей", 10);
        Student s2 = s1; // Копирование объекта
        Student s3(s1); // Тоже копирование

        s1.show_info();
        s2.show_info();
        s3.show_info();

        // Проблема:
        Array a1(5);
        Array a2 = a1; // Оба объекта указывают на одну и ту же память

        /*
        Когда a1 и a2 уничтожается, delete[] вызовется дважда для одной памяти
        Ошибка: двойное высвобождение памяти
        */
}