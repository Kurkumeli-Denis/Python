# Перемешать список

# import random
# x = 'fdsfgrgwf'
# print (x)
# print (random.sample(x, len(x)))

# Не знаю как перемешать рандомно без функции рандом(
x = [1, 2, 3, 4, 5]
print(x)
y = []
i = 0
z = len(x)
print(z)
while((z - 1) >= i):
    y.append(x[z - 1])
    z -= 1
print(y)

    

