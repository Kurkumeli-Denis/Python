# Вывести числа от -N до N  


N = int(input('Введите N: '))
new_list = []

for i in range(-N,N+1):
    new_list.append(i)

print(new_list)