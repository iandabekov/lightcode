city_list = ['London', 'New_york']
move = input('''Выберите действие:
1. Добавить новый город
2. Отобразить список городов
3. Заменить город
4. Удалить город
5. Выход
''')

if move == '1':
    add_city = input('Введите название города: ')
    if add_city in city_list:
        print(f'Такой город уже есть! {add_city} - {city_list.index(add_city)}')
    elif add_city not in city_list:
        city_list.append(add_city)
        print(f'Город {add_city} добавлен!')
        print(city_list) # New York
        move = input('''Выберите действие:
        1. Добавить новый город
        2. Отобразить список городов
        3. Заменить город
        4. Удалить город
        5. Выход
        ''')
    else:
        print('Некорректное название!')
    
    
elif move == '2':
    print(city_list) # New York
    move = input('''Выберите действие:
    1. Добавить новый город
    2. Отобразить список городов
    3. Заменить город
    4. Удалить город
    5. Выход
    ''')
    if move == '3':
        city_name = input('Введите название города: ')
        if city_name in city_list:
            print(f'Текущий город: {city_name}')
            city_list.remove(city_name)
            new_city = input('Введите новый город: ')
            city_list.append(new_city)
            print(city_list)
        elif city_list not in city_list:
            print('Текущий город отсутствует.')
        else:
            print('Некорректное название!')
        move = input('''Выберите действие:
            1. Добавить новый город
            2. Отобразить список городов
            3. Заменить город
            4. Удалить город
            5. Выход
            ''')   
        
    elif move == '1':
        add_city = input('Введите название города: ')
        if add_city in city_list:
            print(f'Такой город уже есть! {add_city} - {city_list.index(add_city)}')
        elif add_city not in city_list:
            city_list.append(add_city)
            print(f'Город {add_city} добавлен!')
            print(city_list) # New York
            move = input('''Выберите действие:
            1. Добавить новый город
            2. Отобразить список городов
            3. Заменить город
            4. Удалить город
            5. Выход
            ''')
        else:
            print('Некорректное название!')
    elif move  == '4':
        city_name = input('Введите название города: ')
        if city_name in city_list:
            city_list.remove(city_name)
            print(city_list)
        elif city_name not in city_list:
            print('Текущий город отсутствует.')
            print(city_list)  
        else:
            print('Некорректное название!')
        move = input('''Выберите действие:
            1. Добавить новый город
            2. Отобразить список городов
            3. Заменить город
            4. Удалить город
            5. Выход
            ''') 
        
    elif move == '5':
        print('Пока!')
elif move == '3':
        city_name = input('Введите название города: ')
        if city_name in city_list:
            print(f'Текущий город: {city_name}')
            city_list.remove(city_name)
            new_city = input('Введите новый город: ')
            city_list.append(new_city)
            print(city_list)
        elif city_list not in city_list:
            print('Текущий город отсутствует.')
        else:
            print('Некорректное название!')
        move = input('''Выберите действие:
            1. Добавить новый город
            2. Отобразить список городов
            3. Заменить город
            4. Удалить город
            5. Выход
            ''')   
elif move  == '4':
        city_name = input('Введите название города: ')
        if city_name in city_list:
            city_list.remove(city_name)
            print(f'Список городов {city_list}')
        elif city_name not in city_list:
            print('Текущий город отсутствует.')  
        else:
            print('Некорректное название!')
        move = input('''Выберите действие:
            1. Добавить новый город
            2. Отобразить список городов
            3. Заменить город
            4. Удалить город
            5. Выход
            ''') 

        
elif move == '5':
    print('Пока!')

