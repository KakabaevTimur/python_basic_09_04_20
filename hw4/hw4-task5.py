from functools import reduce


def my_func(el_1, el_n):
    return el_1 * el_n


print(f'Все четные: {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат перемножения четных элементов: {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')
