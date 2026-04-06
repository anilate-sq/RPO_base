#include <iostream>

class Counter{
    public:
        Counter(int v) : value(v){};

        // Оператор декремента(префиксный)
        Counter& operator--(){
            value--; // Увеличиваем value на 1
            return *this;
        }

        // Оператор декремента(постфиксный)
        Counter& operator--(int){
            Counter temp = *this;
            value--;
            return temp;
        }
    private:
        int value;
};


int main(){
    Counter counter(10);
    int a = --counter; // a = 9, counter = 9;
    int a = counter--; // a = 9, counter = 8;
}