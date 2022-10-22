"""3 Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной
последовательности.

*Пример*

- при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]"""

import random
size_list = int(input('Введите размер массива: '))


def fill(size_list):
    lst = []
    for i in range(size_list):
        lst.append(random.randint(0, 10))
    return lst


new_list = fill(size_list)
print(f'последовательность чисел до изменений {new_list}')


list_ = []
for i in new_list:
    count = 0
    for j in new_list:
        if i == j:
            count += 1
    if count == 1:
        list_.append(i)

print(f'новый уникальный список: {list_}')


# Решение 2
res1 = []
res = [res1.append[i] for i in new_list for j in new_list if i != j]
print(f'новый уникальный список 2: {res}')
