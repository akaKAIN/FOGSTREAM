# Создать класс Point3D, представляющий собой точку в трёхмерном пространстве
# с тремя полями x, y, z и методом distance(other), вычисляющим расстояние между двумя точками.
# Конструктор класса принимает координаты x, y, z.
# Метод distance должен выбрасывать исключение  ValueError, если в него передан параметр неверного типа.

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance(self, other):
        if type(other) == Point3D:
            return ((
                other.x - self.x) ** 2 + (
                other.y - self.y) ** 2 + (
                other.z - self.z) ** 2) ** 0.5
        else:
            raise ValueError('Value-lue-lue')


point1 = Point3D(1, 2, 3)
print(point1.distance('23'))

print(type(point1) == Point3D)