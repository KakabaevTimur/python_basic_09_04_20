item_count = int(input('Введите кол-во элементов: '))
my_list = []
i = 0
item = 0
while i < item_count:
    my_list.append(input('Введите следующее значение: '))
    i += 1

for el in range(int(len(my_list)/2)):
    my_list[item], my_list[item + 1] = my_list[item + 1], my_list[item]
    item += 2
print(my_list)
