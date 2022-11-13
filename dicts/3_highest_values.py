my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
print(my_dict)
keys = sorted(my_dict, key=my_dict.get, reverse=True)[:3]

print(keys)

for i in keys:
    my_dict.pop(i)
print(my_dict)
