
""" Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет
"""

value = int(input('Введите число от 1 до 7 включительно: '))
days = {
    1: 'Sunday',
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thusday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'
}

if value <= 5:
    print(f'Сегодня {days[value]} и этот день не является выходным')
else:
    print(f'Сегодня {days[value]},  Ура, это выходной!!!')