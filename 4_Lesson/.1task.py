# большее и меньшее число в строке


arr = input("Введите числа через пробел: ").split()
mass = []

for i in range (len(arr)):
    mass.append(int(arr[i]))
minn = mass[0]
maxx = mass[0]

for i in range (len(mass)):
    if (mass[i] > maxx):
        maxx = mass[i]
    if (mass[i]< minn):
        minn = mass[i]

print("MAX =", maxx)
print("MIN =", minn)

