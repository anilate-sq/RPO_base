#include <iostream>
#include <vector>

using namespace std;


struct Student {
    string name;
    int age;
    string faculty;
    double grade;
};

void displayStudent() {

}

int main()
{
    setlocale(LC_ALL, "ru");
    double maxGrade = 0;
    Student* bestStudent = nullptr;
    vector<Student>list = {
        {"Виктор", 17, "Математика", 4.3},
        {"Анастасия", 19, "Химия", 3.3},
        {"Александр", 22, "Русский Язык", 5},
        {"Валера", 18, "Философия", 4.3},
        {"Никита", 21, "Информатика", 4.8},
        {"Кира", 18 , "ОБЖ", 4.5},
        {"Елизавета", 20, "Литература", 5}
    };
    
    for (Student& student : list) {
        cout << "Студент: " << student.name << "\n Факультет: " << student.faculty << "\n Возраст: " << student.age << " \n Средний балл: " << student.grade << endl;
        if (maxGrade < student.grade) {
            maxGrade = student.grade;
            bestStudent = &student;
        }
    }

    cout << "Лучший студент: " << bestStudent->name << " Его балл: " << bestStudent->grade;
   
}
