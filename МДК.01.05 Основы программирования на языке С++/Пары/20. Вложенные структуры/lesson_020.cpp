#include <iostream>
#include <vector>

using namespace std;

// Создаем структуры
struct Address{
    string city;
    string street;
    int house;
};

struct Student{
    string name;
    int age;
    Address address;
};

// Метод для получения информации, о конкретном студенте
void printStudent(const Student& s){
    cout << "Имя: " << s.name << " Возраст: " << s.age
    << "\nАдрес: " << s.address.city + " " << s.address.street + " " << s.address.house;
};

// Метод для вывода информации обо всех студентах
void printStudents(const vector<Student>& ss){
    for (const Student s : ss){

        cout << "Имя: " << s.name << " Возраст: " << s.age
        << "\nАдрес: " << s.address.city + " " << s.address.street + " " << s.address.house;
    }
};

int main(){
    setlocale(LC_ALL, " ");
    // Первый способ инициализации
    Student s1;
    s1.name = "Grisha";
    s1.age = 17;
    s1.address.city = "Irkutsk";
    s1.address.street = "Lenina";
    s1.address.house = 12;

    // Второй способ инициализации
    Student s2 = {
        "Igor",
        21,
        {"Irkutsk", "Petrova", 3}
    };
    
    printStudent(s2); // Выводим информацию о втором студенте

    // Создаем список студентов
    vector<Student> students_list;
    // Заполняем список студентов
    students_list.push_back(s1);
    students_list.push_back(s2);

    printStudents(students_list);
}