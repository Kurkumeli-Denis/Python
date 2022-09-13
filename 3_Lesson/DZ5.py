# Фибоначчи
x = int(input('Введите длину последовательности: '))
f1 = 1
f2 = 1
mass = [f1]
i = 0
while(i < x - 1):
    mass.append(f2)
    summ = f1 + f2
    f1 = f2
    f2 = summ
    i += 1

print(mass)

arr = []

for i in range(0, len(mass), 1):
    arr.append(mass[-1 - i])
for i in range (0, len(arr), 2):
    arr[i] *= -1

arr.append(0)

for i in range(len(mass)):
    arr.append(mass[i])

print(arr)


