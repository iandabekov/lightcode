list1 = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]


def sort_num(list_num):
    positive_list = [i for i in list_num if i > 0]
    negative_list = [i for i in list_num if i < 0]
    return positive_list, negative_list


print(sort_num(list1))
