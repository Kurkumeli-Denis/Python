
from logging.config import IDENTIFIER
from traceback import print_tb
import user_input
import SQL
from cgi import test
from csv import writer
import csv
from importlib.resources import path
import sqlite3 as sql
import json



con = sql.connect('test.db')
with con:
    cur = con.cursor()
    

def Add_contact():
    cur.execute("SELECT * FROM test")
    rows = cur.fetchall()
    if(len(rows) == 0):
        res = 0
    else:
        for row in rows:
            res = row[0]

    user_id = res + 1
    name = input("Имя\n> ")
    surname = input("Фамилия\n> ")
    tel = input("Телефон\n> ")
    cur.execute(f"INSERT INTO `test` VALUES ('{user_id}', '{name}', '{surname}', '{tel}')")
    con.commit()


def Find_contact():
    x = input('Введите id, имя, фамилию или телефон: ')
    try:
        cur.execute(f"SELECT * FROM 'test' where user_id Like '{x}' OR name Like '{x}%' OR surname Like '{x}%' OR tel Like '{x}%'")
        result = cur.fetchall()
        print(result)
        
       
    except:
        print("Ошибка при работе с SQLite")
    

def Delete_contact():
    x = input('Введите id, имя, фамилию или телефон: ')
    try:
        cur.execute(f"SELECT * FROM 'test' where user_id Like '{x}' OR name Like '{x}%' OR surname Like '{x}%' OR tel Like '{x}%'")
        rows = cur.fetchall()
        print(rows)
        result = 0
        for row in rows:
            result = row[0]
        
        q = input('Если вы уверены нажмите Y если нет нажмите N: ')
        if q == 'Y':
            cur.execute(f"""DELETE FROM 'test' where user_id Like '{result}'""")
            con.commit()
            print('Запись удалена')
            
        else:
            print('Отмена')
       
    except:
        print("Ошибка при работе с SQLite")
    


def Show_all():
    cur.execute("SELECT * FROM `test`")
    rows = cur.fetchall()
    print(rows)


def Export_CSV():
    cur.execute("SELECT * FROM 'test'")
    DEMO = cur.fetchall()
    path = 'DEMO.csv'
    with open (path, 'w', newline = '') as csvfile: 
        for row in DEMO:
            csv.writer(csvfile).writerow(row)


def Export_JSON():
    cur.execute("SELECT * FROM 'test'")
    DATA = json.dumps(cur.fetchall())
    with open ("DATA.json", 'w') as file:
        file.write(DATA)



