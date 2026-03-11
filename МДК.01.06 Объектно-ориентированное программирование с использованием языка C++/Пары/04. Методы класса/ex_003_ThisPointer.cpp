#include <iostream>

using namespace std;

class Product{
public:
    // Конструктор для инициализации полей
    Product(string name, double price, int quantity){
        this->name = name; // Исполуем this
        this->price = price; // Исполуем this
        this->quantity = quantity; // Исполуем this
    }

    // Методы для возвращения *this для цепочки вызовов
    Product& setName(string name){
        this->name = name; // Исполуем this
        return *this; // Возвращаем текущий объект для цепочки вызовов
    }

    Product& setPrice(double price){
        if (price > 0){
            this->price = price; // Исполуем this
        }
        return *this; // Возвращаем текущий объект для цепочки вызовов
    }

    Product& setQuantity(int quantity){
        if (quantity >= 0){
            this->quantity = quantity; // Исполуем this
        }
        return *this; // Возвращаем текущий объект для цепочки вызовов
    }

    // Метод для отображения информации о продукте
    void displayInfo() const{
        cout << "Название: " << this->name << ", Цена: " << this->price << ", Количество: " << this->quantity << endl; // Исполуем this
    }

private:
    string name;  // Поле для хранения названия продукта
    double price; // Поле для хранения цены продукта
    int quantity; // Поле для хранения количества продукта
};

int main() {
    Product product("Ноутбук", 999.99, 10); // Создаем объект класса Product

    product.displayInfo(); // Отображаем информацию о продукте

    // Используем цепочку вызовов для изменения полей продукта
    product.setName("Игровой ноутбук").setPrice(1299.99).setQuantity(5);

    product.displayInfo(); // Отображаем обновленную информацию о продукте

    return 0;
}