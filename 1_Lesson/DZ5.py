# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

import math

x_1 = float(input('Введите координату X первой точки: '))
y_1 = float(input('Введите координату Y первой точки: '))
x_2 = float(input('Введите координату X второй точки: '))
y_2 = float(input('Введите координату Y второй точки: '))

long = math.sqrt(((x_2 - x_1)**2) + (y_2 - y_1)**2)
print('Расстояние между точками = ', long)
