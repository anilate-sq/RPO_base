#include <iostream>
#include <vector>

using namespace std;

int main(){
    
    // Захват переменных
    int a = 10;
    int b = 12;
    int c = 21;

    auto f = [a](){
        cout << a << endl;
    };

    f();

    auto f_link = [&a](){
        a += 10;
    };

    f_link(); // Меняем значение a
    cout << "Новое значение a = " << a << endl;

    // Глобальный захват
    auto f_all = [=](){
        cout << "a = " << a << "\n" << "b = " << b << "\n" << "c = " << c << endl; 
    };

    f_all(); // Вывод всего

    // Глобальный ссылочный захват
    auto f_all_link = [&](){
        a += b;
        b += c;
        c += a;
        cout << "Новая a = " << a << endl; 
        cout << "Новая b = " << b << endl; 
        cout << "Новая c = " << c << endl; 
    };

    f_all_link(); // Просмотр изменений

    // Мутации(mutable)

    auto f_mutable = [a]() mutable{
        a++;
        cout << "Мутация a = " << a << endl;
    };

    f_mutable(); // будет изменяться копия a: a изменяется только внутри f_matable, а не глобально
    cout << "Стандартная a = " << a << endl;
}