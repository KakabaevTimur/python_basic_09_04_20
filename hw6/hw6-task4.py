'''
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
'''


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn(self, direction):
        return f'{self.name} повернула' + direction

    def show_speed(self):
        return f'Текущая скорость {self.name} составляет {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочей машины {self.name} составляет {self.speed}')
        if self.speed > 60:
            return f'Скорость {self.name} превышена'
        else:
            return f'Скорость {self.name} не превышена'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочей машины {self.name} составляет {self.speed}')
        if self.speed > 40:
            return f'Скорость {self.name} превышена'
        else:
            return f'Скорость {self.name} не превышена'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} из полиции'
        else:
            return f'{self.name} не из полиции'


toyota = TownCar(70, 'White', 'Toyota', False)
lamborghini = SportCar(120, 'Yellow', 'Lamborghini', False)
jeep = WorkCar(30, 'Grey', 'Jeep', False)
ford = PoliceCar(90, 'Red', 'Ford', True)

print(ford.speed, ford.color, ford.name, ford.is_police)
print(ford.go(), ford.stop(), ford.turn(' налево'), ford.show_speed(), ford.police())
print(toyota.speed, toyota.color, toyota.name, toyota.is_police)
print(toyota.go(), toyota.stop(), toyota.turn(' направо'), toyota.show_speed())
