import sqlite3

con = sqlite3.connect('mydatabase.db')

def sql_fetch(con):

    cursorObj = con.cursor()

    cursorObj.execute('SELECT * FROM employees')

    rows = cursorObj.fetchall()

    for row in rows:

        print(row)

sql_fetch(con)