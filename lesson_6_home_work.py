# -------------------------------------------- 1 ----------------------------------------------------

''' 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых
    трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

    Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
    Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность
    вашей ОС.
'''
#  Для просмотра размера памяти занимаемаемого переменными в программе использовал функцию show_sizeof
#  И использовал memory_profiler  для построчного анализа потребления памяти программами на Python
#  Python 3.9.5
#  Operating System: Ubuntu 21.04
#  Architecture: x86-64

import sys
from memory_profiler import profile
from random import randint as rnd


def show_sizeof(x, level=0):
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for y in x.items():
                show_sizeof(y, level + 1)

        elif not isinstance(x, str):
            for y in x:
                show_sizeof(y, level + 1)


@profile
def num():
    n = [rnd(-100, 100) for i in range(rnd(27, 42))]
    max_neg_n = -float('inf')

    for ind, val in enumerate(n):
        if val < 0 and val > max_neg_n:
            max_neg_n = val
            ind_n = ind
    return locals()


# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     20     17.7 MiB     17.7 MiB           1   @profile
#     21                                         def num():
#     22     17.7 MiB      0.0 MiB          33       n = [rnd(-100, 100) for i in range(rnd(27, 42))]
#     23     17.7 MiB      0.0 MiB           1       max_neg_n = -float('inf')
#     24
#     25     17.7 MiB      0.0 MiB          31       for ind, val in enumerate(n):
#     26     17.7 MiB      0.0 MiB          30           if val < 0 and val > max_neg_n:
#     27     17.7 MiB      0.0 MiB           4               max_neg_n = val
#     28     17.7 MiB      0.0 MiB           4               ind_n = ind
#     29     17.7 MiB      0.0 MiB           1       return locals()


# type = <class 'dict'>, size = 232, object = {'n': [-88, -83, -58, -58, -95, -2, -18, 81, 70, 53, -49, 23, 95, 28, 55, 100, 24, 76, 13, -72, 28, 0, 78, -2, -78, -28, -76, -33, -50, 71], 'max_neg_n': -2, 'ind': 29, 'val': 71, 'ind_n': 5}
#  type = <class 'tuple'>, size = 56, object = ('n', [-88, -83, -58, -58, -95, -2, -18, 81, 70, 53, -49, 23, 95, 28, 55, 100, 24, 76, 13, -72, 28, 0, 78, -2, -78, -28, -76, -33, -50, 71])
# 	 type = <class 'str'>, size = 50, object = n
# 	 type = <class 'list'>, size = 312, object = [-88, -83, -58, -58, -95, -2, -18, 81, 70, 53, -49, 23, 95, 28, 55, 100, 24, 76, 13, -72, 28, 0, 78, -2, -78, -28, -76, -33, -50, 71]
# 		 type = <class 'int'>, size = 28, object = -88
# 		 type = <class 'int'>, size = 28, object = -83
# 		 type = <class 'int'>, size = 28, object = -58
# 		 type = <class 'int'>, size = 28, object = -58
# 		 type = <class 'int'>, size = 28, object = -95
# 		 type = <class 'int'>, size = 28, object = -2
# 		 type = <class 'int'>, size = 28, object = -18
# 		 type = <class 'int'>, size = 28, object = 81
# 		 type = <class 'int'>, size = 28, object = 70
# 		 type = <class 'int'>, size = 28, object = 53
# 		 type = <class 'int'>, size = 28, object = -49
# 		 type = <class 'int'>, size = 28, object = 23
# 		 type = <class 'int'>, size = 28, object = 95
# 		 type = <class 'int'>, size = 28, object = 28
# 		 type = <class 'int'>, size = 28, object = 55
# 		 type = <class 'int'>, size = 28, object = 100
# 		 type = <class 'int'>, size = 28, object = 24
# 		 type = <class 'int'>, size = 28, object = 76
# 		 type = <class 'int'>, size = 28, object = 13
# 		 type = <class 'int'>, size = 28, object = -72
# 		 type = <class 'int'>, size = 28, object = 28
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 28, object = 78
# 		 type = <class 'int'>, size = 28, object = -2
# 		 type = <class 'int'>, size = 28, object = -78
# 		 type = <class 'int'>, size = 28, object = -28
# 		 type = <class 'int'>, size = 28, object = -76
# 		 type = <class 'int'>, size = 28, object = -33
# 		 type = <class 'int'>, size = 28, object = -50
# 		 type = <class 'int'>, size = 28, object = 71
#  type = <class 'tuple'>, size = 56, object = ('max_neg_n', -2)
# 	 type = <class 'str'>, size = 58, object = max_neg_n
# 	 type = <class 'int'>, size = 28, object = -2
#  type = <class 'tuple'>, size = 56, object = ('ind', 29)
# 	 type = <class 'str'>, size = 52, object = ind
# 	 type = <class 'int'>, size = 28, object = 29
#  type = <class 'tuple'>, size = 56, object = ('val', 71)
# 	 type = <class 'str'>, size = 52, object = val
# 	 type = <class 'int'>, size = 28, object = 71
#  type = <class 'tuple'>, size = 56, object = ('ind_n', 5)
# 	 type = <class 'str'>, size = 54, object = ind_n
# 	 type = <class 'int'>, size = 28, object = 5


@profile
def not_sieve(m=26):
    n = m * 6
    lst = [2]
    for i in range(3, n + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
    return lst[m - 1], lst


# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     33     17.7 MiB     17.7 MiB           1   @profile
#     34                                         def not_sieve(m = 26):
#     35     17.7 MiB      0.0 MiB           1       n = m * 6
#     36     17.7 MiB      0.0 MiB           1       lst = [2]
#     37     17.7 MiB      0.0 MiB          78       for i in range(3, n+1, 2):
#     38     17.7 MiB      0.0 MiB          77           if (i > 10) and (i % 10 == 5):
#     39     17.7 MiB      0.0 MiB          15               continue
#     40     17.7 MiB      0.0 MiB         226           for j in lst:
#     41     17.7 MiB      0.0 MiB         225               if j*j-1 > i:
#     42     17.7 MiB      0.0 MiB          34                   lst.append(i)
#     43     17.7 MiB      0.0 MiB          34                   break
#     44     17.7 MiB      0.0 MiB         191               if (i % j == 0):
#     45     17.7 MiB      0.0 MiB          27                   break
#     46                                                 else:
#     47     17.7 MiB      0.0 MiB           1               lst.append(i)
#     48     17.7 MiB      0.0 MiB           1       return lst[m - 1], lst


#  type = <class 'tuple'>, size = 56, object = (101, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151])
# 	 type = <class 'int'>, size = 28, object = 101
# 	 type = <class 'list'>, size = 376, object = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151]
# 		 type = <class 'int'>, size = 28, object = 2
# 		 type = <class 'int'>, size = 28, object = 3
# 		 type = <class 'int'>, size = 28, object = 5
# 		 type = <class 'int'>, size = 28, object = 7
# 		 type = <class 'int'>, size = 28, object = 11
# 		 type = <class 'int'>, size = 28, object = 13
# 		 type = <class 'int'>, size = 28, object = 17
# 		 type = <class 'int'>, size = 28, object = 19
# 		 type = <class 'int'>, size = 28, object = 23
# 		 type = <class 'int'>, size = 28, object = 29
# 		 type = <class 'int'>, size = 28, object = 31
# 		 type = <class 'int'>, size = 28, object = 37
# 		 type = <class 'int'>, size = 28, object = 41
# 		 type = <class 'int'>, size = 28, object = 43
# 		 type = <class 'int'>, size = 28, object = 47
# 		 type = <class 'int'>, size = 28, object = 53
# 		 type = <class 'int'>, size = 28, object = 59
# 		 type = <class 'int'>, size = 28, object = 61
# 		 type = <class 'int'>, size = 28, object = 67
# 		 type = <class 'int'>, size = 28, object = 71
# 		 type = <class 'int'>, size = 28, object = 73
# 		 type = <class 'int'>, size = 28, object = 79
# 		 type = <class 'int'>, size = 28, object = 83
# 		 type = <class 'int'>, size = 28, object = 89
# 		 type = <class 'int'>, size = 28, object = 97
# 		 type = <class 'int'>, size = 28, object = 101
# 		 type = <class 'int'>, size = 28, object = 103
# 		 type = <class 'int'>, size = 28, object = 107
# 		 type = <class 'int'>, size = 28, object = 109
# 		 type = <class 'int'>, size = 28, object = 113
# 		 type = <class 'int'>, size = 28, object = 127
# 		 type = <class 'int'>, size = 28, object = 131
# 		 type = <class 'int'>, size = 28, object = 137
# 		 type = <class 'int'>, size = 28, object = 139
# 		 type = <class 'int'>, size = 28, object = 149
# 		 type = <class 'int'>, size = 28, object = 151


if __name__ == "__main__":
    show_sizeof(num())
    show_sizeof(not_sieve())
