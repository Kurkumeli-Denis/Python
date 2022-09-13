# произведение пар чисел [1, 2, 3, 4, 5]  -> 1*5, 2*4, 3*3  -> 5, 8, 9

import random
mass = [random.randint(0, 10) for i in range(5)]
print(mass)
arr =[]

if (len(mass) % 2 != 0):
    seredina = len(mass) // 2
    for i in range (0, seredina + 1, 1):
        arr.append(mass[i] * mass[-1 - i]) 
else:
    seredina = len(mass) // 2
    for i in range (0, seredina, 1):
        arr.append(mass[i] * mass[-1 - i]) 
    
print(arr)


