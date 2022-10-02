from cgi import test
from csv import writer
import csv
from importlib.resources import path
import sqlite3 as sql
import json

import user_input
import controller



def Data_Base():
    
    
    con = sql.connect('test.db')
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS `test` (`user_id` INTEGER, `name` STRING, `surname` STRING, `tel` STRING)")

        user_choice = user_input.menu()
        if user_choice == '1':
            controller.Add_contact()
        elif user_choice == '2':
            controller.Find_contact()
        elif user_choice == '3':
            controller.Delete_contact()
        elif user_choice == '4':
            controller.Show_all()
        elif user_choice == '5':
            controller.Export_CSV()
        elif user_choice == '6':
            controller.Export_JSON()


        con.commit()
        cur.close()