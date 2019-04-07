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
    def __init__(self, num, denom):
        reduct_num = math.gcd(num, denom)
        self.num = num // reduct_num
        self.denom = denom // reduct_num

    # Функция сокращения дроби.
    def reduction(self):
        reduct_num = math.gcd(self.num, self.denom)
        return (self.num // reduct_num, self.denom // reduct_num)

    # Перегрузка оператора сырой строки
    def __repr__(self):
        return '(Дробь {}/{})'.format(self.num, self.denom)

    # Перегрузка оператора вывода print
    def __str__(self):
        return '{}/{}'.format(self.num, self.denom)

    # Перегрузка оператора сложения
    def __add__(self, other):
        return Fraction((self.num * other.denom) + (self.denom * other.num),
                        self.denom * other.denom)

    # Перегрузка оператора вычитания
    def __sub__(self, other):
        return Fraction((self.num * other.denom) - (self.denom * other.num),
                        self.denom * other.denom)




frac1 = Fraction(4, 2)
# frac1 = fraction_reduction(frac1)
frac2 = Fraction(1, 3)
# frac2 = fraction_reduction(frac2)
print(f'{frac1} + {frac2} = {frac1 + frac2}')
