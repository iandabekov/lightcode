import random
'''
stat = [0,0]

counter = 0
while counter < 1000:
    stat[random.randint(0, 1)] += 1
    counter += 1


print(stat)
'''
list1 = []
for i in range(1,1001):
    list1.append(random.randint(1,1000))

counter = 0
for i in list1:
    if i % 2 == 0:
        counter += 1

print(len(list1), counter)

percnt = 100 * (counter/len(list1))
print(percnt)