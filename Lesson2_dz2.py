"""Задание 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
"""

value_ = int(input('Введите число n: '))


def composition(value_):
    comp = 1
    for i in range(value_):
        comp += (i * comp)
        print(comp)


composition(value_)
