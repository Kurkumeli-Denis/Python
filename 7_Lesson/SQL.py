from cgi import test
from csv import writer
import csv
from importlib.resources import path
import sqlite3 as sql
import json



def Menu():
    print("1 - добавление\n2 - получение\n3 - экспорт JSON\n4 - экспорт CSV")
    choice = int(input("> "))
    con = sql.connect('test.db')
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS `test` (`name` STRING, `surname` STRING, `tel` STRING)")

        if choice == 1:
            name = input("Имя\n> ")
            surname = input("Фамилия\n> ")
            tel = input("Телефон\n> ")
            cur.execute(f"INSERT INTO `test` VALUES ('{name}', '{surname}', '{tel}')")
        elif choice == 2:
            cur.execute("SELECT * FROM `test`")
            rows = cur.fetchall()
            for row in rows:
                print(row[0], row[1], row[2])
        elif choice == 3:
            cur.execute("SELECT * FROM 'test'")
            DATA = json.dumps(cur.fetchall())
            with open ("DATA.json", 'w') as file:
                file.write(DATA)
        elif choice == 4:
            cur.execute("SELECT * FROM 'test'")
            DEMO = cur.fetchall()
            path = 'DEMO.csv'
            with open (path, 'w', newline = '') as csvfile: 
                for row in DEMO:
                    csv.writer(csvfile).writerow(row)
                
        else:
            print("Вы ошиблись")

        con.commit()
        cur.close()

    

