goods = int(input('Введите кол-во товаров: '))
n = 1
my_dict = []
my_list = []
while n <= goods:
    my_dict = dict({'Название': input("Введите название: "), 'Цена': input("Введите цену: "),
                    'Количество': input('Введите количество: '), 'Ед.': input("Введите единицу измерения: ")})
    my_list.append((n, my_dict))
    n += 1
print(my_list)
