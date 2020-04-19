def info(name, surname, year_of_birth, city, email, telephone):
    return (name, surname, year_of_birth, city, email, telephone)


print(info(name=str(input('Введите имя: ')), surname=str(input('Введите фамилию: ')),
           year_of_birth=int(input('Введите год рождения: ')), city=str(input('Введите город: ')),
           email=str(input('Введите почту: ')), telephone=int(input('Введите телефон: '))))
