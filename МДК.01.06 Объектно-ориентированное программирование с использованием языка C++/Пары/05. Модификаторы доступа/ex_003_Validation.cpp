#include <iostream>

using namespace std;

class Car{
public:
    void setBrand(const string& brand){
        if(!brand.empty()){
            this->brand = brand;
        }
    }

    void setYear(int year){
        if (year >= 1884 && year <= 2026){
            this->year = year;
        } else{
            cout << "Ошибка: неверный год (" << year << ")" << endl;
        }
    }

    void setSpeed(int speed){
        if(speed >= 0 && speed <= 300){
            this->speed = speed;
        } else{
            cout << "Ошибка: неверная скорость (" << speed << ")" << endl;
        }
    }

    /// @brief Увеличение скорости
    /// @param delta 
    void accelerate(int delta){
        int new_speed = this->speed + delta;
        if (new_speed >= 0 && new_speed <= 300){
            this->speed = new_speed;
            cout << "Скорость: " << this->speed << " км/ч" << endl;
        } else {
            cout << "невозможно изменить скорость" << endl;
        }
    }

    /// @brief Замедление
    /// @param delta 
    void brake(int delta){
        this->accelerate(-delta);
    }

    string getBrand() const{
        return this->brand;
    }

    int getYear() const{
        return this->year;
    }

    int getSpeed() const{
        return this->speed;
    }

    void displayInfo() const{
        cout << "Автомобиль:\nМарка: " << this->brand << "\nГод: " << this->year << "\nСкорость: " << this->speed << endl; 
    }

private:
    string brand; // Приватно
    int year; // Приватно
    int speed; // Приватно
};

int main(){
    Car car;
    car.setBrand("Toyota Camry");
    car.setYear(2022);
    car.setSpeed(0);

    car.displayInfo();
    
    cout << "\nРазгон: " << endl;
    car.accelerate(60);
    car.accelerate(40);

    cout << "\nТорможение: " << endl;
    car.brake(30);
    
    cout << "\nПроверка валидации:" << endl;
    car.setYear(3000);
    car.setSpeed(-30);
    car.setSpeed(3000);
}