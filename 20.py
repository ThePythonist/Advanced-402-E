import sqlite3


def create_table(table_name):
    con = sqlite3.connect("Information.db")
    cur = con.cursor()

    columns = tuple(input("Table columns (seperate them by comma) : ").split(","))

    query = f"CREATE TABLE IF NOT EXISTS {table_name} {columns};"
    cur.execute(query)

    con.commit()
    con.close()

    print()
    print("----------Table Created----------")
    print()
    main()


def insert(table_name):
    con = sqlite3.connect('information.db')
    cur = con.cursor()

    try:
        command = f"PRAGMA table_info({table_name});"
        cur.execute(command)
        columns = cur.fetchall()
        # print(columns)
        values = []

        for i in range(len(columns)):
            entry = input(f"{columns[i][1]} : ")
            values.append(entry)

        command = f"INSERT INTO {table_name} VALUES {tuple(values)};"
        cur.execute(command)

        con.commit()
        con.close()

        print()
        print("----------Inserted into table----------")

    except:
        print()
        print("----------Table Doesnt Exist----------")

    print()
    main()


def select(table_name):
    con = sqlite3.connect("Information.db")
    cur = con.cursor()

    try:

        cur.execute(f"SELECT * FROM {table_name};")
        result = cur.fetchall()
        for i in result:
            print(i)
    except:
        print()
        print("----------Table Doesnt exists----------")

    print()
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
