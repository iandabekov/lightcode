my_friends = {
    "Joomart": "+996555246810",
    "Adinai": "+996555013579",
    "Ermek": "+996777013579",
    "Atai": "+996777246810",
    "Aslan": "+996999246810",
}
my_friends_2 = {
    "Bakyt": "+996555246815",
    "Altynai": "+996555013574",
    "Erbol": "+996777013573",
    "Aman": "+996777246812",
    "Ayan": "+996999246811",
}

dict_3 = dict(**my_friends, **my_friends_2)
#or
dict_4 = {**my_friends, **my_friends_2}
print(dict_3)
print(dict_4)