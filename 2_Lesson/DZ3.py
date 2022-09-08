#  (1 + 1 \ k) ^ k    summ

k = int(input('Введите чило: '))
i = 1
form = 0
summ = 0
while (i <= k):
    form = float((1 + (1/k))**k)
    summ = float(summ + form)
    i += 1
print(summ)

