


def file_reading():
    with open('example.txt', 'r+') as file:
        f = file.read()
        list1 = f.split()
        c_words = [i for i in list1 if i.startswith('c') or i.startswith('C')]
    return c_words

print(file_reading())