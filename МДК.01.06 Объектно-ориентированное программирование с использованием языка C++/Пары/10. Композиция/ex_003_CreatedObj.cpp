#include <iostream>

using namespace std;

class Engine{
        public:
                Engine(int p, string t){
                        power = p;
                        type = t;
                        cout << "Двигатель создан" << endl;
                }

                ~Engine(){
                        cout << "Двигатель уничтожен" << endl;
                }

                void start(){
                        cout << "Двигатель запущен" << endl;
                }

                int get_power(){ return power; }
                string get_type(){ return type; }

        private:
                int power;
                string type;
};

class Car{
        public:
                // Копирование передаваемого двигателя 
                Car(string b, int y, Engine eng) : engine(eng) 
                {
                        brand = b;
                        year = y;
                        cout << "Машина готова!" << endl;
                }

                ~Car(){
                        cout << "Машина" << endl;
                }

                void drive(){
                        cout << brand << "газует!";
                        engine.start();
                }

                string get_brand() { return brand; }
                int get_year() { return year; }
                Engine get_engine() { return engine; }

        private:
                string brand;
                int year;
                Engine engine; // Композиция
};

int main(){
        setlocale(LC_ALL, "ru");
        Engine my_eng(200, "бензиновый");
        Car lastochka("Toyota", 2020, my_eng); // Используем цельный объект в качестве аттрибута
        cout << "Газ";
        lastochka.drive();

        // Композиция
        cout << "Мощность: " << my_eng.get_power() << endl;
        cout << "Тип: " << my_eng.get_type() << endl;
}