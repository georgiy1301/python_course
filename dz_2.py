# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
number = int(input('Введите число: '))
CONST = 3600
hour = number // CONST
minute = (number -hour*3600)//60
second = (number -hour*3600)%60
time_1 = str(0)+':'+str(minute)+':'+str(second)
time_2 = str(hour)+':'+str(minute)+':'+str(second)

if hour < 1:
    print(time_1)
else:
    print(time_2)

print('Расчитано часы-минуты-секунды')

