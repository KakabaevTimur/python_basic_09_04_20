from itertools import count
from math import factorial


def fibo_gen():
    for elem in count(1):
        yield factorial(elem)


i = 0
for el in fibo_gen():
    if i < 15:
        print(el)
        i += 1
    else:
        break
