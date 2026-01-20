#include <iostream>
#include <vector>

using std::cout; // 1
using namespace std; // 2

int add (int a, int b)
{
    return a + b;
};
// template <typename T>

int main(){
    setlocale(LC_ALL, " ");

    // typedef

    // Синтаксис: typedef  какой_тип_переименовываем название_нового_типа;

    typedef int Scope;
    Scope x = 5;
    cout << "Значение x: " << x << "\n";

    typedef int* IntPointer;
    IntPointer p = &x;
    cout << "Получаем значение x через указатель p: " << *p << "\n";

    // using

    // Синтаксис: using новое_имя = существующий_тип_данных;
    using balls = int;
    balls a = 12;

    cout << "Получаем значение a: " << a;

    // using Vec = vector<int>;
    // Vec v; // Тоже самое, что и std::vector<int>

    // Страшна вырубай: std::vector<std::pair<std::string, int>>
    // Переписываем 

    using Group = pair<string, int>; // Создаем группу
    using Groups = vector<Group>;

    // Создаем группы
    Groups list_groups = {
        {"РПО", 1},
        {"КГиД", 2}
    };

    // Работа с функциями 

    //typedef int (*Operation)(int, int); // С помощью typedef
    using Operation = int(*)(int, int); // С помощью using
    
    Operation op = add;
    cout << op(12, 3);
}