# Создать абстрактный класс Figure с методами вычисления площади area() и периметра perimeter().
# Создать производные классы: Rectangle (прямоугольник), Circle (круг),
# Triangle (треугольник) со своими методами вычисления площади и периметра.
# Конструктор класса Rectangle принимает 2 параметра - длину и ширину;
# класса Circle - один параметр - радиус; класса Triangle - три параметра - стороны треугольника.
#
import math


class Figure:
    def __init__(self, param1=None, param2=None, param3=None):
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3

    # Circle
    def area_circle(self):
        return math.pi * self.param1 ** 2

    def perimeter_circle(self):
        return 2 * math.pi * self.param1

    # Rectamgle
    def area_rectangle(self):
        return self.param1 * self.param2

    def perimeter_rectangle(self):
        return (self.param1 + self.param2) * 2

    # Triangle
    def area_triangle(self):
        a, b, c = self.param1, self.param2, self.param3
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5

    def perimeter_triangle(self):
        return self.param1 + self.param2 + self.param3


class Triangle(Figure):
    def __init__(self, param1, param2, param3):
        super().__init__()
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3

    def area(self):
        return Figure.area_triangle(self)

    def perimeter(self):
        return Figure.area_triangle(self)


class Rectangle(Figure):
    def __init__(self, param1, param2):
        super().__init__()
        self.param1 = param1
        self.param2 = param2

    def area(self):
        return Figure.area_rectangle(self)

    def perimeter(self):
        return Figure.perimeter_rectangle(self)


class Circle(Figure):
    def __init__(self, param1):
        super().__init__()
        self.param1 = param1

    def area(self):
        return Figure.area_circle(self)

    def perimeter(self):
        return Figure.perimeter_circle(self)


circle1 = Circle(10)
triangle1 = Triangle(2, 3, 4)
rectangle1 = Rectangle(2,3)
print(f"""
круг {10} S = {circle1.area()}, P = {circle1.perimeter()}
треугольник {1,2,3}  S = {triangle1.area()}, P = {triangle1.perimeter()}
прямоугольник {2,3}  S = {rectangle1.area()}, P = {rectangle1.perimeter()}
""")