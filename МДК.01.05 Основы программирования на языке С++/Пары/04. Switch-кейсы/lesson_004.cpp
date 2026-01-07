#include <iostream>
using std::cout;
using std::cin;


int main()
{
	/*
		Switch-кейсы - способ разветления алгоритма

        Запомнить:
        - default: вместо case _:
        - break; в завершении каждого;
	*/

    setlocale(LC_ALL, "ru");
    int day;
    cout << "Введите текущий день недели: ";
    cin >> day;

    switch (day) {

    case 1:
        cout << "Я понедельник";
        break;

    case 2:
        cout << "Я вторник";
        break;

    case 3:
        cout << "Я среда";
        break;

    case 4:
        cout << "Я четверг";
        break;

    case 5:
        cout << "Я пятница";
        break;

    case 6:
        cout << "Я суббота";
        break;

    case 7:
        cout << "Я воскресенье";
        break;

    default:
        cout << "Я хз кто я";
        break;
    }

}
