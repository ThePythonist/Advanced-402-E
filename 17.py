import sqlite3

con = sqlite3.connect('info.db')
cur = con.cursor()


def select1():
    cur.execute("SELECT * FROM customers;")
    records = cur.fetchall()

    for i in records:
        print(i[2])


def select2():
    cur.execute("SELECT name,phone FROM customers;")
    records = cur.fetchall()

    for i in records:
        print(i[0],i[1])

select2()

con.commit()
con.close()
print("Done")
