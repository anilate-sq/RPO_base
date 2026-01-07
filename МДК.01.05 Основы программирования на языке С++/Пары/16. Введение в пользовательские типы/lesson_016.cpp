#include <iostream>

using namespace std;

// Структура
struct Student {
	string name; // Имя студента
	int age; // Возраст студента
	double grade; // Средний балл
};

/// <summary>
/// Пример без использования ссылок
/// </summary>
void showStudent(string name, int age, double grade) {
	cout << "Студент: " << name << " Возраст: " << age << " Ср. балл: " << grade;
}

/// <summary>
/// Пример с использованием ссылки
/// </summary>
/// <param name="s">ссылка на экземляр Student</param>
void showStudent_link(Student& s) {
	cout << "Студент: " << s.name << " Возраст: " << s.age << " Ср. балл: " << s.grade;
}

int main()
{
	setlocale(LC_ALL, "ru");
	
	// Способы объявления и инициализации структуры:
	// Способ 1.
	Student s1; // Объявляем структуру
	s1.name = "Сергей"; // Инициализируем аттрибут 1
	s1.age = 17; // Инициализируем аттрибут 2
	s1.grade = 3.8; // Инициализируем аттрибут 3
	
	// Способ 2.
	Student s2 = { "Виталий", 23, 4.7 }; // Старый способ объявления и инициализации

	// Способ 3.
	Student s3{"Гришаня", 18, 2.8 }; // Обновленный способ обновления и инициализации

	showStudent(s1.name, s1.age, s1.grade); // Вызов безссылочной функции
	cout << "\n";
	showStudent_link(s2); // Вызов функции с ссылкой
}
