#include <iostream>

using namespace std;

class BankAccount {
public:
    // Возникает путаница с именами переменных, что может привести к ошибкам
    void setBalanceWrong(double balance) {
        balance = balance; // Неправильное присваивание отрицательного баланса
    }

    // Правильный способ использования this для разрешения конфликта имен
    void setBalance(double balance) {
        if (balance >= 0) {
            this->balance = balance; // Правильное присваивание с использованием this
        } else {
            cout << "Баланс не может быть отрицательным!" << endl;
        }
    }

    void deposit(double amount) {
        if (amount > 0) {
            this->balance += amount; // Увеличиваем баланс на сумму депозита
        } else {
            cout << "Сумма депозита должна быть положительной!" << endl;
        }
    }

    void withdraw(double amount) {
        if (amount > 0 && amount <= this->balance) {
            this->balance -= amount; // Уменьшаем баланс на сумму снятия
        } else {
            cout << "Недостаточно средств или сумма снятия некорректна!" << endl;
        }
    }

    int getBalance() const {
        return this->balance; // Возвращаем текущий баланс
    }

    void displayBalance() const {
        cout << "Текущий баланс: " << this->balance << endl; // Отображаем текущий баланс
    }

private:
    double balance; // Поле для хранения баланса счета
};

int main() {
    BankAccount account; // Создаем объект класса BankAccount

    account.setBalance(1000); // Устанавливаем начальный баланс
    account.displayBalance(); // Отображаем текущий баланс

    account.deposit(500); // Депонируем деньги
    account.displayBalance(); // Отображаем обновленный баланс

    account.withdraw(200); // Снимаем деньги
    account.displayBalance(); // Отображаем обновленный баланс

    account.setBalanceWrong(-500); // Пытаемся установить отрицательный баланс (неправильный способ)
    account.displayBalance(); // Баланс не изменится из-за неправильного метода

    return 0;
}