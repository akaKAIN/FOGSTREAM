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
i = 1
result = 0
while i < len(numbers)+1:
    if numbers[i] / numbers[i-1] > 0: # Рано или поздно выловишь что на ноль делить незя
        result = numbers[i] + numbers[i-1]
        break
    i += 1


# ------------------------------ Задача 10
result = max(numbers) + numbers.index(max(numbers))


# ------------------------------ Задача 11
result = [x for x in set(numbers)]


# ------------------------------ Задача 12
# Т.к. искомого number нет в списке (что противоречит условию),
# то блок "if" чуток громоздкий.
if number not in numbers:
    numbers.append(number)
    numbers.sort()
    result = numbers.index(number)
else:
    result = numbers.index(number) + 1
    numbers.insert(result, number)


# ------------------------------ Задача 13
grades = []
result = []

# создаем список с оценками студентов
for student in students:
    grades.append(student['grade'])

# Выбрасываем минимальную оценку.Теперь минимальныя=предпоследней.
grades.remove(min(grades))

# Добавление в пустой список имен, чьи оценки равны минимальным=предпосл.
for student in students:
    if student['grade'] == min(grades):
        result.append(student['name'])


# ------------------------------ Задача 14
result = [x for x in set(list_one) if x in list_two]
