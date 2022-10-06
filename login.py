login = 'johndoe@gmail.com'
password = '12345'

ask_login = input('Введите логин: ')
ask_password = input('Введите пароль: ')

if ask_login == login and ask_password == password:
    print(True)
else:
    print(False)
