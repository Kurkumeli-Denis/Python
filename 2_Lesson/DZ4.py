# [-N, N]  [1, 2, 3, 4, 5]  (1: 3)----> [1, 2, 3]

n = int(input('Введите количество элементов: '))
startt = int(input('Введите начальную позицию: '))
endd = int(input('Введите конечную позицию: '))
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
