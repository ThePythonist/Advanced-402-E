import sqlite3

con = sqlite3.connect('info.db')
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS customers (name, city, phone);")
cur.execute("INSERT INTO customers VALUES ('Mohsen','Tehran','09334438725');")
cur.execute("INSERT INTO customers VALUES ('Sara','Yazd','09213378325');")
cur.execute("INSERT INTO customers VALUES ('Ali','Sari','09213378325');")
cur.execute("INSERT INTO customers VALUES ('Ghazal','Shiraz','09213378325');")

con.commit()
con.close()
print("Done")