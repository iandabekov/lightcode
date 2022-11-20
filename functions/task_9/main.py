a = float(input('contributed money: '))
years = int(input('For how many years: '))


def deposit(a, years_n):
    for i in range(years_n):
        percents = a / 100 * 10
        a += percents

    return a


print(deposit(a, years))
