"""Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""

list_ = []
lenght_ = len(list_) - 1


def composition_(list_=[], lenght_=0):
    comp = 0
    array = []
    for i in range(len(list_)):
        if i != lenght_ - i and i < lenght_ - i:
            comp = list_[i] * (list_[lenght_ - i])
            array.append(comp)
        elif i == lenght_ - i:
            comp = list_[i] * list_[i]
            array.append(comp)
    print(array)


composition_(list_, lenght_)
