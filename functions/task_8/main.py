month = int(input('Enter number of month: '))


def season(month_num):
    if month_num in (12, 1, 2):
        answer = 'Winter'
    elif month_num in (3, 4, 5):
        answer = 'Spring'
    elif month_num in (6, 7, 8):
        answer = 'Summer'
    elif month_num in (9, 10, 11):
        answer = 'Fall'
    else:
        answer = 'This number is out of year range'
    return answer


print(season(month))
