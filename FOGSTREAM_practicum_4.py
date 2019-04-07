# Создать класс Fraction, который должен иметь два поля:
# числитель a и знаменатель b. Оба поля должны быть типа int.
# Конструктор класса должен принимать параметры a и b и присваивать их полям.
# Необходимо реализовать следующие операции:
#
# сравнение
# сложение
# вычитание
# умножение
# деление
# получение в виде строки
# Операции с дробями должны выполняться как с обычными числами,
# то есть если frac1 и frac2 - объекты класса Fraction, то сложение выполняется так:
#
# frac1 + frac2
# А сравнение так:
#
# frac1 == frac2
# frac1 > frac2
# frac1 <= frac2
# После создания и выполнения операций дробь должна быть сокращена,
# если это возможно. Например дробь 12/16 должны быть преобразована к 3/4.
import math


# Создаем класс косой дроби (со встроенным сокращением)
class Fraction:
    def __init__(self, a, b):
        reduct_a = math.gcd(a, b)
        self.a = a // reduct_a
        self.b = b // reduct_a

    # Перегрузка оператора сырой строки
    def __repr__(self):
        return '(Дробь {}/{})'.format(self.a, self.b)

    # Перегрузка оператора вывода print
    def __str__(self):
        return '{}/{}'.format(self.a, self.b)

    # Перегрузка оператора сложения
    def __add__(self, other):
        return Fraction((self.a * other.b) + (self.b * other.a),
                        self.b * other.b)

    # Перегрузка оператора вычитания
    def __sub__(self, other):
        return Fraction((self.a * other.b) - (self.b * other.a),
                        self.b * other.b)

    # Перегрузка оператора <
    def __lt__(self, other):
        if (self.a * other.b) < (self.b * other.a):
            return True
        elif (self.a * other.b) > (self.b * other.a):
            return False
        elif (self.a * other.b) == (self.b * other.a):
            return False

    # Перегрузка оператора <=
    def __le__(self, other):
        if (self.a * other.b) < (self.b * other.a):
            return True
        elif (self.a * other.b) > (self.b * other.a):
            return False
        elif (self.a * other.b) == (self.b * other.a):
            return True

    # Перегрузка оператора >
    def __gt__(self, other):
        if (self.a * other.b) > (self.b * other.a):
            return True
        elif (self.a * other.b) < (self.b * other.a):
            return False
        elif (self.a * other.b) == (self.b * other.a):
            return False

    # Перегрузка оператора >=
    def __ge__(self, other):
        if (self.a * other.b) > (self.b * other.a):
            return True
        elif (self.a * other.b) < (self.b * other.a):
            return False
        elif (self.a * other.b) == (self.b * other.a):
            return True

    # Перегрезка оператора умножения.
    def __mul__(self, other):
        return Fraction((self.a * other.a), (self.b * other.b))

    # Перегрезка оператора деления
    def __truediv__(self, other):
        return Fraction((self.a * other.b), (self.b * other.a))



frac1 = Fraction(1, 5)
# frac1 = fraction_reduction(frac1)
frac2 = Fraction(1, 5)
# frac2 = fraction_reduction(frac2)
print(f'{frac1} + {frac2} = {frac1 + frac2}')

print(f'{frac1} - {frac2} = {frac1 - frac2}')

print(f'{frac1} > {frac2} = {frac1 > frac2}')

print(f'{frac1} < {frac2} = {frac1 < frac2}')

print(f'{frac1} * {frac2} = {frac1 * frac2}')

print(f'{frac1} / {frac2} = {frac1 / frac2}')
