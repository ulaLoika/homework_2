# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

'''
max = 10
slova = print ('Введите несколько слов через пробел и нажмите ENTER: ')
for slova in input().split():
            if len(slova) > max:
            list = slova.split()
            print(list[:10])
        else:
            list = slova.split()
            print(list)
старый код
'''
'''
list=input().split()
i=1
for slova in list:
    if len(slova)>10:
        print(i, ".",slova[:10])
    else:
        print(i,".",slova)
    i+=1
старый код  
'''
print ('Введите слова через пробел и нажмите ENTER: ')

list=input().split()
print ()
for num, val in enumerate(list, 0):
    if len(val)>10:
        print(str(num) + '.' + str(val[:10]))
    else:
        print(str(num) + '.' + str(val))

input()