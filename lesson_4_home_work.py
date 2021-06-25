# -------------------------------------------- 1 ----------------------------------------------------

''' 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках практического задания
первых трех уроков. Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.'''

''' Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) 
    вводится с клавиатуры.'''

# ---------------------------------- Нерекурсивный алгоритм --------------------------------------------

import cProfile
import timeit


def num_series(n):
    sum_num = 0
    for i in range(n):
        sum_num += 1 / (-2) ** i
    return sum_num


def memorize(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r
    return g


@memorize
def num_series_1(n):
    sum_num = 0
    for i in range(n):
        sum_num += 1 / (-2) ** i
    return sum_num


def num_series_2(n, memory=[]):
    if n < len(memory):
        return memory[n]
    else:
        sum_num = 0
        for i in range(n):
            sum_num += 1 / (-2) ** i
            memory.append(sum_num)
        return sum_num


print(f'{num_series(50) = }')
print('Измерение времени работы нерекурсивного алгоритва с использованием timeit')
print(timeit.timeit('num_series(50)', globals=globals()))
cProfile.run('num_series(50)')

print(f'{num_series_1(50) = }')
print('С добавлением декоратора мемоизации через словарь')
print(timeit.timeit('num_series_1(50)', globals=globals()))
cProfile.run('num_series_1(50)')

print(f'{num_series_2(50) = }')
cProfile.run('num_series(50)')
print('С добавлением мемоизации через список')
print(timeit.timeit('num_series_2(50)', globals=globals()))
cProfile.run('num_series_2(50)')


''' В нерекурсивном исполнении самым производительным алгоритмом, по результатам измерений, является алгоритм с 
    использованием мемоизации через словарь. Добавляя мемоизирующий декоратор, удалось снизить сложность алгоритма 
    до линейной.'''

# ----------------------------------- Рекурсивный алгоритм ---------------------------------------------

import cProfile
import timeit


def num_series_rec_1(n, i=1, result=None):
    if result is None:
        result = []
    if n > 0:
        result.append(i)
        return num_series_rec_1(n - 1, -i / 2, result)
    return result


result = num_series_rec_1(10)
print(sum(result))


def num_series_rec_2(n, i=1):
    if n > 0:
        yield i
        yield from num_series_rec_2(n - 1, -i / 2)


result = list(num_series_rec_2(10))
print(sum(result))


print('Измерение времени работы рекурсивного алгоритва с мемоизацией через список')
print(timeit.timeit('num_series_rec_1(10)', globals=globals()))
cProfile.run('num_series_rec_1(10)')

print('Измерение времени работы рекурсивного алгоритва с работой через генератор')
print(timeit.timeit('num_series_rec_2(10)', globals=globals()))
cProfile.run('num_series_rec_2(10)')


''' В рекурсивном исполнении самым производительным алгоритмом, по результатам измерений, является алгоритм с 
    использованием генератора. В итоге получили линейную сложность алгоритма.'''

''' По результатам измерений наибольшей производительностью для данной задачи показал нерекурсивный алгоритм с 
    мемоизацией через словарь'''

# -------------------------------------------- 2 ----------------------------------------------------

''' 2.	Написать два алгоритма нахождения i-го по счёту простого числа.
●	Без использования Решета Эратосфена;
●	Использовать алгоритм решето Эратосфена
'''

import cProfile
import timeit

# С использованием алгоритма решето Эратосфена
def sieve_of_eratosthenes(n):
    n_list = [i for i in range(n * 6)]
    n_list[1] = 0
    i = 2
    s_num_list = []
    while len(s_num_list) < n:
        if n_list[i] != 0:
            s_num_list.append(n_list[i])
            j = i * 2
            while j < len(n_list):
                n_list[j] = 0
                j += i
        i += 1
    return s_num_list[n - 1], s_num_list


n = int(input('Какое по счету простое число вы хотите найти от 1 до 100: '))
print(f'{sieve_of_eratosthenes(n) = }')
print(timeit.timeit('sieve_of_eratosthenes(30)', globals=globals()))
cProfile.run('sieve_of_eratosthenes(30)')

# Без использованием алгоритма решето Эратосфена
def not_sieve(m):
    n = m * 6
    lst = [2]
    for i in range(3, n+1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j*j-1 > i:
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
    return lst[m - 1], lst


m = int(input('Какое по счету простое число вы хотите найти от 1 до 100: '))
print(f'{not_sieve(m) = }')
print(timeit.timeit('not_sieve(30)', globals=globals()))
cProfile.run('not_sieve(30)')

# Какое по счету простое число вы хотите найти от 1 до 100: 30
# sieve_of_eratosthenes(n) = (113, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113])
# 168.21692110900767
#          463 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 main.py:5(sieve_of_eratosthenes)
#         1    0.000    0.000    0.000    0.000 main.py:6(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       428    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        30    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# Какое по счету простое число вы хотите найти от 1 до 100: 30
# not_sieve(m) = (113, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179])
# 150.09833975404035
#          44 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 main.py:28(not_sieve)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        40    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


''' Сложность 1го алгоритма (sieve_of_eratosthenes) = O(n**2).
    Сложность 2го алгоритма (not_sieve)  = O(n**2)
    По производительности лучше, по результатам измерения, 2й алгоритм'''