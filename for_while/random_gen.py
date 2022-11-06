import random

stat = [0,0]

counter = 0
while counter < 1000:
    stat[random.randint(0, 1)] += 1
    counter += 1


print(stat)