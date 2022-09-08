# 1 строка - люблю
# 2 строка - лю
# в первой строке вторая строка встречается два раза

a = input('Введите первую строку: ')
b = input('Введите вторую строку: ')
print(len(b))
# print(a.count(b))  

count = 0
for i in range (0, len(a) - len(b) + 1):
    if b == a[i:(i + len(b))]:
        count += 1

print (f"{count} раз")