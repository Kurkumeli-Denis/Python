# Урок 4 задание 3
# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]



mass = input('Введите числа через пробел: ').split()
x = [i for i in mass if mass.count(i) == 1]
print(x)

# from collections import Counter
# x = input('Введите послдовательность чисел через пробел: ').split()
# print(x)
# print(Counter(x).most_common())
# for i in (Counter(x).most_common()):
#     if i[1] == 1:
#         print(i[0])