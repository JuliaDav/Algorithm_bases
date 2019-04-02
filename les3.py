#1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""
def qty(a):
    lst = []
    for el in range(2,100):
        if el % a == 0:
            lst.append(el)
    return(len(lst))
n = int(input('Введите число от 2 до 9: '))
print(f'Числу {n} кратно {qty(n)} чисел в диапазоне от 2 до 99')
"""

#2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6
#(или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
'''
import random
a = []
for i in range(5):
    a.append(random.randint(0,100))
print(a)
b = []
for n in range(len(a)):
    if a[n] % 2 == 0:
        b.append(n+1)
print(b)
'''
#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''
import random
a = []
for i in range(5):
    a.append(random.randint(0,100))
print(a)
b = max(a)
maxN = a.index(b)
c = min(a)
minN = a.index(c)
a[minN], a[maxN] = a[maxN], a[minN]
print(a)
'''

#4. Определить, какое число в массиве встречается чаще всего.
"""
import random
a = []
N = 100
for i in range(N):
    a.append(random.randint(0,10))
print(a)
for i in range(N):
    n = 1
    for j in range(N):
        if a[i] == a[j] and i != j:
            n += 1
    maxN = n
    if n > maxN:
        maxN = n
print(f'Чаще всего ({maxN} раз) встречается число {a[i]}')
"""

#5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random
a = []
N = 10
for i in range(N):
    a.append(random.randint(-100,100))
print(a)
b = []
for i in range(N):
    if a[i] < 0:
        b.append(a[i])
print(f'Максимальный отрицательный элемент {max(b)}, позиция {a.index(max(b))}')


#6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
"""
import timeit
def main():
    import random
    a = []
    N = 10
    for i in range(N):
        a.append(random.randint(0,10))
    print(a)
    maxN = max(a)
    minN = min(a)
    indMax = a.index(maxN) + 1
    indMin = a.index(minN) + 1
    print(indMax, indMin)
    if indMax < indMin:
        print(a[indMax:indMin-1])
        print(sum(a[(indMax):indMin-1]))
    else:
        print(a[indMin:indMax-1])
        print(sum(a[indMin:indMax-1]))

print(timeit.timeit("main()", setup="from __main__ import main", number = 100000))
#cProfile.run('main()')
"""