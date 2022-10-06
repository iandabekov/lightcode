file_ext = input('Напишите имя файла с расширением: ')

name_n_ext = file_ext.split('.')
print(name_n_ext)
print('Имя файла', name_n_ext[0],' расширение файла ', name_n_ext[-1])
