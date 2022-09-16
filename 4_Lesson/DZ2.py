# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

x = int(input("Введите число: "))
dell = 2
mass = []
while (x != 1):
    if (x % dell == 0):
        mass.append(str(dell))
        x = x / dell
    else:
        dell = dell + 1

print(mass)
