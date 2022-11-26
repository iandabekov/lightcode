def file_reading():
    with open('example.txt', 'r+') as file:
        f = file.read()
        f1 = f.replace('\n', ' ')
        list1 = f1.split(' ')
    return list1


text = file_reading()


def my_filter(word):
    if 'p' in word:
        return True
    else:
        return False


result = list(filter(my_filter, text))
print(result)



