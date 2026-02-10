#include<iostream>
#include<windows.h> // Для PowerShell


using namespace std;

int add(int a, int b){      
	cout << "Нагадил в терминале ";
	return a + b;
}

int main(){
	SetConsoleOutputCP(65001); // Для PowerShell
	cout << add(4, 8);
}


