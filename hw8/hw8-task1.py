'''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''


class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def transformation(cls, day_month_year):
        my_date = []
        for i in day_month_year.split():
            if i != '-':
                my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(data, month, year):
        if 1 <= data <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2020:
                    return 'Дата корректна'
                else:
                    return 'Год указан неправильно'
            else:
                return 'Месяц указан неправильно'
        else:
            return 'Дата указана неправильно'


today = Data('06 - 05 - 2020')
print(today.transformation('06 - 05 - 2020'))
print(Data.transformation('06 - 05 - 2020'))
print(today.valid(6, 5, 2020))
print(Data.valid(6, 5, 2020))
print(today.valid(6, 5, 2021))
print(Data.valid(6, 5, 2021))
