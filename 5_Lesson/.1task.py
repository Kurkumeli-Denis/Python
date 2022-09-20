file = open('5lesson(1).txt', 'a')
file.write('1 2 4 5 6')
file.close()
txt = open('5lesson(1).txt', 'r')

lst = txt.read().split()
print(lst)
mass = []
for i in range(len(lst)):
    mass.append(int(lst[i]))
print(mass)

for i in range(len(mass) - 1):
    if (mass[i] + 1 != mass[i+1]):
        mass[i+1] = mass[i] + 1
mass.append(mass[len(mass) - 1] + 1)
print('Восстановленная последовательность:', mass)
