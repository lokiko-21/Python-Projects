#I will be using the sqlite3 module for this project
import sqlite3

#creating a list of files as a tuple. NOT AS ACTUAL FILES
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

#creating and connecting variable to database1.db
conn = sqlite3.connect('database1.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_fileName TEXT \
                )")
    conn.commit()
conn.close()

#this will add file to database if it contains .txt extension

#iterates through fileList
for i in fileList:
    #searches for .txt extension in files
    if ".txt" in i:
        fileName = i
        #connects to database1.db
        conn = sqlite3.connect('database1.db')
        with conn:
            cur = conn.cursor()
            #inserts i value(file containing .txt extension) into col_fileName
            #DON'T FORGET TO ADD THE COMMA!
            cur.execute("INSERT INTO tbl_files(col_fileName) VALUES (?)", \
                        (fileName,))
            conn.commit()
        conn.close()

