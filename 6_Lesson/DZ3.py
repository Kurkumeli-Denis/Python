

import math

mass = input ('Введите числа через пробел: ').split()
print(mass)

a = list(map(int, mass))
print(a)
def uslovie(x):
    if (math.sqrt(x) % 2 != 0):
        return True
    else:
        return False

b = list(filter(uslovie, a ))
print(b)