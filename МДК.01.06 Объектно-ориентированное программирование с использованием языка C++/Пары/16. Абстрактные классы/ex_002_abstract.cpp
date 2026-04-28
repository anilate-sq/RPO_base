#include <iostream>
using namespace std;

class ILogger{
    public:
        // Чисто виртуальная функция
        virtual void log(const string& message) = 0;
        virtual ~ILogger() = default; // Виртуальный деструктор
};