# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

from cgitb import reset
from itertools import count


def Encode(string):
    x = string[0]
    count = 0
    res = ''
    for i in range(len(string)):
        if (string[i] == x):
            count += 1
        else:
            res = res + str(count) + x
            count = 1
            x = string[i]
    res = res + str(count) + x
    return(res)

print(Encode(input('Введите строку: ')))

def Decode(string):
    res = ''
    count = ''
    for i in string:
        if (i.isdigit()):
            count += i
        else:
            res += int(count) * i
            count = ''
    return(res)
print(Decode(input('Введите строку: ')))    