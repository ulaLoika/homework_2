# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент
# с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].


'''Один вариант решения'''

print("Введите через пробел изначальный список,чтобы закончить ввод нажмите ENTER")
list=[int(i) for i in input().split()]
print("Введите числа.Чтобы закончить ввод введите 999")
while True:
    a=int(input())
        if a==999:
        break
    list.append(a)
list.sort(reverse = True)
print(list)

list_1 = input.split(' ')


'''Другой вариант решения'''

list=[]
while True:
    try:
        a=int(input())
        if a==999:
            break
        list.append(a)
    except ValueError:
        print('Введите число:')
list.sort(reverse = True)
print(list)