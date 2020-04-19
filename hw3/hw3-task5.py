def my_sum():
    sum_res = 0
    leaving = False
    while leaving == False:
        number = input('Введите числа или В(в) для выхода: ').split(' ')
        res = 0
        for el in range(len(number)):
            if number[el] == 'в' or number[el] == 'В':
                leaving = True
                break
            else:
                res += int(number[el])
        sum_res += res
        print(f'Текущая сумма {sum_res}')
    print(f'Окончательная сумма {sum_res}')


my_sum()
