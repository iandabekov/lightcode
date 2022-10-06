
car = input('Какую машину хотите купить(лексус или тойота)? ')
year = int(input('Какого года хотите машину? '))
car_mileage = int(input('Какой пробег машины желаете? '))
color = input('Какой цвет(серый или белый)? ')
masters = int(input('Какой минимальное количество бывших хозяинов должно быть? '))

if car == 'тойота' or car == 'лексус' and year >= 2004 and car_mileage <= 150000 and color == 'серый' or color == 'белый' and masters <= 2:
    print(car)
    print(year)
    print(car_mileage)
    print(color)
    print(masters)
    print('Цена на машину 9000$')
elif car == 'тойота' or car == 'лексус' and year >= 2004 and car_mileage >= 150001 and  car_mileage <= 200000 and color == 'серый' or color == 'белый' and masters <= 2:
    print(car)
    print(year)
    print(car_mileage)
    print(color)
    print(masters)
    print('Цена на машину 8000$')



