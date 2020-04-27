'''
Создать текстовый файл (не программно), построчно записать
фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней
величины дохода сотрудников.
'''
summary = 0
number_of_workers = 0
workers = []
with open('test3.txt', 'r', encoding = ' UTF-8') as file:
    for line in file:
        marks = line.split(':')
        if int(marks[1]) < 20000:
            workers.append(marks[0])
        summary += int(marks[1])
        number_of_workers += 1
avg_sum = summary / number_of_workers
print(f'Сотрудники: {workers}')
print(f'Средняя величина дохода: {avg_sum}')
