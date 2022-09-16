# Наименьшее общее кратное

x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))

m = max(x,y)

while (True):
    if m%x==0 and m%y==0:
        print("Наименьшее общее кратное: ",m)
        break
    else:
        m+=1   

with open ('file.txt', 'a') as f:
    f.write(str(m))