# Вывод первой цифры дробной части числа





num_list = input('Введите дробное число: ')
count = 1

for i in range(len(num_list)):
    if (num_list[i] == ','):
        print(num_list[i+1]) 
        break
    count = count + 1
    if (count == len(num_list)):
       print ('Число не дробное')





