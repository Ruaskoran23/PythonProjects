#working with databases
#03-03-2024

import sqlite3

#creation of a connection

conn = sqlite3.connect('emaildb.sqlite') #emaildb is created when this line runs

chandle = conn.cursor()    #cursor is like a file handle

chandle.execute('''
DROP TABLE IF EXISTS Counts''') #execute runs the SQL commands

chandle.execute('''
CREATE TABLE Counts(email TEXT, count INTEGER)''') #creates a table with columns

fname = input('Enter the name of the file:')
fhandle = open(fname)
for line in fhandle:
    if not line.startswith('From: '): continue
    words = line.split()
    email = words[1]
    chandle.execute('SELECT count FROM Counts WHERE email = ?', (email,))
    # ? is a place holder and (email,) is a tuple
    row = chandle.fetchone() #grabs the first one and insert into row
    if row is None:
        chandle.execute('''INSERT INTO Counts(email, count)
                    VALUES(?, 1)''', (email,))
    else:
        chandle.execute('UPDATE Counts SET count = count +1 WHERE email =?', (email,))
    conn.commit()

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in chandle.execute(sqlstr):
    print(str(row[0]), row[1])

chandle.close




