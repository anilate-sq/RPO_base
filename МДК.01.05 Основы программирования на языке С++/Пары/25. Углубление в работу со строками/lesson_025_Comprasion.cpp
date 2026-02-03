#include <iostream>


int main(){
        // Сравнение строк
        std::string a = "Вторник"; 
        std::string b = "Среда";

        // Сравнение 1
        if (a > b){
                std::cout << "В первом сравнении победила: " << a << std::endl;
        }

        else {
                std::cout << "В первом сравнении победила: " << b << std::endl;
        }

        // Сравнение 2:
        if (a < b){
                std::cout << "Во втором сравнении победила: " << b << std::endl;
        }

        else {
                std::cout << "Во втором сравнении победила: " << a << std::endl;
        }

        // Сравнение 3:
        if (a == b){
                std::cout << "a и b равны"<< std::endl;
        }

        else {
                std::cout << "a и b не равны"<< std::endl;
        }
}