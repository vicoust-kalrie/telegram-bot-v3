import sqlite3

conn = sqlite3.connect("portfolio.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM portfolio")

data = cursor.fetchall()

for row in data:
    print(row)

conn.close()
