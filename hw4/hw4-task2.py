my_list = [1, 10, 2, 9, 15, 7]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num] > my_list[num - 1]]
print(my_list)
print(my_new_list)
