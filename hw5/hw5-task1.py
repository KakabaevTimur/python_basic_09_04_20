'''
Создать программно файл в текстовом формате, записать
в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

with open('test.txt', 'w', encoding='UTF-8') as file:
    line = input('Введите строку: ')
    while line:
        file.writelines(line + '\n')
        line = input('Введите строку: ')
        if not line:
            break


with open("test.txt", 'r', encoding = 'UTF-8') as file:
    content = file.readlines()
    print(content)
