from collections import defaultdict

text = 'В 1960-е годы в СССР начались попытки запускать аппараты к Венере в рамках космической программы «Венера». Первый пуск был неудачными, но уже второй аппарат Венера-1 достиг зоны действия тяготения планеты, где с ним было потеряна связь — он пролетел на расстоянии 100 000 км от поверхности. В 1965 году результат был уже лучше — 24 000 км. Венера-4 доставила спускаемый аппарат и смогла получить данные о давлении, что использовали при построении следующих аппаратов. Венера-7 впервые совершила мягкую посадку на другую планету — в 1970-м году. А Венера-9 в 1975 году впервые передала телевизионную панораму с Венеры на Землю.'
list_text = text.split(' ')
# print(list_text)


d = {}
for i in list_text:
    d[i] = len(i)
d2 = ''
for i in d.keys():
     if d[i] == max(d.values()):
        print(i)
print(d2)






# res = ''
# res2 = 'В'
# for i in list_text:
#     if len(i) > len(res):
#         res = i
#     print(list_text.count(i))
#     # if list_text.count(i) > list_text.count(res2):
#     #     res2 = i
#
#
# print(res)
# print(res2)
# print(list_text.count('в'))


# # my_list = ["python is best for coders", "python is fun", "python is easy to learn"]
# my_list = text.split()
# print("The list is :")
# print(my_list)
#
# my_temp = defaultdict(int)
#
# for sub in my_list:
#     for word in sub.split():
#         my_temp[word] += 1
# dict2 = {}
# for i in my_list:
#     dict2[i] = len(i)
# print('*' * 100)
# print(dict2.values())
# for key, value in dict2.items():
#     if value == max(dict2.values()):
#         print('-' * 100)
#         longest = key
# print(dict2)
#
# result = max(my_temp, key=my_temp.get)
#
# print("The word that has the maximum frequency :")
# print(result)
# print(f"The longest word is:\n{longest}")
