#include <iostream>
#include <vector>
#include <memory>

using namespace std;

/// @brief Сотрудник
class Employee{
    protected:
        string name;
        double base_salary;
    public:
        Employee(string n, double bs) : name(n), base_salary(bs) {
            cout << "Работник создан " << name << endl;
        }

        // Деструктор
        virtual ~Employee(){
            cout << "Работник удален " << name << endl;
        }

        // Расчет зарплаты
        virtual double calculate_salary(){
            return base_salary ;
        }

        // Просмотр информации
        virtual void show_info(){
            cout << name << "Кэш: " << base_salary << "руб." << endl;
        }
};

/// @brief Разработчик 
class Developer : public Employee{
    private:
        string language;
        double project_bonus;
    public: Developer(string n, double bs, string lang, double bonus)
        : Employee(n, bs), language(lang), project_bonus(bonus){}

    double calculate_salary() override{
        return base_salary + project_bonus;
    }

    void show_info() override{
        cout << "Разработчик: " << name << "\nЯзык: " << language << "\nКэш: " << calculate_salary() << endl;
    }
};

class Manager : public Employee{
    private:
        int team_size;
        double management_bonus;
    public:
        Manager(string n, double bs, int team, double bonus)
            : Employee(n, bs), team_size(team), management_bonus(bonus) {}

        double calculate_salary() override{
            return base_salary + management_bonus + (team_size * 1000);
        }

        void show_info() override{
            cout << "Менеджер: " << name << "\nЧисленность команды: " << team_size << "\nКэш: "
                << calculate_salary() << endl; 
        }
};

class Intern : public Employee{
    public:
        Intern(string n, double bs) : Employee(n, bs) {}

        double calculate_salary() override{
            return base_salary * 0.5;
        }

        void show_info() override{
            cout << "Стажер: " << name << "\nКэш: " << calculate_salary() << endl; 
        }
};

int main(){
    setlocale(LC_ALL, "ru");

    cout << "Создание сотрудников: " << endl;

    vector<unique_ptr<Employee>> staff;
    staff.push_back(make_unique<Developer>("Алексей", 150000, "C++", 25000));
    staff.push_back(make_unique<Manager>("Ольга", 180000, 5, 40000));
    staff.push_back(make_unique<Intern>("Дима", 70000));

    cout << endl << "Информация о сотрудниках: " << endl;
    for(const auto& emp : staff){
        emp->show_info(); // Полиморфный вызов
    }
    cout << endl << "Зарплатный фонд: " << endl;
    double total_fond = 0;
    for(const auto& emp : staff){
        total_fond += emp->calculate_salary();
    }
    cout << "Общий фонд зарплат: " << total_fond << endl;
}