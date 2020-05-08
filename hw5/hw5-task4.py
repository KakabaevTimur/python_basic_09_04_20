'''
Создать (не программно) текстовый файл со следующим содержимым: One — 1, Two — 2, Three — 3, Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
'''
translator = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_list = []
with open('test4_input.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        marks = line.split('—')
        print(marks)
        if marks[0] in translator:
            word = translator[marks[0]]
            new_list.append(word + ':' + marks[1])
    print(new_list)

with open('test4_output.txt', 'w', encoding='UTF-8') as new_file:
    new_file.writelines(new_list)
