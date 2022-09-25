# ввести строку 1+2 и посчитать 


import re

exp=input('Введите выражение без пробелов используя цифры и (\'+\', \'-\', \'/\', \'*\'): ')

expression = exp.replace('+',' +')
expression = expression.replace('-',' -')
expression = expression.replace('*',' *')
expression = expression.replace('/',' /')
expression = expression.split()

print(expression)
mass = []
mass.append(re.findall('[0-9]{1,}', exp))

arr = []
for i in range(len(mass[0])):
    arr.append(int(mass[0][i]))
print(arr)

count = 0
for i in expression:
    for j in range(len(i)):
        if (i[j] == '-'):
            arr[count] = (arr[count]) * (-1)


    count += 1
print(arr)
k = 0
for i in range(len(expression)):
    for j in range(len(expression[i])):
        if(expression[i][j] == '/'):
            arr[k - 1] = arr[k - 1] // arr[k]
            arr.pop(k)
            k -= 1
            
    k += 1        
print('String massive -', expression)    
print('Int massive -', arr)

expression_2 = []
for i in range(len(expression)):
    for j in range(len(expression[i])):
        if(expression[i][j] == '/'):
            expression_2.append(i)
print(expression_2)
spisok = []
for i in range(len(expression)):
    for j in range(len(expression_2)):
        if(i != expression[j]) and (i != expression[j]-1):
            spisok.append(expression[i])

print(spisok)
# count = 0
# for i in expression:
#     for j in range(len(i)):
#         if(i[j] == '/'):
#             for k in range (len(arr)):
#                 arr[count] = arr[count ] // arr[count + 1]
#                 arr.pop(count + 1 )
            
#             expression.pop(i+1)
#             i = str(arr[count])

#         print('String massive -', expression)    
#         print('Int massive -', arr) 
              
#     count += 1



# count = 0
# for i in expression:
#     for j in range(len(i)):
#         if (i[j] == '*'):
#             arr[count] = arr[count - 1] * arr[count]
#             arr.pop(count - 1)
#             expression.remove(i)
#             i = str(arr[count-1])
                  
#     count += 1
        
# print(expression)
# print(arr)
