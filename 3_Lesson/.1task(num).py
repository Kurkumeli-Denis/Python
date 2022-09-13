#  находит в списке строк, строку где есть заданное число



mass = []
mass = input('Введите строки через пробел: ').split()
x = (input('Введите искомое число: '))
print(mass)
i = -1

while(i < (len(mass) - 1)):
    i += 1
    arr = []
    arr = mass[i]
    j = 0
    while(j < (len(arr))):
       
        if ((list(arr)[j]) != x):
            j += 1
           
        else:
            print(arr)
            break


   

    