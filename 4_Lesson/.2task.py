# найти корни квадратного уравнения A(x)^2 + Bx + C = 0

# a = int(input("Введите A: "))
# b = int(input("Введите B: "))
# c = int(input("Введите C: "))

# d = (b**2) - (4 * a * c)
# if (d < 0):
#     print()
#     print("НЕТ КОРНЕЙ")
# else:
#     x1 = (-b + (d ** 0.5))/2
#     x2 = (-b - (d ** 0.5))/2
#     print()
#     print("Первый корень: ", x1)
#     print("Второй корень: ", x2)

    
import cmath
  
a = int(input("Введите A: "))
b = int(input("Введите B: "))
c = int(input("Введите C: "))
  

d = (b**2) - (4 * a*c)

if (d < 0):
    print()
    print("НЕТ КОРНЕЙ")
else:
    x1 = (-b-cmath.sqrt(d))/(2 * a)
    x2 = (-b + cmath.sqrt(d))/(2 * a)
    print()
    print("Первый корень: ", x1)
    print("Второй корень: ", x2)

