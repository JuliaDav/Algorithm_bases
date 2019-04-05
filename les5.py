#1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

factories = {}
n = int(input("Количество предприятий: "))
s = 0
for i in range(n):
    fname = input('Введите название ' +  str(i + 1) + '-го предприятия: ')
    profit1 = int(input('Введите прибыль за 1 квартал: '))
    profit2 = int(input('Введите прибыль за 2 квартал: '))
    profit3 = int(input('Введите прибыль за 3 квартал: '))
    profit4 = int(input('Введите прибыль за 4 квартал: '))
    total_profit = profit1 + profit2 + profit3 + profit4
    factories[fname] = total_profit
    s += total_profit

avrg = s / n
print("\nСредняя прибыль: %.0f. Предприятия с прибылью выше среднего:" % avrg)
for i in factories:
    if factories[i] > avrg:
        print(i)
print("Предприятия с прибылью ниже среднего:")
for i in factories:
    if factories[i] < avrg:
        print(i)
print(factories)