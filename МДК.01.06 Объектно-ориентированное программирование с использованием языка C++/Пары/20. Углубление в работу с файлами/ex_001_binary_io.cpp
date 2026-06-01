#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip> // Манипуляторы форматирования вывода
#include <stdexcept> // Для создания стандартных исключений
using namespace std;

#pragma pack(push, 1)
struct Student{
    char name[64];
    int age;
    double gpa;
};
#pragma pack(pop)

void save_students_binary(const string& filename, const vector<Student>& students){
    ofstream file(filename, ios::binary | ios::trunc); // Открывае поток для бинарной записи, режим trunc очищает файл, если он уже существует
    if(!file.is_open()) throw runtime_error("Не удалось открыть файл " + filename + " и записать в него информацию");
    size_t count = students.size();
    file.write(reinterpret_cast<const char*>(&count), sizeof(size_t)); // Записали размер вектора как сырые байты
    for (const auto& s : students){
        file.write(reinterpret_cast<const char*>(&s), sizeof(Student)); // Записали сырые байты структуры Student напрямую в файловый поток
    }
    if (file.fail()) throw runtime_error("Ошибка записи данных");
    file.close();
}

vector<Student> load_students_binary(const string& filename){
    ifstream file(filename, ios::binary); // Поток для чтения в бинарном режиме
    if(!file.is_open()) throw runtime_error("Файл не найден");
    vector<Student> students;
    size_t count = 0;
    file.read(reinterpret_cast<char*>(&count), sizeof(size_t));
    if (file.fail()) throw runtime_error("Ошибка чтения заголовка или файл пустой");
    students.reserve(count); // Резервируем память в векторе до заполнения
    for(size_t i = 0; i < count; ++i){
        Student s;
        file.read(reinterpret_cast<char*>(&s), sizeof(Student));
        students.push_back(s);
    }
    if (file.fail() && !file.eof()) throw runtime_error("Файл поврежден");
    file.close();
    return students;
}

int main(){
    setlocale(LC_ALL, "ru");
    try {
        // Запись в файл 
        vector<Student> original = {
            {"Соловье Захар", 18, 4.9},
            {"Григорьев Никита", 17, 4.7},
            {"Соколинский Владимир", 17, 4.8}
        };
        save_students_binary("students.dat", original);
        cout << "Успешно сохранено " << original.size() << " записей" << endl;
        
        // Выгрузка из файла
        vector<Student> loaded = load_students_binary("students.dat");
        cout << "Успешно загружено" << endl;

        // Восстановление данных
        for(const auto& s : loaded){
            cout << "Имя: " << s.name << " | Возраст: " << s.age << " | СБ: " << fixed << setprecision(1) << s.gpa << endl;
        }
    }
    catch (const exception& e){
        cerr << "Ошибка: " << e.what() << endl;
        return 1;
    }
}