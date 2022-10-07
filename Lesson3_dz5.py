"""Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
"""

from array import array


fib1 = fib2 = 1
fib3 = fib4 = -1

n = int(input())
array_ = [0, -1, -1]
array2_ = [1, 1]


for i in range(-n, n + 1):
    if i < - 2:
        fib3, fib4 = fib4, fib3 + fib4
        array_.append(fib4)
        i = i + 1
    if i > 2:
        fib1, fib2 = fib2, fib1 + fib2
        array2_.append(fib2)
        i = i + 1


print(array_[::-1] + array2_)
