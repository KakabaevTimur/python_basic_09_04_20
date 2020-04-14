# Решение через список
seasons_list = ['winter', 'spring', 'summer', 'autumn']
month = int(input('Введите порядковый номер месяца: '))
if month == 1 or month == 2 or month == 12:
    print(seasons_list[0])
elif 3 <= month <= 5:
    print(seasons_list[1])
elif 6 <= month <= 8:
    print(seasons_list[2])
elif 9 <= month <= 11:
    print(seasons_list[3])
else:
    print('Такого месяца нет')

# Решение через словарь
seasons_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
month = int(input('Введите порядковый номер месяца: '))
if month == 1 or month == 2 or month == 12:
    print(seasons_dict.get(1))
elif 3 <= month <= 5:
    print(seasons_dict.get(2))
elif 6 <= month <= 8:
    print(seasons_dict.get(3))
elif 9 <= month <= 11:
    print(seasons_dict.get(4))
else:
    print('Такого месяца нет')
