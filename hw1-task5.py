print('Введите выручку фирмы: ')
gain = int(input())
print('Введите издержки фирмы: ')
costs = int(input())

if gain > costs:
    print(f'Фирма имеет прибыль. Рентабельность выручки составляет {gain / costs:.2f}')
    print('Введите кол-во сотрудников: ')
    workers = int(input())
    print(f'Прибыль в рассчёте на одного сотрудника составила: {gain / workers:.2f}')
elif gain == costs:
    print('Фирма работает в ноль')
else:
    print('Фирма работает в убыток')
