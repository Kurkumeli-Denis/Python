import os

while True:
    print('Напиши \"показать\" или \"записать\" или \"удалить\" или \"редактировать\" заметку!')
    answer=input()
    if answer=='показать':
        i=1
        with open("Note.txt") as file:
            for item in file:
                print(f'{i}.',item)
                i+=1
    elif answer=='записать':
        with open("Note.txt",'a') as file:
                print("Что хотите внести в заметки?")
                Note=str(input())+"\n"
                file.write(Note)
    elif answer=='удалить':
        list=[]
        with open("Note.txt") as file:
            i = 1
            print("Выберите номер строки:")
            for item in file:
                print(f'{i}.',item)
                list.append(item)
                i+=1
        try:
            number=int(input())
        except:
            print('Попробуйте все заново')
        list.pop(number-1)
        os.remove('Note.txt')
        with open("Note.txt", 'a') as file:
            for i in list:
                file.write(str(i))
    elif answer=='редактировать':
        list=[]
        with open("Note.txt") as file:
            i = 1
            print("Выберите номер строки:")
            for item in file:
                print(f'{i}.',item)
                list.append(item)
                i+=1
        try:
            number=int(input())
        except:
            print('Попробуйте все заново')
        os.remove('Note.txt')
        print('Как изменить данную заметку?')
        Note=input()+'\n'
        list=list[:number-1]+[Note]+list[number:]
        with open("Note.txt", 'a') as file:
            for i in list:
                file.write(str(i))
    else:
        break