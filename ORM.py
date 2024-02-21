import sqlite3

class ORM:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        columns_str = ', '.join(columns)
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})"
        self.cursor.execute(query)

    def select(self, table_name, columns='*', condition=None):
        query = f"SELECT {columns} FROM {table_name}"
        if condition:
            query += f" WHERE {condition}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def insert(self, table_name, values):
        placeholders = ', '.join(['?' for _ in values])
        query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        self.cursor.execute(query, values)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()

# Example usage
db = ORM('mydatabase.db')

# Create a table
db.create_table('users', ['id INTEGER PRIMARY KEY', 'name VARCHAR(50)', 'age INT'])

# Insert a record
db.insert('users', [1, 'John Doe', 25])

# Select all records from the table
result = db.select('users')
print(result)

# Select records with a condition
# result = db.select('users', condition='age > 20')
# print(result)
