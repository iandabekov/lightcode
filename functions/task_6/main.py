def shift_list():
    n = ' '
    list1 = []
    while n != '':
        n = input('Вводите цифры и нажимайте enter, а затем когда закончите нажмите просто enter: ')
        if n != '':
            list1.append(int(n))

    print(list1)

    shift = int(input('Введите значение для сдвига элементов списка: '))
    if shift > 0:
        print(list1[shift:] + list1[:shift])
    elif shift < 0:
        print(list1[shift:] + list1[:shift])
    else:
        print('Писать здесь 0 не имеет смысла)')

shift_list()