# Создать абстрактный класс Figure с методами вычисления площади area() и периметра perimeter().
# Создать производные классы: Rectangle (прямоугольник), Circle (круг),
# Triangle (треугольник) со своими методами вычисления площади и периметра.
# Конструктор класса Rectangle принимает 2 параметра - длину и ширину;
# класса Circle - один параметр - радиус; класса Triangle - три параметра - стороны треугольника.
#
import math

class Figure:
    def area_circle(self, r):
        return math.pi * r ** 2

    def perimeter_circle(self, r):
        return 2 * math.pi * r



class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c


class Rectangle(Figure):
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius