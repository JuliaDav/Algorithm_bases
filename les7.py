# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

import random
a = []
for i in range(10):
    a.append(random.randint(-100,100))
print(a)
print()

def bubble(arr):
    a = arr
    for k in range(len(a) - 1, 0, -1):
        for i in range(k):
            if a[i] > a[i + 1]:
                temp = a[i]
                a[i] = a[i + 1]
                a[i + 1] = temp
    return(a)

print(bubble(a))
print()
print('*************************************')
print()

#2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random
b = []

for i in range(6):
    b.append(random.uniform(0,50))
print(b)
print()

def merge(left, right):
    result = []
    i ,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def mergesort(list):
    if len(list) < 2:
        return list
    middle = int(len(list) / 2)
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])
    return merge(left, right)

print(mergesort(b))
