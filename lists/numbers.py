numbers = [1,2,3,4,5,6,7,8,9]
def elements(lst1):
    first = lst1[0]
    last = lst1[-1]
    middle = lst1[(len(lst1)// 2)]

    return f'{first}, {last}, {middle}'
print(elements(numbers))

