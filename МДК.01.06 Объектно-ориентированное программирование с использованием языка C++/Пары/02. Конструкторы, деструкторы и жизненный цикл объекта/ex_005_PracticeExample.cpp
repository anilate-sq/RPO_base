#include <iostream>

using namespace std;

class Array{
public:
        Array(int size) : size(size){
                data = new int[size]; // Выделяем память
                cout << "Память выделена" << endl;
        }

        ~Array() {
                delete[] data; // Освобождение памяти
                cout << "Память освобождена" << endl;
        
        }

private:
        int* data;
        int size;
};

int main(){
        Array arr(10);
}