dict1 = {'a': 5, 'b': 3, 'c': 8, 'd': 14}

for key, value in dict1.items():
    if value % 3 == 0:
        print(f'{key} = HI')
    elif value % 5 == 0:
        print(f'{key} = Bye')