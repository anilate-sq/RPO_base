#include <iostream>

using namespace std;

class Phone{
public:
    // Публичные методы для работы с телефоном
    void setModel(const string& model){
        this->model = model;
    }

    string getModel() const{
        return this->model;
    }

    void setPrice(double price){
        if(price > 0){
            this->price = price;
        } else{
            cout << "Цена должна быть больше 0";
        }
    }

    double getPrice() const{
        return this-> price;
    }

    void displayProductionInfo(){
        cout << "[Внутренняя информации: завод №" << factory_id << "]" << endl;
    }

    void displayInfo(){
        cout << "Телефон:\nМодель: " << this->model << "\nЦена: " << this->price << endl; 
        this->displayProductionInfo();
    }

private:
    string model; // Приватные данные - без изменения на прямую
    double price; // Приватные данные
    int factory_id = 7; // Приватная константа
};

int main(){
    Phone phone;
    phone.setModel("iphone 15");
    phone.setPrice(50000.99);

    cout << "Модель: " << phone.getModel() << endl;
    cout << "Цена: " << phone.getPrice() << endl;

    cout << "\n\n";
    phone.displayInfo();
}