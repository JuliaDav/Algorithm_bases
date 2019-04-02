# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import timeit
import cProfile
import random

SIZE = 100000
MIN_ITEM = -100000
MAX_ITEM = 100000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
#print(array)

# Первое решение:
def max_below_zero1():
    i = 0
    index = -1
    while i < len(array):
        if array[i] < 0 and index == -1:
            index = i
        elif 0 > array[i] > array[index]:
            index = i
        i += 1

    if index != -1:
        result1 = (f'Максимальное отрицательное число {array[index]} '
              f'находится в ячейке {index}')

#Второе решение:
def max_below_zero2():
    b = []
    for i in range(SIZE):
        if array[i] < 0:
            b.append(array[i])
    result2 = (f'Максимальный отрицательный элемент {max(b)}, позиция {array.index(max(b))}')


print(timeit.timeit("max_below_zero1()", setup="from __main__ import max_below_zero1", number = 10))
print(timeit.timeit("max_below_zero2()", setup="from __main__ import max_below_zero2", number = 10))
#Увеличим элементы массива в 10 раз:
SIZE = 1000000
MIN_ITEM = -100000
MAX_ITEM = 100000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(timeit.timeit("max_below_zero1()", setup="from __main__ import max_below_zero1", number = 10))
print(timeit.timeit("max_below_zero2()", setup="from __main__ import max_below_zero2", number = 10))
#Увеличим элементы массива в 10 раз:
SIZE = 10000000
MIN_ITEM = -100000
MAX_ITEM = 100000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(timeit.timeit("max_below_zero1()", setup="from __main__ import max_below_zero1", number = 10))
print(timeit.timeit("max_below_zero2()", setup="from __main__ import max_below_zero2", number = 10))
# Второй способ решения задачи в среднем в два раза быстрее первого.
# Сложность обоих алгоритмов линейная, при увеличении количества элементов массива
# скорость выполнения возрастает пропорционально
