months_a = set(["Jan", "Feb", "March", "Apr", "May", "June"])
months_b = set(["July", "Aug", "Sep", "Oct", "Nov"])
#1
month_c = months_a | months_b
print(month_c)
#2
month_c.add('Dec')
print(month_c)
#3
for i in month_c:
    print(i)
#4
x = {1, 2, 3}
y = {4, 3, 6}

z = x.intersection(y)
print(f'This is intersection element {z} between these two sets')