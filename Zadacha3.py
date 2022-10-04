# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.

# Пример:     - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


print('Задайте размерность списка')
n = int(input())
print('Заполните список вещественными числами через Enter')
lst = []


for i in range(n):
    lst.append(float(input()))

print(lst)


for i in range(n):
    while lst[i] >= 1:
        lst[i] -= 1    

minn = lst[0]
maxx = lst[0]


for i in range(n):
    if lst[i] < minn:
        minn = lst[i]
    elif lst[i] > maxx:
        maxx = lst[i]
        
print(round(maxx - minn, 2))
