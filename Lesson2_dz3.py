""" Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
округлённую до трёх знаков после точки.

Пример:

Для n = 6 -> 14.072
    """


def sequence(n):
    temp = [0] * n
    sum_ = 0
    for i in range(1, n + 1):
        temp[i - 1] = ((1+1/i)**i)
        sum_ += temp[i - 1]
    return round(sum_, 3)


numb = sequence(int(input('Введите число n: ')))
print(numb)
