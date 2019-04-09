# Создать класс Point3D, представляющий собой точку в трёхмерном пространстве
# с тремя полями x, y, z и методом distance(other), вычисляющим расстояние между двумя точками.
# Конструктор класса принимает координаты x, y, z.
# Метод distance должен выбрасывать исключение  ValueError, если в него передан параметр неверного типа.

class Point3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

#     def distance(self, other):
#         try:
#             raise ErrorCatcher('Ввот не тод')
#         except ErrorCatcher as e:
#             print(e.args)
#         # return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2 + (other.z - self.z) ** 2) ** 0.5
#
# class ErrorCatcher(ValueError):
#     def __init__(self, arg):
#         self.arg = arg


point1 = Point3D(1, 2, 3)

print(type(point1) == Point3D)