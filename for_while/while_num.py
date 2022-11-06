sum_num = 0
count = 0
while sum_num < 1000:
    sum_num += count
    count = count + 1
    if sum_num <= 1000:
        print(sum_num)

while True:
    a = int(input('Enter number: '))
    if a > 100:
        print('You have entered number greater than 100')
        break
