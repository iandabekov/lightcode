x = int(input("Введите координату х(просто цифру н-р: -5 или 5): "))
y = int(input("Введите координату y(просто цифру н-р: -5 или 5): "))
print('ваши координаты х = ', x,", ваши координаты y = ",y )

if x > 0 and y > 0:
    print('Ваша точка находится в первой четверти координатной плоскости.')
elif x < 0 and y > 0:
    print('Ваша точка находится во второй  четверти координатной плоскости.')
elif x < 0 and y < 0:
    print('Ваша точка находится в третьей четверти координатной плоскости.')
else:
    print('Ваша точка находится в четвертой четверти координатной плоскости.')
