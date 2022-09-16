import re


file=open('DZ4.txt','r')
file1=open('DZ4_2.txt','r')
lst=str(file.read())
lst1=str(file1.read())
print(lst)
print(lst1)
lst = re.findall('[0-9]{1,2}', lst)
lst1 = re.findall('[0-9]{1,2}', lst1)
koef = [lst[i] for i in range(0, len(lst), 2)]
koef1 = [lst1[i] for i in range(0, len(lst1), 2)]
koef.reverse()
koef1.reverse()
sum = []
if len(koef) >= len(koef1):
    for i in range(len(koef1)):
        sum.append(int(koef[i]) + int(koef1[i]))
    if len(koef) > len(koef1):
        for k in range(len(koef) - 1, len(koef1) - 1, -1):
            sum.append(int(koef[k]))
else:
    for i in range(len(koef)):
        sum.append(int(koef[i]) + int(koef1[i]))
    if len(koef1) > len(koef):
        for k in range(len(koef1) - 1, len(koef) - 1, -1):
            sum.append(koef1[k])
file = open('DZ5.txt', 'a')
for i in range(len(sum) - 1, 0, -1):
    file.write(f'{sum[i]}*x^{i}+')
file.write(f'{sum[0]}=0\n')
file = open('DZ5.txt', 'r')
print(file.read())
file.close()


