# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

import random
vibor = input('Введите p если хотите играть против человека, введите b если против бота: ')
allconfet = 221
if (vibor == 'p'):

    x = input('Введите имя 1 игрока: ')
    y = input('Введите имя 2 игрока: ')
    first = random.randint(0,1)
    second = 0
    if (first == 0):
        first = x
        second = y
    else:
        first = y
        second = x

    num = 0
    count = 1
    play = True
    while(play):
        if (count % 2 != 0):
            print('Ход игрока -',first)
            shiiiit = True
            while(shiiiit):
                if(allconfet == 1):
                    print(second,'выиграл!')
                    play = False
                    break
                num = input('Введите сколько конфет: ')
                try:
                    num = int(num)
                except:
                    print('Введите число от 1 до 28!!!!!!!!!!!!!!!!!!!!!!!!!')
                    continue
                if (num < 0 or num > 28):
                    print('ВВЕДИТЕ ЧИСЛО ОТ 1 ДО 28!!!!!!!')
                else:
                    allconfet = allconfet - num
                    if (allconfet < 1):
                        print(second,'выиграл!')
                        play = False
                        break
                    print('Осталось конфет:',allconfet)
                    break
            count += 1
        else:
            print('Ход игрока -',second)                                                              
            shiiiit = True
            while(shiiiit):
                if(allconfet == 1):
                    print(first,'выиграл!')
                    play = False
                    break
                num = input('Введите сколько конфет: ')
                try:
                    num = int(num)
                except:
                    print('Введите число от 1 до 28!!!!!!!!!!!!!!!!!!!!!!!!!')
                    continue
                if (num < 0 or num > 28):
                    print('ВВЕДИТЕ ЧИСЛО ОТ 1 ДО 28!!!!!!!')
                else:
                    allconfet = allconfet - num
                    if (allconfet < 1):
                        print(first,'выиграл!')
                        play = False
                        break
                    print('Осталось конфет:',allconfet)
                    break
            count += 1
else:
    x = 'bot'
    y = input('Введите имя игрока: ')
    first = random.randint(0,1)
    second = 0
    if (first == 0):
        first = x
        second = y
    else:
        first = y
        second = x
    num = 0
    if (first == x):
        count = 0
    else:
        count = 1
    play = True
    while(play):
        if (count % 2 != 0):
            print('Ход игрока -',first)
            shiiiit = True
            while(shiiiit):
                if(allconfet == 1):
                    print(second,'выиграл!')
                    play = False
                    break
                num = input('Введите сколько конфет: ')
                try:
                    num = int(num)
                except:
                    print('Введите число от 1 до 28!!!!!!!!!!!!!!!!!!!!!!!!!')
                    continue
                if (num < 0 or num > 28):
                    print('ВВЕДИТЕ ЧИСЛО ОТ 1 ДО 28!!!!!!!')
                else:
                    allconfet = allconfet - num
                    if (allconfet < 1):
                        print(second,'выиграл!')
                        play = False
                        break
                    print('Осталось конфет:',allconfet)
                    break
            count += 1
        else:
            print('Ход игрока -',x)
            if(allconfet == 1):
                    print(y,'выиграл!')
                    play = False
            if(allconfet > 58):
                num = random.randint(1, 28)
            if(allconfet <= 58 and allconfet >= 30):
                num = allconfet - 30
                if(num == 0):
                    num = 1
            
            if (allconfet < 30):
                num = allconfet - 1
            allconfet = allconfet - num
            count += 1
            print('Бот отнял конфет:', num)
            print('Осталось ковфет:', allconfet)

            