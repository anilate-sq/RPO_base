#include <iostream>

using namespace std;

/*
Синтаксис:
class имя_класса{
// Поля
// Методы
// P.s в целом описывается вся логика
}
*/

// Создаем класс "Банковский аккаунт"
class Account{
    public:
        int balance;

        void deposit(int amount){
            balance += amount;
        }

        void withdraw(int amount){
            balance -= amount;
        }
};

int main(){
    // Реализация класса
    Account acc;
    acc.balance = 1000;

    acc.deposit(100);
    acc.withdraw(800);

    cout << "Баланс: " << acc.balance;
}