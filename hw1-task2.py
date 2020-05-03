print('Введите количество секунд для перевода: ')
number_of_seconds = int(input())
hours = number_of_seconds // 3600
minutes = (number_of_seconds // 60) % 60
seconds = number_of_seconds % 60
if hours < 10:
    hours = '0' + str(hours)
else:
    hours = str(hours)
if minutes < 10:
    minutes = '0' + str(minutes)
else:
    minutes = str(minutes)
if seconds < 10:
    seconds = '0' + str(seconds)
else:
    seconds = str(seconds)

time = f'Будет {hours} часов, {minutes} минут, {seconds} секунд'
print(time)