# -------------------------------------------- 1 ----------------------------------------------------

''' 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
(   т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
    (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести
    наименования предприятий, чья прибыль ниже среднего.'''

company = {}
n = int(input('Введите количество предприятий: '))
profit_comp_year = 0
all_profit = 0

for i in range(n):
    name = input(str(i + 1) + '-я компания: ')
    for j in range(4):
        quarterly_profit = int(input('Прибыль за квартал ' + str(j + 1) + '-й квартал: '))
        profit_comp_year += quarterly_profit
    company[name] = profit_comp_year
    all_profit += profit_comp_year

average_profit = all_profit / n
print(f'Средняя прибыль {average_profit:.2f}. Компании с прибылью выше среднего: ')
for i in company:
    if company[i] > average_profit:
        print(i)
print(f'Средняя прибыль {average_profit:.2f}. Компании с прибылью ниже среднего: ')
for i in company:
    if company[i] < average_profit:
        print(i)

# -------------------------------------------- 2 ----------------------------------------------------

''' 2.	Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется 
    как коллекция, элементы которой это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и 
    [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].'''

from collections import deque

str_16 = '0123456789ABCDEF'
str_dict = {str_16[i]: int(i) for i in range(len(str_16))}
int_dict = {int(i): str_16[i] for i in range(len(str_16))}
dict_16 = {**str_dict, **int_dict}


def sum_16(a, b):
    carry = 0
    result = deque()
    if len(b) > len(a):
        a, b = deque(b), deque(a)
    else:
        a, b = deque(a), deque(b)
    while a:
        if b:
            tot = dict_16[a.pop()] + dict_16[b.pop()] + carry
        else:
            tot = dict_16[a.pop()] + carry
        carry = 0
        if tot < 16:
            result.appendleft(dict_16[tot])
        else:
            result.appendleft(dict_16[tot - 16])
            carry = 1
    if carry:
        result.appendleft('1')

    return list(result)


def mult_16(a,b):
    result = deque()
    non = deque([deque() for _ in range(len(b))])
    a, b = a.copy(), deque(b)

    for i in range(len(b)):
        n = dict_16[b.pop()]
        for j in range(len(a) - 1, -1, -1):
            non[i].appendleft(n * dict_16[a[j]])
        for _ in range(i):
            non[i].append(0)
    carry = 0

    for _ in range(len(non[-1])):
        res = carry
        for i in range(len(non)):
            if non[i]:
                res += non[i].pop()
        if res < 16:
            result.appendleft(dict_16[res])
        else:
            result.appendleft(dict_16[res % 16])
            carry = res // 16
    if carry:
        result.appendleft(dict_16[carry])
    return list(result)


a = ['A', '2']
b = ['C', '4', 'F']

print(f'{a} + {b} = {sum_16(a, b)}')
print(f'{a} + {b} = {mult_16(a, b)}')
