#include <iostream>

using namespace std;

class Shape{
    public:
        Shape(){
            cout << "Фигура создана" << endl;
        }

        virtual double area(){
            return 0;
        }

        virtual ~Shape(){}
};

class Circle : public Shape{
    private:
        double radius;
    
    public:
        Circle(double r) : Shape(){
            radius = r;
            cout << "Окружность создана" << endl;
        }

        double area() override{
            return 3.14 * (radius * radius);
        }
};

class Rectangle : public Shape{
    private:
        double width, height;
    
    public:
        Rectangle(double w, double h) : Shape(){
            width = w;
            height = h;
            cout << "Прямоугольник создан" << endl;
        }

        double area() override{
            return width * height;
        }
};

int main(){
    Shape* s1 = new Circle(5);
    Shape* s2 = new Rectangle(4, 6);
    cout << "Площадь окружности: " << s1->area() << endl;
    cout << "Площадь прямоугольника: " << s2->area() << endl;

    delete s1;
    delete s2;
}