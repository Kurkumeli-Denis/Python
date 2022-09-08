# N = 3  --->   1, 2, 6  (1, 1*2, 1*2*3)

x = int(input('Введите число: '))
summ = 1
i = 1
while (i <= x):
    summ = summ * i
    print(summ)
    i += 1