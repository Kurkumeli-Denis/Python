# 5 чисел и находит максимальное

num_1 = int (input('Введите число 1: '))
num_2 = int (input('Введите число 2: '))
num_3 = int (input('Введите число 3: '))
num_4 = int (input('Введите число 4: '))
num_5 = int (input('Введите число 5: '))

max = num_1

if (num_2 > max):
    max = num_2
if (num_3 > max):
    max = num_3
if (num_4 > max):
    max = num_4
if (num_5 > max):
    max = num_5

print(max)


