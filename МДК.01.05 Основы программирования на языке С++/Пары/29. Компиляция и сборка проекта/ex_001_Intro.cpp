#include<iostream>

using namespace std;

int add(int a, int b){
        
	cout << "Накодил в терминале";
	return a + b;

	
}

int main(){
	setlocale(LC_ALL, "ru");
	cout << add(4, 8);
}
