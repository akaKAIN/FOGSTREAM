# Создать абстрактный класс Figure с методами вычисления площади area() и периметра perimeter().
# Создать производные классы: Rectangle (прямоугольник), Circle (круг),
# Triangle (треугольник) со своими методами вычисления площади и периметра.
# Конструктор класса Rectangle принимает 2 параметра - длину и ширину;
# класса Circle - один параметр - радиус; класса Triangle - три параметра - стороны треугольника.
#
class Figure:
    def area(self):
        pass

    def perimeter(self):
        pass

class Triangle(Figure):
    pass

class Rectangle(Figure):
    pass

class Circle(Figure):
    pass