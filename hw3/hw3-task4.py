def my_func(x, y):
    res = 1
    i = 1

    while i <= abs(y):
        res *= 1 / x
        i += 1
    return res


x = int(input("Введите число: "))
y = int(input("Введите отрицательную степень: "))
result = my_func(x,y)
print("Результат возведения {0} в степень {1} = {2}".format(x, y, result))
