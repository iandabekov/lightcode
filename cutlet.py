k = int(input('Сколько вмещается котлет одновременно в вашу сковороду? '))
m = int(input('Какое время обжаривается каждая котлета(минуты)? '))
n = int(input("сколько всего котлет планируете пожарить? "))


if n % k > 0:
    answer = ((n // k) + 1) * m
    print('Наименьшее время которое вы потратите на жарку ', n, " котлет, это ", answer, ' минут')
elif n % k == 0:
    answer = (n / k) * m
    print('Наименьшее время которое вы потратите на жарку ', n, " котлет, это ", answer, ' минут')
