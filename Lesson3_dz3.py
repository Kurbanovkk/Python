"""Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""

list_ = [1.1, 1.2, 3.1, 5, 10.01]
array = [i - (int(i)) for i in list_]
print(max(array) - min(array))