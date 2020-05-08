'''
Создайте собственный класс-исключение, который должен проверять содержимое списка  на отсутствие элементов типа строка и
булево. Проверить работу исключения на реальном примере.  Необходимо запрашивать у пользователя данные и заполнять
список. Класс-исключение должен контролировать типы данных элементов списка.
'''


class OwnError:
    def __init__(self, my_list):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                value = int(input('Введите число: '))
                self.my_list.append(value)
                print(f'Текущий список {self.my_list}')
                print('Для прекращения ввода, введите строку или булево')
            except:
                print('Недопустимое значение, строка или булевое')
                choice = input(f'Ввести еще раз? Yes/No ')

                if choice == 'Yes' or choice == 'yes':
                    print(my_except.my_input())
                elif choice == 'No' or choice == 'no':
                    print(f'Вы вышли, ваш текущий список {self.my_list}')
                    break
                else:
                    print(f'Вы вышли, ваш текущий список {self.my_list}')
                    break


my_except = OwnError(1)
print(my_except.my_input())
