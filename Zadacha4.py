# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:     - 45 -> 101101
#             - 3 -> 11
#             - 2 -> 10



n = int(input('Введите число \n'))

lst = []


while n > 0:
    lst.append(n % 2)
    n //= 2  
lst.reverse()
print(lst)