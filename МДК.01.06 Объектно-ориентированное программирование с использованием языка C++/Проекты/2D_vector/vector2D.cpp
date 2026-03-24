#include <vector2D.h>
#include <cmath>

// Конструкторы
Vector2D::Vector2D::Vector2D() : x(0), y(0) {}
Vector2D::Vector2D(double x, double y) : x(x), y(y){}

// Геттеры и сеттеры
double Vector2D::getX() const { return x; }
double Vector2D::getY() const { return y; }

void Vector2D::setX(double x) { this->x = x; }
void Vector2D::setX(double y) { this->y = y; }

// Длина вектора
double Vector2D::length() const {
        return std::sqrt(x*x + y*y);
}

Vector2D Vector2D::operator+(const Vector2D& other) const{
        return Vector2D(x + other.x, y + other.y);
}

Vector2D Vector2D::operator-(const Vector2D& other) const{
        return Vector2D(x - other.x, y - other.y);
}

Vector2D Vector2D::operator*(double scalar) const{
        return Vector2D(x * scalar, y * scalar);
}

bool Vector2D::operator==(const Vector2D& other) const{
        return x == other.x && y == other.y;
}

bool Vector2D::operator!=(const Vector2D& other) const{
        return !(*this == other);
}

Vector2D& Vector2D::operator=(const Vector2D& other){
        if(this != &other){
                x = other.x;
                y = other.y;
        }
        return *this;
}

std::ostream& operator<< (std::ostream& os, const Vector2D& vec){
        os << "(" << vec.x << "," << vec.y << ")" << std::endl;
        return os;
}