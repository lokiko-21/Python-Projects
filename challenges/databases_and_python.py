import sqlite3
from tkinter import *

#CREATING OUR TUPLES
data1 = ("Jean-Baptiste Zorg", "Human", "122")
data2 = ("Korben Dallas", "Meat Popsicle", "100")
data3 = ("Ak'not", "Mangalore", "-5")

#CREATING THE DATABASE database1.db
conn = sqlite3.connect(':memory:')
with conn:
    cur = conn.cursor()
    #CREATING TABLE tbl_Roster WITH COLUMNS: Name, Species, & IQ
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_Roster(\
                Name TEXT, \
                Species TEXT, \
                IQ Text \
                )")
    #INSERTING DATA INTO 1ST ROW
    cur.execute("INSERT INTO tbl_Roster VALUES(?, ?, ?)", data1)
    #INSERTING DATA INTO 2ND ROW
    cur.execute("INSERT INTO tbl_Roster VALUES(?, ?, ?)", data2)
    #INSERTING DATA INTO 3RD ROW
    cur.execute("INSERT INTO tbl_Roster VALUES(?, ?, ?)", data3)
    #UPDATING Korben Dallas' Species TO Human
    cur.execute("UPDATE tbl_Roster SET Species = ? WHERE Name = ?",
                ('Human', 'Korben Dallas'))
    #THIS WILL SELECT Name AND IQ FROM DATABASE WHERE Species IS Human
    cur.execute("SELECT Name, IQ FROM tbl_Roster WHERE Species = 'Human'")
    for row in cur.fetchall():
        print(row)
    conn.commit()
conn.close()
