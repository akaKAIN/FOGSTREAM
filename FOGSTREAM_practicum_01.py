#----------- Задание №1
result = '{:02}:{:02}'.format((moment // 60) % 24, moment % 60)


#----------- Задание №2
result = int((108 + (speed * hours) % 108) % 108)


#----------- Задание №3
# Расчет времени между уроками.
restTime = sum([5 if x % 2 == 0 else 15 for x in range(number-1)])
# Общее кол-во минут, к концу урока n
overMinut = restTime + (number*45)
result = '{:02}:{:02}'.format(9 + (overMinut // 60), overMinut % 60)


#----------- Задание №4
result = int((deposit_rubles * 100 + deposit_pennies) * (1 + percent / 100)) // 100

#----------- Задание №5
result = (60 * hours + minutes + seconds / 60) / 2