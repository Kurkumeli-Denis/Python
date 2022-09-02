# Кратно ли число 5 и 10 или 15 но не 30

num = int(input('Введите число: '))

if (num % 30 == 0):
    print ('30 - НЕЛЬЗЯ!!!!!')
elif (num % 5 == 0) and (num % 10 == 0) or (num % 15 == 0):
    print ('КРАТНО')
else:
    print ('НЕТ')

 