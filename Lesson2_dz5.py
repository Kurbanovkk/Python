# Задание 5 Реализуйте алгоритм перемешивания списка.
import random


def range_(list_=[]):
    for i in range(len(list_)):
        count = random.randrange(0, len(list_))
        temp = list_[i]
        list_[i] = list_[count]
        list_[count] = temp

    return list_


list_ = [22, -5, 1113, 43, 765, 43, 321, -555]
print(range_(list_))
