# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:      - [2, 3, 4, 5, 6] => [12, 15, 16];
#             - [2, 3, 5, 6] => [12, 15]


print('Задайте размерность списка')
n = int(input())
print('Заполните список целыми числами через Enter')
lst = []


for i in range(n):
    lst.append(int(input()))

print(f'Изначальный список {lst}')

m_ind = n - 1
multi = []

if n % 2 == 0:
    for i in range(0, n // 2):
        multi.append(lst[i] * lst[m_ind])
        m_ind -= 1   
else:
    for i in range(n // 2 + 1):
        multi.append(lst[i] * lst[m_ind])
        m_ind -= 1
print(f'Перемноженный список {multi}')