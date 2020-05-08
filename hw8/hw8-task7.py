'''
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,  реализуйте перегрузку методов
сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
'''


class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.c = 'a + b * i'

    def __add__(self, other):
        return f'c = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'c = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'


c1 = ComplexNumber(1, 2)
c2 = ComplexNumber(2, 3)
print(c1.__add__(c2))
print(c1.__mul__(c2))
