"""ЗАДАЧА 1"""
# # Дан файл с расписанием занятий на неделю. Помимо названия предмета
# # в нем также указано лекция это, или практическое занятие, или лабораторная работа.
# # В одной строке может быть указаны только один предмет с информацией о нем.
# # Посчитать, сколько за неделю проходит практических занятий, лекций и лабораторных работ.
# #    ПРИМЕР:
# file_name = '''
# Понедельник Физика (лекц.)
# Физика (лаб.)
# Алгебра (практ.)
# Вторник
# Геометрия (лекц.)
# Физика (практ.)
# Физика (лаб.)
# Физкультура (практ.)
# '''
#
# # filename - хранит в себе имя файла
lect, pract, lab = 0, 0, 0
with open('filename.txt', 'r', encoding='utf-8') as file:
    words_line = file.read().split()
    lect = words_line.count('(лекц.)')
    pract = words_line.count('(практ.)')
    lab = words_line.count('(лаб.)')

print(lect, pract, lab)
# # lect = ...
# # pract = ...
# lab = ...

"""ЗАДАЧА 2"""
# В одном файле в каждой строке записаны координаты пар точек.
# Каждая координата отделена от другой пробелом. Например, строка вида 3 6 -2 4 означает,
# что координаты первой точки (3;6), второй - (-2;4).
# Требуется рассчитать наибольшее и наименьшее расстояние между точками.


# filename - хранит в себе имя файла
def range(array):
    x1, y1, x2, y2 = [int(x) for x in array]
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

ranges = []
with open('filename.txt', 'r', encoding='utf-8') as file:
    sets_points = file.read().split('\n')
    for points in sets_points:
        ranges.append(range(points.split()))

min = min(ranges)
max = max(ranges)
print(f'min{min}'
      f'max{max}')

"""ЗАДАЧА 3"""
# Дан файл. Определите сколько в нем букв (латинского алфавита), слов, строк.

import re
letters, words, rows = 0, 0, 0

pattern_word = (r"[a-zA-Z]+")
pattern_letter = (r"[a-zA-Z]")
with open('filename.txt', 'r', encoding='utf-8') as file:
    for line in file:
        letters += len(re.findall(pattern_letter, line))
        words += len(re.findall(pattern_word, line))
        rows += 1


print(rows, words, letters)


"""ЗАДАЧА 4"""
# Дан файл содержащий произвольный текст.
# Необходимо проверить сколько раз в тексте повторяется введеное слово или фраза.
# Начальный код (нажмите для просмотра)

with open('filename', 'r', encoding='utf-8') as file:
    result = file.read().count(word)


"""ЗАДАЧА 6"""
# В файле содержится текстовая строка.
# Определить частоту повторяемости каждой буквы в тексте и вывести ее в файл.
# Учитывать только буква латиницы, остальные символы не считать.
# Заглавные и строчные буквы считать отдельно.
# filename - хранит в себе имя исходного файла
# outfilename - хранит в себе имя файла результата

import re
import pprint

dict_letters = {}
pattern_letter = (r"[a-zA-Z]")
with open('filename.txt', 'r', encoding='utf-8') as file:
    all_letters = re.findall(pattern_letter, file.read())
    for letter in all_letters:
        dict_letters[letter] = all_letters.count(letter)
out_file = open('out.txt', 'w', encoding='utf-8')
for key, values in dict_letters.items():
    out_file.write(f'{key} {values}\n')
out_file.close()
