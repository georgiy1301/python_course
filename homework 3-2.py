def information(**kwargs):
    return ' '.join(kwargs.values())

name = input('Введите имя - ')
surname = input('Введите фамилию - ')
birthday = input('Введите дату рождения - ')
city = input('Введите город проживания - ')
email = input('Введите адрес электронной почты - ')
phone = input('Введите телефон - ')

print(information(name=name, surname=surname, birthday=birthday, city=city, email=email, phone=phone))