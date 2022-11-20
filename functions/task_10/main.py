

def measurement():
    temperatures = []
    n = 0
    while n > -300:
        n = int(input('Enter your measured temperature: '))
        if n >= -300:
            temperatures.append(n)
    return sum(temperatures) / len(temperatures)

print(measurement())