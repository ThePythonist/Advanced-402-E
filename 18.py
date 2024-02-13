import sqlite3

con = sqlite3.connect("mydata.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS students(name,major,grade);")

people = [
    {"name":"mahdi","major":"memari dakheli","grade":16},
    {"name":"yasna","major":"eghtesad","grade":17},
    {"name":"milad","major":"computer","grade":16,},
    {"name":"amir","major":"modiriat","grade":20},
    {"name":"sara","major":"modiriat","grade":15.5},
    {"name":"ali","major":"bargh","grade":14},
]

def insert(name,major,grade):
    command = f"INSERT INTO students VALUES {(name,major,grade)};"
    # print(command)
    cur.execute(command)


def select(table):
    command = f"SELECT * FROM {table};"
    cur.execute(command)
    result = cur.fetchall()
    for i in result:
        if i[2] >= 17 :
            print(i)

# for i in people:
#     insert(i["name"],i["major"],i["grade"])

select("students")

con.commit()
con.close()
