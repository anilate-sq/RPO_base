#include <iostream>
#include <vector>

using namespace std;

class Student{
        public:
                Student(string n, int a){
                        name = n;
                        age = a;
                        cout << "Студент создан" << endl; 
                }

                ~Student(){
                        cout << "Студент удален" << endl;
                }

                string get_name() { return name; }
                int get_age() { return age; }
        
        private:
                string name;
                int age;
};

class Group{

        public:
                Group(string gn){
                        group_name = gn;
                        cout << "Группа создана";
                }

                ~Group(){
                        cout << "Группа расформированна";
                }

                void add_student(Student * s){
                        students.push_back(s);
                        cout << "Студент: " << s->get_name() << "добавлен в группу" << endl; 
                }

                void show_students(){
                        for(int i = 0; i < students.size(); i++){
                                cout << i + 1 << ". " << students[i]->get_name() << endl;
                        }
                }

                // Количество студентов
                int get_students_count(){ return students.size(); }

        private: 
                string group_name;
                vector<Student*> students; // Указатель <- агрегация                
};


int main(){
        setlocale(LC_ALL, "ru");

        Student s1("Захар", 18);
        Student s2("Влад", 18);
        Student s3("Соня", 20);

        Group g1("9/2_РПО_24/1");  // Создаем группу
        // Добавляем студентов
        g1.add_student(&s1);
        g1.add_student(&s2);
        g1.add_student(&s3);

        g1.show_students();
}