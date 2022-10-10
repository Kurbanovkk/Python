""" Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

*Пример*

- при N=236     ->        [2, 2, 59]
"""

number_ = int(input('Введите число N: '))


def num_multipliers(number_):
    list_ = []
    num = 2

    while number_ / num != 1:
        if number_ % num == 0:
            list_.append(num)
            number_ //= num
        else:
            num += 1
    else:
        list_.append(number_)
    return list_


print(num_multipliers(number_))
