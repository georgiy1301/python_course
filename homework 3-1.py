def div(s_1, s_2):
    try:
        s_1, s_2 = int(s_1), int(s_2)
        div_num = s_1 / s_2
    except ValueError:
        return 'Не хватает числа'
    except ZeroDivisionError:
        return 'На 0 делить нельзя'
    return round(div_num, 4)

print(div(input('Введите первое число - '), input('Введите второе число - ')))