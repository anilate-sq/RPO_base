#include <iostream>

using namespace std;

// Синтаксис: return_type operator <оператор> (параметры)

class Point{
        public:
                Point(int x, int y){
                        this->x = x;
                        this->y = y;
                }

                // Создаем перегрузку +
                Point operator+(const Point& other){
                        return Point(x + other.x, y + other.y);
                }

                // Создаем перегрузку -
                Point operator-(const Point& other){
                        return Point(x - other.x, y - other.y);
                }

                // Создаем перегрузку ==
                bool operator==(const Point& other){
                        return x == other.x && y == other.y;
                }

                // Вывод результата
                void display(){
                        cout << "("  <<  x <<  "," << y << ")" << endl;
                }
        private:
                int x, y;
};

int main(){
        Point point1(2, 3);
        Point point2(2, 3);

        Point point3 = point1 + point2;
        point3.display();

        Point point4 = point2 - point1;
        point4.display();

        if (point1 == point2){
                cout << "Координаты равны";
        }
        else{
                cout << "Координаты не равны";
        }
}