# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

mass = map(int, input("Введите последовательность: ").split())
arr = set(mass)
print(arr)