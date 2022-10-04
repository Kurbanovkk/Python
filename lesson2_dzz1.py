"""Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:

6782 -> 23
0,56 -> 11
"""

value_ = input('Введите вещественное число: ')


def sum_(x):
    res_ = 0
    for i in range(len(x)):
        if x[i] != ',':
            res_ += int(x[i])
        else:
            continue
    return res_


print(sum_(value_))
