'''
Реализовать проект расчета суммарного расхода ткани на  производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название.  К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто)  и рост (для костюма). Это могут быть обычные числа:
V и H,  соответственно.  Для определения расхода ткани по каждому типу одежды использовать  формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).  Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на  практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике  работу декоратора @property.
'''

from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    @abstractmethod
    def get_square_coat(self):
        pass

    @abstractmethod
    def get_square_costume(self):
        pass


class Clothes(MyAbstractClass):
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def get_square_coat(self):
        return self.size / 6.5 + 0.5

    def get_square_costume(self):
        return self.height * 2 + 0.3

    @property
    def get_full_square(self):
        return str(f'Общая площадь ткани {(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.square_coat = (self.size / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь на пальто {self.square_coat}'


class Costume(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.square_costume = (self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь на костюм {self.square_costume}'


coat = Coat(6.5, 4)
costume = Costume(3, 4)
print(coat)
print(costume)
print(coat.get_full_square)
