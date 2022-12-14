"""
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

Пример:

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
"""
from cmath import sqrt


a_x = int(input('Введите координату x точки А: '))
a_y = int(input('Введите координату y точки А: '))
b_x = int(input('Введите координату x точки Б: '))
b_y = int(input('Введите координату y точки Б: '))

lenght = sqrt(((b_x - a_x) ** 2) + ((b_y - a_y) ** 2))
print(f'Раастояние между точками А и Б составляет: {lenght}')
