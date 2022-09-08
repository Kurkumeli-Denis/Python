# 0,56 -> 11

from curses.ascii import isdigit


x = (input('Введите число: '))
i = 0
summ = 0
print (len(list(x)))
while(i < (len(list(x)))):
    if (list(x)[i].isdigit()):
        summ += int(list(x)[i])
        i += 1
    else:
        i += 1
print(summ)

