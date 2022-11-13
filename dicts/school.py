school = {
    '1а': 40,
    '1б': 38,
    "2б": 42,
    "6а": 37,
    "7в": 36,
    "8г": 35,
    "9а": 37,
    "10а": 34,
    "11б": 33
}

#a)

school['7в'] = 34
print(school)

#б)

school['7г'] = 33
print(school)
#c)

school.pop('11б')
print(school)

#Общее количество учащихся
total = sum(school.values())
print(total)
