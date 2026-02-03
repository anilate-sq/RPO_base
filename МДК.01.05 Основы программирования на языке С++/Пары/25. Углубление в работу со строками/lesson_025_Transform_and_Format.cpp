#include <iostream>
#include <sstream>

using namespace std;

int main(){

        // Форматирование строк и Преобразования
        
        // Поток для строчной записи
        stringstream ss;
        ss << "x=" << 10 << ", y=" << 20;
        string res = ss.str();
        cout << res;

        // Преобразования строк
        int x = stoi("123"); // Преобразование в int
        double d = stod("3.12"); // Преобразования в double
        string s = to_string(42); // Преобразования в строку
        cout << "int: " << x << "\ndouble: " << d << "\nstring: " + s << endl;
}
