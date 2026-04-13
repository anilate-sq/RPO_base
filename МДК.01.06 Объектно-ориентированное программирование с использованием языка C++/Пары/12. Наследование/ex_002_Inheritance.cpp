#include <iostream>
using namespace std;

class Animal{
protected:
    string name; // Кличка
    int age; // Возраст
    string species; // Разновидность

public:
    Animal(string n, int a, string sp){
        name = n;
        age = a;
        species = sp;
        cout << "Мы создали питомца" << endl;
    }

    ~Animal(){
        cout << "Питомца забрали" << endl;
    }

    void eat(){
        cout << name << " кушает" << endl;
    }

    void sleep(){
        cout << name << " спит" << endl;
    }

    void make_sound(){
        cout << name << " издает звук" << endl;
    }

    string get_name(){ return name; }
    int get_age() { return age; }
    string get_species() { return species; }
};

// Создание наследника "Пес"
class Dog : public Animal{
    
    public:
        Dog(string n, int a, string sp, string br, bool trained) : Animal(n, a, sp){
            breed = br;
            is_trained = trained;
            cout << "Создан мощный пес"
        } 

        ~Dog(){
            cout << "Мощный пес ушел гулять"
        }

        void run_to_stick(){
            cout << "Пес пошел за палкой" << endl;
            
            if(is_trained){
                cout << "Пес принес палку" << endl;
            }
            
            else{
                cout << "Пес написал на соседский куст" << endl;
            }

        void make_sound(){
            cout << name << " пес гавкнул" << endl;
            if(is_trained){
                cout << "Пес съел соседа" << endl;
            }
            
            else{
                cout << "Пес съел тебя" << endl;
            }
        }

        void show_info(){
            cout << "Собака: " << name << ", возраст: " << age << ", порода: " << breed << ", обучен: " << (is_trained ? "Дрессирован" : "Не дрессирован") << endl;
        }
    }
    private:
        string breed; // Порода
        bool is_trained; // Статус дрессировки    
};

// Создание наследника "Кошка"
class Cat : public Animal{

    public:
        Cat(string n, int a, string sp, string c, bool cast) : Animal(n, a, sp){
            color = c;
            is_castrated = cast;
            cout << "Взяли кошку";
        }

        ~Cat(){
            cout << "Кошка ушла в лес";
        }

        void meow(){
            cout << "Кошка мяукнула" << endl;
        }

        void purr(){
            cout << "Кошка мурчит" << endl;
        }

        void make_sound(){
            cout << name << " мяукает" << endl;
        }

        void show_info(){
            cout << "Кошка: " << name << ", возраст: " << age << ", цвет: " << color << ", кастрация: " << (is_castrated ? "Анлак" : "Не анлак") << endl;
        }

    private:
        string color;
        bool is_castrated;
};

int main(){
    setlocale(LC_ALL, "ru");

    Dog dog("Виталя", 3, "Пес", "Лабрадор", true);
    Cat dog("Мишаня", 2, "Кот", "Рыжий", true);

    cout << "Животные дают бассов" << endl;
    dog.make_sound();
    cat.make_sound();

    cout << "Наследованный контент" << endl;
    dog.eat();
    cat.sleep();

    cout << "Палки" << endl;
    dog.run_to_stick();

    cout << "Кошачьи мувы" << endl;
    cat.meow();
    cat.purr();

    cout << "Информация" << endl;
    cat.show_info();
    dog.show_info();
}