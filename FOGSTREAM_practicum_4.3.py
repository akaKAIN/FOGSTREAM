# Создать класс Complex, который должен иметь два поля:действительная часть real и мнимая часть imag.
# Оба поля должны быть типа int. Конструктор класса должен принимать параметры real и imag и
# присваивать их соответствующим полям. Реализовать сложение, вычитание, умножение и деление комлексных чисел.
# Операции с комлексными числами должны выполняться как с обычными, то есть если compl1 и compl2 -
# объекты класса  Complex, то сложение выполняется так:
#
# compl1 + compl2
#
# Также следует реализовать метод для строкового представления объектов типа Complex для
# вывода на печать или непосредственного получения строкового значения в
# коде вызовом встроенной функции str(c).
#
#  Реализовать операции с компексными числами:
# - сложение +
# - вычитание +
# - умножение +
# - деление +
# - ВЫВОД (функция str(c)) +

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        sign = ''
        if self.imag > 0:
            sign = '+'
        return '({:.2f}{}{:.2f}j)'.format(
            round(self.real, 2), sign, round(self.imag, 2)
        )

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        x1, y1, x2, y2 = splitting_into_variables(self, other)
        real = (x1 * x2 - y1 * y2)
        imag = (x1 * y2 + x2 * y1)
        return Complex(real, imag)

    def __truediv__(self, other):
        x1, y1, x2, y2 = splitting_into_variables(self, other)
        real = (x1 * x2 + y1 * y2) / (x2 ** 2 + y2 ** 2)
        imag = (x2 * y1 - x1 * y2) / (x2 ** 2 + y2 ** 2)
        return Complex(real, imag)


def splitting_into_variables(self, other):
    x1 = self.real
    y1 = self.imag
    x2 = other.real
    y2 = other.imag
    return x1, y1, x2, y2



z1 = Complex(10, 2)
z2 = Complex(8, 32)
print(f"""
z1 = {z1}
z2 = {z2}""")
print(f'z1 + z2 = {z1 + z2}')
print(f'z1 - z2 = {z1 - z2}')
print(f'z1 * z2 = {z1 * z2}')
print(f'z1 / z2 = {z1 / z2}')
print(f"""
z1 = {z1}
z2 = {z2}""")