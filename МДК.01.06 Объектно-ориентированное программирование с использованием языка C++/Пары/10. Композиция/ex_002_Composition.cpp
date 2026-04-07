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
                Car(string b, int y, int engine_p, string engine_t) : engine(engine_p, engine_t){
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

        Car lastochka("Toyota", 2020, 150, "Бензиновый");
        cout << "Газ";
        lastochka.drive();

        // Композиция
        Engine e = lastochka.get_engine();
        cout << "Мощность: " << e.get_power() << endl;
        cout << "Тип: " << e.get_type() << endl;
        
}