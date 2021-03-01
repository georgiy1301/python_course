# 6. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
x = int(input('Введите начальное значение, в км: '))
y = int(input('Введите конечное значение, в км: '))
day = 1
while y - x > 0:
    x = x + (x * 0.1)
    day = day + 1
print('На', day, 'день спортсмен достигнет', y, 'км.')