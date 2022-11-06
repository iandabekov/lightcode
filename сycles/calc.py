while True:
    a = float(input('Введите число а: '))
    b = float(input("Введите число б: "))
    operation = input('Введите знак операции "+", "-", "*", "/", или "0" для выхода из программы: ')
    try:
        if operation == "0":
            break
        elif operation == '+':
            print(f'{a} + {b} = {a + b}')
        elif operation == '-':
            print(f'{a} - {b} = {a - b}')
        elif operation == '*':
            print(f'{a} * {b} = {a * b}')
        elif operation == '/':
            print(f'{a} / {b} = {a / b}')
        else:
            print('Неверная команда')
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
    

        