user_time = int(input('Введите ваше время в секундах: '))
hour = user_time // 3600
min = int((user_time % 3600)/60)
sec = user_time % 60

time = f'{hour:02}:{min:02}:{sec:02}'
print(time)