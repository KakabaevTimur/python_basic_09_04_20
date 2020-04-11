print('Введите число: ')
n = abs(int(input()))
max_num = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max_num:
        max_num = n % 10
    elif n > 9:
        continue
    else:
        print('Максимальная цифра в числе', max_num)
        break
