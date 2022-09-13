# Определить позицию второго вхождения  [1, 2, 1, 3, 3]  x=1  ответ позиция 2

mass = []
mass = input('Введите строки через пробел: ').split()
x = (input('Введите искомое: '))
print(mass)
i = 0
arr = []


for i in range (len(mass)):
    if (mass[i] == x):
        arr.append(i)
        
        
    
if (len(arr) > 1):
    print(arr)
    print(arr[1])
else:
    print('Нет второго вхождения!')


