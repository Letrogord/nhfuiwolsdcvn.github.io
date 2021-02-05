import sqlite3 as sq

conn = sq.connect('example.db')
c = conn.cursor()

for row in c.execute("SELECT * FROM user"):
    print(row)