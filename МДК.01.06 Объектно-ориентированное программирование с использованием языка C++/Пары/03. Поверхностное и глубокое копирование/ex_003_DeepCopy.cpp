// ===================Глубокое копирование===================
#include <iostream>

using namespace std;

class Array{
public:
        Array(int size) : size(size){
                data = new int[size];
                cout << "Память выделена" << endl;
        }

        // Гуд: копирование
        Array(const Array& other) : size(other.size){
                data = new int[size]; 
                for(int i = 0; i < size; i++){
                        data[i] = other.data[i]; 
                }
                cout << "Выполнено глубокое копирование" << endl;
        }

        ~Array(){
                delete[] data;
                cout << "Память освобождена" << endl;
        }

        void set(int index, int value){
                if(index >= 0 && index < size){
                        data[index] = value;
                }
        }

        int get(int index){
                if(index >= 0 && index < size){
                        return data[index];
                }
                return -1;
        }

private:
        int* data;
        int size;
};

int main(){
        Array a1(5);
        a1.set(0, 100);
        Array a2 = a1; // Для a2 выделяется своя область памяти
        a2.set(0, 200); // Значение изменится в a2
        cout << "a[0] = " << a1.get(0) << endl; 
        cout << "a[1] = " << a2.get(0) << endl; 

}