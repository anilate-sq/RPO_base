// Стандартный пример процедурного подхода

#include <iostream>

using namespace std;

int balance = 1000; // Глобальная переменная

void deposit(int amount){
    balance += amount;
}

void withdraw(int amount){
    balance -= amount;
}

int main(){
    cout << "Изначальный баланс: " << balance << endl;
    deposit(500);
    cout << "После начисления: " << balance << endl;
    withdraw(200);
    cout << "После списывания: " << balance << endl;
}