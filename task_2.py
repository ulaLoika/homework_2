# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
# x=[int(i) for i in input().split()]


i = int(input('Введите длину списка: '))
schetchik = 0
spisok = []
while schetchik < i:
    el = input('Введите элемент списка через пробел: ')
    spisok.append(el)
    schetchik += 1
print(spisok)

p = 0
temp = 0
while p < len(spisok) - 1:
    temp = spisok[p]
    spisok[p] = spisok[p + 1]
    spisok[p + 1] = temp
    p += 2
print(spisok)

