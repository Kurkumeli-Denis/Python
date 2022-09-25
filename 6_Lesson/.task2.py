

from collections import Counter

x = input('Введите послдовательность чисел через пробел: ').split()
print(x)
print(Counter(x).most_common())
for i in (Counter(x).most_common()):
    if i[1] == 1:
        print(i[0])