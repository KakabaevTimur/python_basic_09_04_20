print('Введите кол-во километров в первый день')
a = int(input())
print('Введите ожидаемый результат в километрах')
b = int(input())
day_result = 1
while a < b:
    a = a + 0.1 * a
    day_result += 1
print(f'Результат будет достигнут на {day_result} день')
