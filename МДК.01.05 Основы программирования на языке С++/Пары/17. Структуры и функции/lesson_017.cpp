#include <iostream>
#include <vector>
using namespace std;

struct Student{
    string name;
    int age;
    double grade;
};

void constPrint(const Student& s) {
    // s.name = "Новое имя"; // Так делать нельзя
    cout << s.name << " " << s.age << " " << s.grade << endl;
}

void updateStudent(Student* s, string new_name) {
    s->age++;
    s->name = new_name;
}

Student createStudent(string name, int age, double grade) {
    Student new_student{ name, age, grade }; // Создаем студента
    return new_student;
}

int main()
{
    setlocale(LC_ALL, "ru");
    Student Vitalya{ "Виталик", 19, 4.3 };
    cout << "Изначальное имя: " << Vitalya.name << endl;
    updateStudent(&Vitalya, "Гришаня"); // Меняем имя и увеличиваем возраст
    cout << "Новое имя: " << Vitalya.name << endl;
    Student igor = createStudent("Игорь", 21, 3.9); // Создаем студента
    cout << "Новый пользователь: ";
    constPrint(igor);

    // Массивы
    Student group[3]{ {"Семен", 17, 3.2}, {"Стас", 23, 4.6},{"Витя", 21, 4.3} };
    cout << group[0].name << endl;

    // Векторы
    vector<Student> students;
    students.push_back({ "Ахнаф", 17, 4.1 });
    for (Student& s : students) {
        cout << s.name << " " << s.age << " " << s.grade << endl;
    }
}