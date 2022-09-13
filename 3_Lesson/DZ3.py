# разница между максимальным и минимальным числом после запятой [1.2, 1.01, 2.1] --> 20-01 = 19

import random
mass = [round(random.uniform(1.01, 2.50), 2) for i in range(3)]
print(mass)
arr = []

for i in range(len(mass)):
    arr.append(round((mass[i] % 1),2))

print(arr)

minn = arr[0]
maxx = arr[0]

for i in range(len(arr)):
    if (arr[i] > maxx):
        maxx = arr[i]
    if (arr[i] < minn):
        minn = arr[i]

print(maxx, minn)
rez = maxx - minn
print()
print('Разница между мин и макс: ',rez)