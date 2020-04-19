def my_func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 >= arg2 and arg3 >= arg2:
        return arg1 + arg3
    elif arg2 >= arg1 and arg3 >= arg1:
        return arg3 + arg2


print(my_func(arg1=int(input('Введите первый аргумент: ')),
              arg2=int(input('Введите второй аргумент: ')), arg3=int(input('Введение третий аргумент: '))))
