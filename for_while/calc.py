while True:
    try:
        a = int(input('Введите число а: '))
        b = int(input("Введите число б: "))
        operation = input('Введите знак операции "+", "-", "*", "/", или "0" для выхода из программы: ')

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
    except (ZeroDivisionError, ValueError, NameError) as e:
        print(e)


        