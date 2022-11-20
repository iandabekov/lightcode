notes = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 3, 1]

note = int(input('Enter some number you want to cash out: '))

cash_out = []


def atm(money):
    for i in notes:
        while money // i > 0:
            cash_out.append(i)
            money -= i
    return cash_out

print(atm(note))
