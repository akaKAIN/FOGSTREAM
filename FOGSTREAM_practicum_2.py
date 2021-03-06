# ------------------------------ Задача 1
result = len(words.split())


# ------------------------------ Задача 2
if len(words) % 2 == 0:
    border = int(len(words) / 2)
else:
    border = int((len(words) + 1) / 2)
result = words[border:] + words[:border]


# ------------------------------ Задача 3
if words.find('f') != words.rfind('f'):
    result = words.find('f') + words.rfind('f')
else:
    result = words.find('f')


# ------------------------------ Задача 4
result = words.replace('1', 'one')


# ------------------------------ Задача 5
# Т.к. (0 % 3) дает 0, то в проверку добавляем +1, чтобы не потерять words[0].
new_words = [words[x] for x in range(len(words)) if (x + 1) % 3 != 0]
result = ''.join(new_words)


# ------------------------------ Задача 6
words = len(set(words.replace(' ', '').lower()))
result = words == 26


# ------------------------------ Задача 7
# Поиск "хэштега" для универсальности :)
start_index = words.index('#')
# Т.к. в первом слове прописная буква, то счет ведем с 1.
result = 1
for simvol in range(start_index + 1, len(words)):
    if words[simvol].isupper():
        result += 1


# ------------------------------ Задача 8
result = [numbers[i] for i in range(1, len(numbers))
          if numbers[i-1] < numbers[i]]


# ------------------------------ Задача 9
i = 0
result = 0
while i < len(numbers)-2:
    if numbers[i] * numbers[i+1] > 0:
        result = numbers[i] + numbers[i + 1]
        break
    i += 1


# ------------------------------ Задача 10
result = max(numbers) + numbers.index(max(numbers))


# ------------------------------ Задача 11
numbers.sort()
result = [number for number in numbers if numbers.count(number) == 1]


# ------------------------------ Задача 12
result = 0
if number in numbers:
    result = numbers.index(number) + 1
    numbers.insert(result, number)
else:
    i = len(numbers)-1
    while True:
        i -= 1
        if numbers[i] < number:
            result = numbers.index(numbers[i]) + 1
            break


# ------------------------------ Задача 13
result = []
grades = []
# создаем список с оценками студентов
for student in students:
    grades.append(student['grade'])
grade_list = [x for x in set(grades)]
grade_list.sort()
# Добавление в пустой список имен, чьи оценки равны предпоследней в списке оценок.
for student in students:
    if student['grade'] == grade_list[1]:
        result.append(student['name'])


# ------------------------------ Задача 14
result = [x for x in set(list_one) if x in list_two]
