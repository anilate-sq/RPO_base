#include <iostream>

using namespace std;

/*
Модификаторы:
- public - полный доступ;
- private - без доступа;
- protected - в дальнейших занятиях.
*/

class Account{
    private:
        int balance;

    public:
        void deposit(int amount){
            if (amount > 0){
                balance += amount;
            }
        }

        void withdraw(int amount){
            if(amount <= balance){
                balance -= amount;
            }
        }

        int getBalance(){
            return balance;
        }
};

int main(){
    // Account acc1{1000, "username"}; // Нужен конструктор
    // acc1.balance += 1000; // Доступ запрещен
    
    Account acc1;

    cout << "Изначальный баланс: " << acc1.getBalance() << endl;
    acc1.deposit(500);
    cout << "Новый баланс: " << acc1.getBalance() << endl;
    acc1.deposit(200);
    cout << "Итоговый баланс: " << acc1.getBalance() << endl;
}