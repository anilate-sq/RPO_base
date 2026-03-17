#include <iostream>

using namespace std;

class Counter{
        public:
                Counter(){
                        count++;
                }

                // Создаем static-метод
                static int getCount(){
                        return count;
                }


        private:
                static int count;
};

int Counter::count = 0; // Инициализация count

int main(){
        Counter a;
        Counter b;
        Counter c;

        cout << Counter::getCount();

        Counter d;
        Counter e;
        Counter f;
        
        cout << Counter::getCount();
}