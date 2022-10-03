
import SQL
import sqlite3 as sql

while(True):

    con = sql.connect('test.db')
    cur = con.cursor()
    SQL.Data_Base(con, cur)
    con.commit()
    cur.close()
