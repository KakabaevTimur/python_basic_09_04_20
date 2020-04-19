user_str = str(input('Введите строку: '))
words = []
num = 1
for item in range(user_str.count(' ') + 1):
    words = user_str.split()
    if len(str(words)) <= 10:
        print(f'{num} {words[item]}')
        num += 1
    else:
        print(f'{num} {words[item][0:10]}')
        num += 1
