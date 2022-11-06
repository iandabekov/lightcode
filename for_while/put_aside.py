num1 = int(input('How much would you like to put aside? '))
count = 0
while True:
    contribution = int(input('Put in your fee: '))
    count += contribution
    if count >= num1:
        print(f'Поздравляю! Вы накопили {count} сомов!')
        break

