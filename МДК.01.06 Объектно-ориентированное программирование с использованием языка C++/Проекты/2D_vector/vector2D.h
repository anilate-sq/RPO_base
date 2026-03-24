#ifndef VECTOR2D_H
#define VECTOR2D_H

#include <iostream>

class Vector2D{
        public:
                // Конструктор по умолчанию
                Vector2D();
                // Параметризированный конструктор
                Vector2D(double x , double y);

                // Геттеры и сеттеры
                double getX() const;
                double getY() const;

                void setX(double x);
                void setY(double y);

                double length() const; // Длина вектора

                // Перегрузка операторов
                Vector2D operator+(const Vector2D& other) const;
                Vector2D operator-(const Vector2D& other) const;
                Vector2D operator*(double scalar) const;
                bool operator==(const Vector2D& other) const;
                bool operator!=(const Vector2D& other) const;
                Vector2D& operator=(const Vector2D& other);

                friend std::ostream& operator<<(std::ostream& os, const Vector2D& ver);
                
        private:
        double x, y; // Координаты
};

#endif