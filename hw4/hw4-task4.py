my_list =[1, 2, 3, 6, 6, 5, 4, 3, 4]
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(my_list)
print(my_new_list)
