"""4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
многочлена и записать в файл многочлен степени k.

*Пример:* 

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""
import random
k = int(input('Введите степень: '))


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
with open('Pyth.txt', 'w', encoding='utf8') as file:
    file.write(new_poly)
