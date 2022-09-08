# [-N, N]  [1, 2, 3, 4, 5]  (1: 3)----> [1, 2, 3]

n = int(input('Введите количество элементов: '))
startt, endd = [int(s) for s in input('Введите начальную и конечную позиции через пробел: ').split()]
new_list = []
multy = 1

for i in range(-n, n+1):
    new_list.append(i)

print(new_list)
i = startt - 1
while (i < endd):
    multy = multy * new_list[i]
    i += 1
print(multy)

