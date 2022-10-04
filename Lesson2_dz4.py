"""Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на позициях a и b. Значения N, a и b вводит пользователь с клавиатуры."""


def fill(temp=[]):
    temp = []
    length_ = int(input('Введите размер списка: '))
    for i in range(-length_, length_ + 1):
        temp.append(i)
    return temp


temp = []
list_ = fill(temp)
print(list_)

a = int(input('Введите позицию а: '))
b = int(input('Введите позицию b: '))

for i in range(len(list_)):
    if i == a:
        a = list_[i]
    if i == b:
        b = list_[i]


print(a * b)
