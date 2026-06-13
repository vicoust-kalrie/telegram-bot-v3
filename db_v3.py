import sqlite3

conn = sqlite3.connect("portfolio.db")
cursor = conn.cursor()

print("=== PORTFOLIO ===")

cursor.execute("SELECT * FROM portfolio")

for row in cursor.fetchall():
    print(row)

conn.close()
