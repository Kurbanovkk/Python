# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
from math import fabs


x = int(input('Введите чило  x: '))
y = int(input('Введите чило  y: '))
z = int(input('Введите чило  z: '))

if x == 1 and y == 1 and z == 1:
    i = False

if x == 0 and y == 0 and z == 0:
    i = True

if x == 1 and y == 1 and z == 0:
    i = False

if x == 1 and y == 0 and z == 0:
    i = False

if x == 1 and y == 0 and z == 1:
    i = False

if x == 0 and y == 0 and z == 1:
    i == False

if x == 0 and y == 1 and z == 1:
    i == False

if x == 0 and y == 1 and z == 0:
    i == False

print(i)
