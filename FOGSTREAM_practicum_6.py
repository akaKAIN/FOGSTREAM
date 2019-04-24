# ЗАДАЧА №1
# Переменная local_datetime хранит объект datetime с учетом часового пояса.
# Необходзимо средствами стандартной библиотеки произвести комбинацию даты
# из переменной с временем равным 7 утра. Результатом будет новый объект
# типа datetime который необходимо поместить в переменную result

import datetime

new_time = datetime.time(7)
result = datetime.datetime.combine(
    local_datetime.date(),
    new_time,
    local_datetime.tzinfo
)

# еще можно заменить время:
# result = local_datetime.replace(hour=7, minute=0, second=0, microsecond=0)




# ЗАДАЧА №2
# Реализуйте функцию get_datetime(just_datetime), которая принимает один
# параметр типа datetime. Еслидата в объекте just_datetime равна текущей,
# то необходимо отнять от just_datetime дельту равную 1 д. 3ч. 15мин и
# вернуть полученное значение, иначе вернуть дату/время без изменений.
#
# Объект хранящийся в just_datetime не должен быть изменен!!!

import datetime

def get_datetime(just_datetime):
    if just_datetime.date() == datetime.datetime.today().date():
        return just_datetime - datetime.timedelta(days=1, hours=3, minutes=15)
    return just_datetime



# ЗАДАЧА №3

# Дана переменная just_datetime, которая хранит объект datetime c учетом
# часового пояса. Необходимо привести дату/время хранящуюся в
# just_datetime к времени по Москве.

import pytz

time_zone = pytz.timezone('Europe/Moscow')
result = just_datetime.astimezone(time_zone)




# ЗАДАЧА №4
# Дана переменная datetime_string, которая хранит строку с временем в
# формате HH:MM:SS DD-MM-YYYY. Необходимо преобразовать строку в объект
# datetime. Сформатировать данную дату в ISO формат (по умолчанию)
# и сохранить в переменную result.

from datetime import datetime

pattern = '%H:%M:%S %d-%m-%Y'
result = datetime.strptime(datetime_string, pattern).isoformat()




# ЗАДАЧА №5
# В переменной time_shift хранится целое число. Необходимо определить
# порядковый номер недели в году (ISO 8601), на дату со сдвигом от
# текущей на количество дней хранящееся в time_shift.

from datetime import datetime
from datetime import timedelta

result = datetime.isocalendar(datetime.now() + timedelta(days=time_shift))[1]



# ЗАДАЧА №6

from collections import Counter, OrderedDict, defaultdict

result = defaultdict(list)
for operation in history:
    date, oper_type = operation['access_date'], operation['access_type']
    result[date].append(oper_type)
for key, value in result.items():
    result[key] = dict(Counter(value))
result = OrderedDict(sorted(result.items(), key=lambda x: x[0]))