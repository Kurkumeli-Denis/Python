array = input("Введите числа через пробел: ").split()
arr = list(map(int, array))
maxx = arr[0]
mass = [maxx]
for i in range(1, len(arr)):
    if (arr[i] > maxx):
        maxx = arr[i]
        mass.append(maxx)
print(mass)
