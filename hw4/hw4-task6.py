# пункт а
from itertools import count
import time


for el in count(int(input('Введите стартовое число: '))):
    print(el)
    time.sleep(0.5)


# пункт б
from itertools import cycle
import time

my_list = [10, True, 'name', None]
for el in cycle(my_list):
    print(el)
    time.sleep(0.5)
