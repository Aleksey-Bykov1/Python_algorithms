# -------------------------------------------- 1 ----------------------------------------------------

'''
    1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами
    на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть
    реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
'''

from random import randint as rnd

'''
Добавил в исходный алгоритм проверку на обмен элементов для уменьшения количества проходов по списку.
Остальные доработки изменяют тип алгоритма на Шейкерную сортировку, Чётно-нечётную сортировку или Сортировку расчёской.
А это уже не совсем пузырьковая сортировка на мой взгляд.
'''


def bubble_sort(lst):
    print(f'До сортировки: {lst}')
    lenght = len(lst)
    for i in range(lenght):
        swapped = False
        for j in range(0, lenght - i - 1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if swapped == False:
            break
    return print(f'После сортировки: {lst}')


bubble_sort([rnd(-100, 100) for i in range(20)])

# -------------------------------------------- 2 ----------------------------------------------------

''' 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными 
    числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
'''

from random import uniform as unf


def merge_sort(lst):
    def merge(one, two):
        res = []
        i, j = 0, 0
        while i < len(one) and j < len(two):
            if one[i] < two[j]:
                res.append(one[i])
                i += 1
            else:
                res.append(two[j])
                j += 1
        res.extend(one[i:] if i < len(one) else two[j:])
        return res

    def div_half(lst):
        if len(lst) == 1:
            return lst
        elif len(lst) == 2:
            return lst if lst[0] <= lst[1] else lst[::-1]
        else:
            return merge(div_half(lst[:len(lst) // 2]), div_half(lst[len(lst) // 2:]))

    return div_half(lst)


lst = [round(unf(0, 50), 2) for _ in range(20)]

print('До сортировки:', lst)
print('После сортировки:', merge_sort(lst))

# -------------------------------------------- 3 ----------------------------------------------------

''' 3.	Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. 
    Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше 
    медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком 
    сложно, то используйте метод сортировки, который не рассматривался на уроках.
'''

from random import randint as rnd


def median(lst, n):
    if len(lst) == 1:
        return lst[0]
    for med in lst:
        left_el = [i for i in lst if i < med]
        right_el = [i for i in lst if i > med]
        pivots = [i for i in lst if i == med]
        if n < len(left_el):
            return median(left_el, n)
        elif n < len(left_el) + len(pivots):
            return pivots[0]
        else:
            return median(right_el, n - len(left_el) - len(pivots))


m = 20
lst = [rnd(0, 20) for _ in range(2 * m + 1)]
print(f'Исходный список:\n{lst}')
print(f'Медианой списка является: {median(lst, len(lst) / 2)}')

