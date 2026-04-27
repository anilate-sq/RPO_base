#include <iostream>
#include <vector>

using namespace std;

class Shape {
    protected:
        string name; // Название фигуры

    public:
        // Конструктор
        Shape(string n) : name(n){}

        // Виртуальный деструктор - всегда прописываем в контексте работы с полиморфизмом!!!
        virtual ~Shape(){
            cout << "Фигура удалена: " << name << endl;
        }

        virtual double area(){
            return 2 * 2;
        }

        virtual void draw(){
            cout << "Создана новая фигура" << endl;
        }

        string get_name(){ return name; }
};

class Circle: public Shape{
    private:
        double radius; // Радиус
    public:
        Circle(string n, double r) : Shape(n), radius(r){
            cout << "Круг создан: " << name << " - " << radius << endl;
        }
        
        // Переопределение
        double area() override{
            return 3.14  * (radius * radius);
        }

        // Переопределение
        void draw() override{
            cout << "Созданем круг: " << name << endl;
        } 
    };

class Rectangle : public Shape{
    private:
        double width, height; // Высота и ширина
    
    public:
        Rectangle(string n, double w, double h) : Shape(n), width(w), height(h){
            cout << "Прямоугольник создан: " << name << "(" << w << "," << h << ")" << endl;
        }

        // Переопределение
        double area() override{
            return width * height;
        }
        
        // Переопределение
        void draw() override{
            cout << "Создаем прямоугольник: " << name << endl;
        }
};

int main(){
    setlocale(LC_ALL, "ru");
    cout << "Создание фигур: "<< endl;

    vector<Shape*> shapes;
    shapes.push_back(new Circle("Круг", 3.0));
    shapes.push_back(new Rectangle("Прямоугольник", 10.0, 4.0));
    shapes.push_back(new Circle("Фишка", 1.5));

    cout << "Отображение фигур:" << endl;

    for(Shape* s : shapes){
        s->draw();
    }
    
    cout << "Подсчет площадей: " << endl;
    double total_area = 0;
    for(Shape* s : shapes){
        double a = s->area();
        cout << s->get_name() << " площадь: " << a << endl;
        total_area += a;
    }
    cout << "Общая площадь: " << total_area << endl;

    cout << "Чистка памяти" << endl;

    for(Shape* s : shapes){
        delete s;
    }
}