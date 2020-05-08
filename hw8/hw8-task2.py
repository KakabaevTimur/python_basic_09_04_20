'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.  Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем  нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
'''


class DivisionByNull:
    def __init__(self, dividend, divider):
        self.dividend = dividend
        self.divider = divider

    def division_by_null(self, dividend, divider):
        try:
            return dividend / divider
        except:
            return 'Деление на ноль невозможно'


div = DivisionByNull(100, 10)
print(div.division_by_null(100, 10))
print(div.division_by_null(10, 0))
