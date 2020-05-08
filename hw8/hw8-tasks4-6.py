'''
4) Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.  А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.  В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

5)Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
на склад и передачу в определенное подразделение компании. Для хранения данных
о наименовании и количестве единиц оргтехники, а также других данных, можно использовать
любую подходящую структуру, например словарь.

6) Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных
на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
максимум возможностей, изученных на уроках по ООП.
'''


class StoreEquipment:
    def __init__(self, name, price, quantity, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.store = []
        self.store_full = []
        self.item = {'Наименование товара:': self.name, 'Цена товара:': self.price,
                     'Кол-во товара:': self.quantity}

    def record(self):
        try:
            new_item_name = input('Введите наименование товара: ')
            new_item_price = int(input('Введите цену товара: '))
            new_item_quantity = int(input('Введите кол-во товара: '))
            unique = {'Наименование товара: ': new_item_name, 'Цена товара: ': new_item_price,
                      'Кол-во товара: ': new_item_quantity}
            self.item.update(unique)
            self.store.append(self.item)
            print(f'Текущий список: {self.store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода нажмите В, для продолжения нажмите Enter')
        leaving = input()
        if leaving == 'В' or leaving == 'в':
            self.store_full.append(self.store)
            print(f'Весь склад: {self.store_full}')
            return f'Выход'
        else:
            return StoreEquipment.record(self)


class Printer(StoreEquipment):
    def to_print(self):
        return f'Для печати чего-либо'


class Scanner(StoreEquipment):
    def to_scan(self):
        return f'Для сканирования чего-либо'


class Xerox(StoreEquipment):
    def to_copy(self):
        return f'Для копирования чего-либо'


item1 = Printer('HP', 5000, 5)
item2 = Scanner('Canon', 3000, 3)
item3 = Xerox('Xerox', 2000, 1)
print(item1.record())
print(item2.record())
print(item3.record())
print(item1.to_print())
print(item2.to_scan())
print(item3.to_copy())
