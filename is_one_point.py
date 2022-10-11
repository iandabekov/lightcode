x1 = int(input("Введите координату х1(просто цифру н-р: -5 или 5): "))
y1 = int(input("Введите координату y1(просто цифру н-р: -5 или 5): "))

x2 = int(input("Введите координату х2(просто цифру н-р: -5 или 5): "))
y2 = int(input("Введите координату y2(просто цифру н-р: -5 или 5): "))


if x1 > 0 and x2 > 0 and y1 > 0 and y2 > 0:
    print('Да')
elif x1 < 0 and x2 < 0 and y1 > 0 and y2 > 0:
    print('Да')
elif x1 < 0 and x2 < 0 and y1 < 0 and y2 < 0:
    print('Да')
elif x1 > 0 and x2 > 0 and y1 < 0 and y2 < 0:
    print('Да')
else:
    print('Нет')
