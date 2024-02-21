import sqlite3
def create_table(table_name):
    con = sqlite3.connect("Information.db")
    cur = con.cursor()

    columns = tuple(input("Table columns (seperate them by comma) : ").split(","))

    query = f"CREATE TABLE IF NOT EXISTS {table_name} {columns};"
    cur.execute(query)

    con.commit()
    con.close()
    main()

def insert(table_name):
    con = sqlite3.connect("Information.db")
    cur = con.cursor()


def select(table_name):
    con = sqlite3.connect("Information.db")
    cur = con.cursor()

    try :

        cur.execute(f"SELECT * FROM {table_name};")
        result = cur.fetchall()
        for i in result:
            print(i)
    except :
        print("Table Doesnt exists")
        main()

def main():
    operation = input("""
1 : Create Table
2 : Insert Record Into Table
3 : Select Data From Table
: """)

    if operation == "1":
        table_name = input("Enter table name : ")
        create_table(table_name)
    elif operation == "2":
        table_name = input("Enter table name : ")
        insert(table_name)
    elif operation == "3":
        table_name = input("Enter table name : ")
        select(table_name)


main()
