with open('test5.txt', 'w', encoding='UTF-8') as file:
    numbers = input('Введите числа через пробел: \n')
    file.writelines(numbers)
    get_numbers = numbers.split()
    print(sum(map(int, get_numbers)))
