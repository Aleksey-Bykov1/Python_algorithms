# -------------------------------------------- 1 ----------------------------------------------------

''' 1.	В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне
    от 2 до 9.'''

# Без использования словаря

n = list(range(2, 100))
multiples_2 = 0
multiples_3 = 0
multiples_4 = 0
multiples_5 = 0
multiples_6 = 0
multiples_7 = 0
multiples_8 = 0
multiples_9 = 0

for i in n:
    if i % 2 == 0:
        multiples_2 += 1
    if i % 3 == 0:
        multiples_3 += 1
    if i % 4 == 0:
        multiples_4 += 1
    if i % 5 == 0:
        multiples_5 += 1
    if i % 6 == 0:
        multiples_6 += 1
    if i % 7 == 0:
        multiples_7 += 1
    if i % 8 == 0:
        multiples_8 += 1
    if i % 9 == 0:
        multiples_9 += 1
print(f'{multiples_2 = }')
print(f'{multiples_3 = }')
print(f'{multiples_4 = }')
print(f'{multiples_5 = }')
print(f'{multiples_6 = }')
print(f'{multiples_7 = }')
print(f'{multiples_8 = }')
print(f'{multiples_9 = }')

# С использованием словаря

multiples = dict.fromkeys(range(2, 10), 0)

for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            multiples[j] += 1

for key in multiples:
    print(f'{key} кратны {multiples[key]} чисел')

# -------------------------------------------- 2 ----------------------------------------------------

''' 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив 
    со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 
    (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят 
    четные числа.'''

n = [int(i) for i in input("Введите несколько чисел через пробел: ").split()]
index_n = []

for i in range(len(n)):
    if n[i] % 2 == 0:
        index_n.append(i)
print(f'Номера четных индексов в списке "n" - {index_n}')

# -------------------------------------------- 3 ----------------------------------------------------

''' 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.'''

from random import randint as rnd

n = [rnd(1, 100) for i in range(rnd(17, 29))]
print(n)
max_ind, max_val = 0, 0
min_ind, min_val = 0, 99999999999

for ind, val in enumerate(n):
    if val > max_val:
        max_ind, max_val = ind, val
    elif val < min_val:
        min_ind, min_val = ind, val

print(f'{min_ind = }, {min_val = }, {max_ind = }, {max_val = }')

n[min_ind] = max_val
n[max_ind] = min_val

print(n)

# -------------------------------------------- 4 ----------------------------------------------------

''' 4. Определить, какое число в массиве встречается чаще всего.'''

from random import randint as rnd

n = [rnd(1, 100) for i in range(rnd(42, 58))]
print(n)
count_n = 0
num = 0

for i in n:
    if n.count(i) > count_n:
        count_n = n.count(i)
        num = i

print(f'Наибольшее число повторений - {count_n}, у числа - {num}')

# -------------------------------------------- 5 ----------------------------------------------------

''' 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) 
    в массиве.'''

from random import randint as rnd

n = [rnd(-100, 100) for i in range(rnd(27, 42))]
print(n)
max_neg_n = -float('inf')

for ind, val in enumerate(n):
    if val < 0 and val > max_neg_n:
        max_neg_n = val
        ind_n = ind
print(f'Максимальное минимальное число в списке: {max_neg_n}, значение индекса {ind_n}')

# -------------------------------------------- 6 ----------------------------------------------------

''' 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. 
    Сами минимальный и максимальный элементы в сумму не включать.'''

from random import randint as rnd

n = [rnd(1, 100) for i in range(rnd(24, 38))]
print(n)
max_ind, max_val = 0, 0
min_ind, min_val = 0, 99999999999

for ind, val in enumerate(n):
    if val > max_val:
        max_ind, max_val = ind, val
    elif val < min_val:
        min_ind, min_val = ind, val

print(f'{min_ind = }, {min_val = }, {max_ind = }, {max_val = }')

if min_ind < max_ind:
    print('Сумма элементов между максимальным и минимальным = ', sum(n[min_ind + 1 : max_ind]))
else:
    print('Сумма элементов между максимальным и минимальным = ', sum(n[max_ind + 1: min_ind]))

# -------------------------------------------- 7 ----------------------------------------------------

''' 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между 
    собой (оба являться минимальными), так и различаться. '''

from random import randint as rnd

n = [rnd(1, 100) for i in range(rnd(23, 44))]
print(n)

min_num = n[0]
min_num_2 = n[1]

for i in n:
    if i < min_num:
        min_num_2 = min_num
        min_num = i
    elif i < min_num_2:
       min_num_2 = i

print(f'Минимальное число {min_num}, второе минимальное число {min_num_2}')

# -------------------------------------------- 8 ----------------------------------------------------

''' 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять 
    сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести 
    полученную матрицу.'''

str_n = 4
col_n = 4
a = [[int(input('Введите числа для списка: ')) for i in range(col_n)] for j in range(str_n)]
for i in range(len(a)):
    a[i].append(sum(a[i]))
print('Итоговая матрица')
for i in a:
    for j in i:
        print(f'{j:>8}', end='')
    print()

# -------------------------------------------- 9 ----------------------------------------------------

''' 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.'''

from random import randint as rnd

S = 8
C = 6
a = [[int(rnd(1, 100)) for _ in range(C)] for _ in range(S)]
min_col = float('inf')
max_min = -float('inf')

for i in a:
    for j in i:
        print(f'{j:>4}', end='')
    print()

for j in range(C):
    for i in range(S):
        if a[i][j] < min_col:
            min_col = a[i][j]
    if min_col > max_min:
        max_min = min_col

print("Максимальный среди минимальных: ", max_min)
