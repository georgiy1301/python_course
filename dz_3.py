# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn
number = int(input('Введите число: '))
x = str(number)
a = number
b = number * 11
c = number * 111
d = a + b + c
print(x, '+', x+x, '+', x+x+x, '=', d)
