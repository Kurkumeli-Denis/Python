# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:

# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random

k=int(input('Введите степень многочлена: '))
file = open('DZ4.txt', 'a')

for i in range(k,0,-1):
        file.write(f'{random.randint(0, 100)}*x^{i}+')
file.write(f'{random.randint(0, 100)}=0\n')
# file.write(f'x^{k}+{random.randint(0, 100)}=0\n')
# file.write(f'{random.randint(0, 100)}*x^{k}=0\n')
file.close()