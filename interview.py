language = input("Какой язык програмирования вы знаете? ")
age = int(input('Сколько вам лет? '))
exp = int(input("Какой у вас опыт? "))
salary = int(input("Желаемая зарплата? "))

if language == 'python' or language == 'java' or language == 'javascript' and age >= 18 and age <= 65 and exp >= 3 and salary <= 60000:
    print('Язык программирования:', language)
    print('Возраст: ', age)
    print('Опыт:', exp)
    print('Желаемая зарплата:', salary)
    print('Вы нам подходите!')
else:
    print('Язык программирования:', language)
    print('Возраст: ', age)
    print('Опыт:', exp)
    print('Желаемая зарплата:', salary)
    print('Вы нам не подходите, простите!')
