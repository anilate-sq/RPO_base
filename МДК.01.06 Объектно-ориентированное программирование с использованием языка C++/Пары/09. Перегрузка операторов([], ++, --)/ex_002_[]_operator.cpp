#include <iostream>

using namespace std;

class Array{
    public:
        Array(){
           for(int i = 0; i < 10; i++){
                data[i] = 0;
           } 
        }
    
        // Создаем оператор
        int & operator[](int index){
            if (index < 0 || index > 9){
                cout << "Индекс вышел за пределы массива";
                exit(1); // Выход
            }
            return data[index];
        }
    
    private:
        int data[10];
};

int main(){
    Array arr;

    arr[7]; // 0
    arr[2] = 12 // Перезапись
}