"""
1 Вычислить число π c заданной точностью d

*Пример:*

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
"""
value_ = input('Введите точность pi(Вещественное число): ')

for i in range(len(value_) - 1):
    value_ = i

k = 1
s = 0
for i in range(1, 100000):
    if i % 2 != 0:
        s += 4 / k
        k += 2
    else:
        s -= 4 / k
        k += 2
pi = str(s)
print(str(pi[:value_ + 2]))
