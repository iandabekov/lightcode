import random

random_num = random.randint(0, 100)
count = 0
while count <= 10:
    answer = int(input('Какое число загадано? '))
    count += 1
    if answer == random_num:
        print(f'Все верно ответ - {random_num}')
        break
    elif answer > random_num:
        print('Меньше')
    elif answer < random_num:
        print('Больше')
    if count == 10:
        print(f'вы исчерпали все свои 10 попыток, загаданное число - {random_num}')

