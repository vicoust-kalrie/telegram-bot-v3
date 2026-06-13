import sqlite3

conn = sqlite3.connect("portfolio.db")
cursor = conn.cursor()

cursor.execute(
    "UPDATE portfolio SET jumlah = jumlah + 10 WHERE coin = 'XRP'"
)

conn.commit()

print("Berhasil tambah XRP")

conn.close()
