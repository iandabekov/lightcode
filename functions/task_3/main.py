def func_1(num1, num2):
    product = num1 * num2
    division = func_2(10, 5)
    return division + product


def func_2(num1, num2):
    return num1 / num2


print(func_1(10, 5))
