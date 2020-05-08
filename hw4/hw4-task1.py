from sys import argv

script_name, time, salary, bonus = argv
# time = 40
# salary = 5000
# bonus = 50000
time = int(time)
salary = int(salary)
bonus = int(bonus)


def wages():
    wage = time * salary + bonus
    return wage


print(wages())
