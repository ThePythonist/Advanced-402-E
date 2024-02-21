import sqlite3


class ORM:
    def __init__(self):
        self.con = sqlite3.connect("Information.db")
        self.cur = self.con.cursor()

    def create_table(self, table_name):
        columns = tuple(input("Table columns (separate them by comma) : ").split(","))

        query = f"CREATE TABLE IF NOT EXISTS {table_name} {columns};"
        self.cur.execute(query)

        self.con.commit()
        self.con.close()

        print("\n----------Table Created----------\n")

    def insert(self, table_name):
        try:
            command = f"PRAGMA table_info({table_name});"
            self.cur.execute(command)
            columns = self.cur.fetchall()

            values = []
            for i in range(len(columns)):
                entry = input(f"{columns[i][1]} : ")
                values.append(entry)

            command = f"INSERT INTO {table_name} VALUES {tuple(values)};"
            self.cur.execute(command)

            self.con.commit()
            self.con.close()

            print("\n----------Inserted into table----------\n")

        except:
            print("\n----------Table Doesnt Exist----------\n")

    def select(self, table_name):
        try:
            self.cur.execute(f"SELECT * FROM {table_name};")
            result = self.cur.fetchall()
            for i in result:
                print(i)

        except:
            print("\n----------Table Doesnt exist----------\n")

    def main(self):
        operation = input("""
        1 : Create Table
        2 : Insert Record Into Table
        3 : Select Data From Table
        : """)

        if operation == "1":
            table_name = input("Enter table name : ")
            self.create_table(table_name)
        elif operation == "2":
            table_name = input("Enter table name : ")
            self.insert(table_name)
        elif operation == "3":
            table_name = input("Enter table name : ")
            self.select(table_name)


orm_instance = ORM()
orm_instance.main()
