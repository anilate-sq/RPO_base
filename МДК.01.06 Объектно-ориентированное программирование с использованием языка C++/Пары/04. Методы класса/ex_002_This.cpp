#include <iostream>

using namespace std;

class Student{
    public:
        // Метод для установки имени
        void setName(string name){
            this->name = name; // Исполуем this
        }

        // Метод для получения имени
        string getName(){
            return this->name; // Исполуем this
        }

        // Метод для установки возраста
        void setAge(int age){
            if(age > 0 && age < 800){
                this->age = age; // Исполуем this
            } else {
                cout << "Некорректный возраст!" << endl;
            }
        }

        // Метод для получения возраста
        int getAge(){
            return this->age; // Исполуем this
        }

        // Метод для отображения информации о студенте
        void displayInfo() const{
            cout << "Имя: " << this->name << ", Возраст: " << this->age << endl; // Исполуем this
        }

    private:
        string name; // Поле для хранения имени
        int age; // Поле для хранения возраста
};

int main() {
    Student student; // Создаем объект класса Student

    student.setName("Иван"); // Устанавливаем имя
    student.setAge(20); // Устанавливаем возраст

    student.displayInfo(); // Отображаем информацию о студенте

    Student anotherStudent; // Создаем другой объект класса Student

    anotherStudent.setName("Мария"); // Устанавливаем имя
    anotherStudent.setAge(22); // Устанавливаем возраст

    anotherStudent.displayInfo(); // Отображаем информацию о другом студенте

    return 0;
}
