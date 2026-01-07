#include <iostream>
#define ADD(a, b) ((a) + (b)) // Создаем макрос
using namespace std;

template <typename T>
T print_type(T t) {
	return t;
}

template <typename K, typename V>
void get(K k, V v) {
	cout << "Key: " << k << "Value: " << v << endl;
}

// Пример использование inline
inline void print() {
	cout << "Какое-то сообщение";
}

// Пример использования inline
inline int sum(int a = 2, int b = 4) {
	return a + b;
}

int main()
{
	setlocale(LC_ALL, "ru");

	// Макрос - текстовая вставка, выполняемая для компиляции
	
	print();
	cout << sum();
	cout << ADD(2, 3); // a + b
	cout << ADD(2, 3) * 2; // a + b * 2, а надо (a + b) * 2

	// Демонстрация работы шаблона
	cout << print_type(21) << " - это число";
	cout << print_type(21.4) << " - это дробь";
	cout << print_type("Text") << " - это строка";
	cout << print_type(true) << " - это логическое значение";
	get("Возраст", 21);


	// Бонус: Тернарный оператор
	int a = 10, int b = 12;
	bool check = a > b ? true : false;
	int check_int = a > b ? a : b;
	int result = a > b ? a > 0 ? a : -a : b > 0 ? b : -b; // Тяжело
	
	// Переписываем пример с 48 строчки
	if (a > b) {
		if (a > 0) {
			cout << a;
		}
		else {
			cout << -a;
		}
	}

	else {
		if (b > 0) {
			cout << b;
		}

		else {
			cout << -b;
		}
	}

	int ball;
	cin >> ball;
	char score = ball > 80 && ball < 100 ? 'A' 
		: ball < 80 && ball > 60 ? 'B' 
		: ball < 60 && ball > 40 ? 'C'
		: ball < 40 ? 'D' : 'N';

	// Описание примера с 72 по 75 строчки:
	if (ball > 80 && ball < 100) {
		cout << 'A';
	}

	else {
		if (ball < 80 && ball > 60) {
			cout << 'B';
		}

		else {
			if (ball < 60 && ball > 40) {
				cout << 'C';
			}

			else {
				if (ball < 40) {
					cout << 'D';
				}
				
				else {
					cout << 'N';
				}
			}
		}
	}


}

