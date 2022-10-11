"""5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
Коэффициенты могут быть как положительными, так и отрицательными. Степени многочленов могут отличаться."""

import random
from re import X
k = 2


def polynomial(k):
    list_ = []
    for i in range(k, -1, -1):
        d = random.randint(0, 100)
        if i == 0:
            list_.append(f'{d}')
        elif i == 1:
            list_.append(f'{d}x')
            list_.append('+')
        else:
            list_.append(f'{d}x^{i}')
            list_.append('+')
    list_.append('= 0')
    poly = " ".join(map(str, list_))
    return (poly)


new_poly = polynomial(k)
with open('dz5_1.txt', 'w', encoding='utf8') as file:
    file.write(new_poly)

new_pol = polynomial(k)
with open('dz5_2.txt', 'w', encoding='utf8') as file:
    file.write(new_pol)


with open('dz5_1.txt', 'r', encoding='utf8') as file:
    for i in file:
        x = i

print(x)

with open('dz5_2.txt', 'r', encoding='utf8') as file:
    for i in file:
        y = i

print(y)
