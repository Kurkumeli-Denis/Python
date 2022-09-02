# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

xyz_list = ['X', 'Y', 'Z']
num_list = []

for i in range(len(xyz_list)):
    num_list.append(float(input('Введите значения: ')))


if (not(num_list[0] or num_list[1] or num_list[2]) == (not (num_list[0]) and not (num_list[1]) and not (num_list[2]))):
    print ('Верно')
else:
    print ('Не верно')

