#include <iostream>

using namespace std;

// В комментариях прописаны ошибки

int unusedFunction(int x){
    int unused_var = 12; // Неиспользуемая переменная
    return x;
}

int main(){
    setlocale(LC_ALL, "ru");
    int a; // Неинициализирована
    int b = 10;

    if (a > b){
        cout << "Замечательно";
    }

    unsigned int un_int = 10;
    int i = -1;

    // Сравниваем int и unsigned int
    if(i < un_int){
        cout << "Положительна против отрицательной";
    }

    double d = 3.12;
    int truncated = d; // Конвертация

    if(false)
        cout << "Привет";
        cout << "Всегда печатается"; // Вне условия

    int arr[3];
    cout << arr[5] << endl; // Несуществуйщий элемент

}