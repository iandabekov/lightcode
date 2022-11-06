a = input('Enter some random number>  ')

a2 = list(a)

for i in range(0, len(a2)):
    a2[i] = int(a2[i])

print(max(a2))

