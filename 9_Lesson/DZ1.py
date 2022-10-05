# Создайте программу для игры в ""Крестики-нолики"".
import random


mass = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def Otrisovka(mass):
    print(mass[0],'|',mass[1],'|',mass[2])
    print('--|---|--')
    print(mass[3],'|',mass[4],'|',mass[5])
    print('--|---|--')
    print(mass[6],'|',mass[7],'|',mass[8])

def Xod(player):
    shiiiit = True
    while(shiiiit):
        
        num = input('На какую клетку хотите сходить: ')
        try:
            num = int(num)
        except:
            print('Введите число от 1 до 9!!!!!!!!!!!!!!!!!!!!!!!!!')
            continue
        if (num < 1 or num > 9):
            print('ВВЕДИТЕ ЧИСЛО ОТ 1 ДО 9!!!!!!!')
        else:
            if(mass[num -1] == 'X' or mass[num - 1] == 'O'):
                print('Клетка занята!')
            else:
                mass[num - 1] = player
                shiiiit = False
            
   
def Igroki():
    player1 = input('Введите имя первого игрока: ')
    player2 = input('Введите имя второго игрока: ')
    first = random.randint(0,1)
    second = 0
    if (first == 0):
        first = player1
        second = player2
    else:
        first = player2
        second = player1
    print(first,'ходит первый!')
    return(first, second)


def Proverka(mass):
    wincombo = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in wincombo:
        if(mass[i[0]] == mass[i[1]] == mass[i[2]]):
            return(mass[i[0]])
    return(False)


def Main(mass):
    count = 1
    play = True
    player1, player2 = Igroki()
    while(play):
        
        if(count % 2 != 0):
            print('Ходит',player1)
            Otrisovka(mass)
            Xod('X')
            count += 1
        else:
            print('Ходит',player2)
            Otrisovka(mass)
            Xod('O')
            count += 1
        if(count > 4):
            z = Proverka(mass)
            if(z):
                Otrisovka(mass)
                if(z == 'X'):
                    print(player1,'WIN!')
                else:
                    print(player2,'WIN!')
                
                break

        if(count == 10):
            play = False
            print('НИЧЬЯ!')
            Otrisovka(mass)

Main(mass)