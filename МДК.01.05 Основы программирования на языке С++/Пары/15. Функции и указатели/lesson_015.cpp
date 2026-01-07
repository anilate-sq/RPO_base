#include <iostream>
using namespace std;

/// <summary>
/// Создание массива через указатель
/// </summary>
/// <param name="n">Количество элементов массива</param>
/// <returns></returns>
int* createArray(int n) {
	return new int[n];
}

/// <summary>
/// Пример как делать не надо
/// </summary>
/// <returns></returns>
int* createInt() {
	int x = 10;
	return &x; // x исчезнет после вызовы функции
}

/// <summary>
/// Занесение нескольких указателей в параметры
/// </summary>
/// <param name="a">Параметр 1</param>
/// <param name="b">Параметр 2</param>
void transform(int* a, int* b) {
	*a *= 2; // Возводим параметр a в квадрат
	*b *= 3; // Возводим параметр b в куб
}

/// <summary>
/// Создание указателя на функцию
/// </summary>
int (*function_ptr)(int, int) = add;

/// <summary>
/// Создание калькулятора с использованием параметризированных функций
/// </summary>
/// <param name="operation">Функция-операция</param>
/// <param name="x">число 1</param>
/// <param name="y">число 2</param>
/// <returns></returns>
int calc (int(*operation) (int, int), int x, int y){
	return operation(x, y);
}

/// <summary>
/// Функция сложения для калькулятора
/// </summary>
/// <param name="a">число 1</param>
/// <param name="b">число 2</param>
/// <returns>Сумма a и b</returns>
int add(int a, int b) {
	return a + b;
}

/// <summary>
/// Функция-операция умножения
/// </summary>
/// <param name="a">число 1</param>
/// <param name="b">число 2</param>
/// <returns>Перемножение a и b</returns>
int mul(int a, int b) {
	return a * b;
}

/// <summary>
/// Функция-операция деления
/// </summary>
/// <param name="a">число 1</param>
/// <param name="b">число 2</param>
/// <returns>Деление a на b</returns>
int dif(int a, int b) {
	return a / b;
}

/// <summary>
/// Функция-операция вычетания
/// </summary>
/// <param name="a">число 1</param>
/// <param name="b">число 2</param>
/// <returns>Разность a и b</returns>
int min(int a, int b) {
	return a - b;
}

int main()
{
	int sum = 0;
	int* arr = createArray(21);
	
	for (int i = 0; i < 21; i++) {
		cout << arr[i];
		/*sum += arr[i];
		arr[i] + 2;*/
	}

	int a_real = 2, b_real = 3;
	transform(&a_real, &b_real);

	cout << function_ptr(2, 3); // Реализация указателя на функцию

	// Практические примеры

	// Использование указателя на функцию
	cout << "Измененная переменная a: " << a_real << endl;
	cout << "Измененная переменная b: " << b_real << endl;

	// Вызов функций калькулятора
	cout << "Операция сложения: " << calc(add, 2, 3);
	cout << "Операция вычетания: " << calc(min, 3, 2);
	cout << "Операция умножения: " << calc(mul, 2, 3);
	cout << "Операция деления: " << calc(dif, 6, 3);

	delete[] arr;
}

// Перегрузка указателей
void print(int* arr, int n);
void print(double* arr, int n);
