#include <iostream>

using namespace std;

class Person{
        private:
                int age;

        public:
                void setAge(int age){
                        // Делаем проверку
                        if (age > 0 && age < 120){
                                this->age = age;
                        }
                }

                int getAge(){
                        return this->age;
                }
};

int main(){
        Person boby;
        boby.setAge(15);

        cout << "Боби сегодня исполнилось: " << boby.getAge() << " лет" << endl;
}