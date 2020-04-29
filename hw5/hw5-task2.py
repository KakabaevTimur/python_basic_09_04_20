'''
Создать текстовый файл (не программно), сохранить
в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
'''
with open('test2.txt', 'r', encoding ='UTF-8') as file:
    content = file.read()
    print(content)

with open('test2.txt', 'r', encoding ='UTF-8') as file:
    content = file.readlines()
    print(f'Кол-во строк в файле: {len(content)}')

words = 0
with open('test2.txt', 'r', encoding ='UTF-8') as file:
    for i in range(len(content)):
        for line in file:
            words = len(line.split())
            print(f'Кол-во слов в {i + 1} строке: {words}')
