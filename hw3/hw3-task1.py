def division(num_1, num_2):
    try:
        res = num_1 / num_2
        return res
    except ZeroDivisionError:
        return 'Ошибка, делитель равен нулю'


print(division(num_1=int(input('Введите делимое: ')), num_2=int(input('Введите делитель: '))))
