"""Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""


value_ = int(input('Введите десятичное значение:'))
array = []


def reverse_(value_, array=[]):
    while value_ > 0:
        array.append(value_ % 2)
        value_ = value_ // 2
    return array[::-1]


print(reverse_(value_, array))
