# сумма элементов списка на нечетных позициях

import random
mass = [random.randint(0, 10) for i in range(5)]
print(mass)
arr = []
for i in range (len(mass)):
    if (i % 2 != 0):
        arr.append(mass[i])

print(arr)
summ = 0
for i in range (len(arr)):
    summ += arr[i]

print(summ)