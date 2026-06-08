#include <iostream>
#include <thread>
#include <chrono>
#include <mutex>

using namespace std;

struct BankAccount{
    string owner;
    double balance;
    mutex mtx;
};

// Перевод денег между счетами
void transfer_money(BankAccount& from, BankAccount& to, double amount){
    cout << "[Перевод] " << amount << " руб. от " << from.owner << " к " << to.owner << endl;
    std::scoped_lock lock(from.mtx, to.mtx); // Конструктор, вызывающий std::lock()
    if (from.balance > amount){
        this_thread::sleep_for(chrono::milliseconds(50));
        from.balance -= amount;
        to.balance += amount;
        cout << "[Успех] перевод выполнен успешно. Баланс " << from.owner << ": " << from.balance << endl;
    } else{
        cout << "[Отказ] недостаточно средств у " << from.owner << ": " << from.balance << endl;
    }
}

int main(){
    setlocale(LC_ALL, "ru");
    BankAccount alice{"Алиса", 1000.0, {}};
    BankAccount nikolay{"Николай", 500.0, {}};
    cout << "Изначальные балансы: " << alice.owner << ": " << alice.balance << "\n" << nikolay.owner << ": " << nikolay.balance << endl;
    thread t1(transfer_money, ref(alice), ref(nikolay), 300.0);
    thread t2(transfer_money, ref(nikolay), ref(alice), 200.0);
    cout << "Выполняются переводы" << endl;
    t1.join();
    t2.join();
    cout << "Итоговые балансы: " << alice.owner << ": " << alice.balance << "\n" << nikolay.owner << ": " << nikolay.balance << endl;
}