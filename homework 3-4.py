def my_pow_fun(x, y):
    try:
        res = x ** y
    except TypeError:
        return "Ошибка, нужно число"
    return res

print(my_pow_fun('привет', -18))




