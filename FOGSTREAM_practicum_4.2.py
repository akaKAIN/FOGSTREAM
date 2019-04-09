# Создать класс Polynome, представляющий собой многочлен одной переменной.
# Конструктор класса должен принимать один параметр - список коэффициентов
# многочлена от младшего члена к старшему. Реализовать сложение, вычитание
# и умножение многочленов, а также метод calc(x), вычисляющий значение многочлена
# для заданной переменной x. Операции с многочленами должны выполняться как с
# обычными числами, то есть если poly1 и poly2 - объекты класса Polynome, то
# сложение выполняестся так:
#
# poly1 + poly2
# Обратите внимание на порядок коэффициентов в списке: от младшего члена к старшему.
# Принятая в математике форма записи многочленов - от старшего члена к младшему:
# 4x2−2x+1.
# Такой многочлен инициализируется вот таким списком коэффициентов:
# [1, -2, 4]
class Polynome:
    def __init__(self, list):
        self.var_list = ['', 'x'] + [
            'x' + str(i + 1) for i in range(1, len(list) - 1)]
        self.list = list
        self.dict = dict(zip(self.var_list, self.list))

    # Перегрузка оператора сырой строки.
    def __repr__(self):
        return '({}, : {})'.format(self.list, self.var_list)

    # Перегрузка оператора вывода print.
    # Ставить знаки между многочленами, согласно их полярности,
    # Многочлены, чей множитель равен 1, сокращает до переменной в степени n.
    def __str__(self):
        line_print = ''
        for key in self.var_list[::-1]:
            if self.dict[key] >= 0:
                line_print += '+'
            line_print += str(self.dict[key]) + key
        if line_print[0] == '+':
            return line_print[1:]
        return line_print

    def __add__(self, other):
        new_list = []
        check_list = list(set(self.var_list) | set(other.var_list))
        check_list.sort()
        for key in check_list:
            new_list.append(
                self.dict.setdefault(key, 0) + other.dict.setdefault(key, 0))
        return Polynome(new_list)

    def __sub__(self, other):
        new_list = []
        check_list = list(set(self.var_list) | set(other.var_list))
        check_list.sort()
        for key in check_list:
            new_list.append(
                self.dict.setdefault(key, 0) - other.dict.setdefault(key, 0))
        return Polynome(new_list)

    def __mul__(self, other):
        p = self.list
        q = other.list
        result = [sum(
            [p[i] * q[k - i] for i in range(
                max([0, k - len(q) + 1]), 1 + min([k, len(p) - 1])
            )])for k in range(len(p) + len(q) - 1)]
        return Polynome(result)

    def calc(self, x):
        result = 0
        for key, value in enumerate(self.list):
            result += value * x ** key
        return result



    # Перегрузка оператора сложения.




poly1 = Polynome([1, 2, 3])
poly2 = Polynome([10, 3, 1])

print(f"""\n-------------------------------
poly1   = {poly1.list}
var_list= {poly1.var_list}
print   = {poly1}\n------------------|{poly1 + poly2}""")
print(f"""
poly2   = {poly2.list}
var_list= {poly2.var_list}
print   = {poly2}\n------------------|{poly1 - poly2}
------------------------------------*|{poly1 * poly2}""")

print(poly1.calc(3))


