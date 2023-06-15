import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL)")

    def insert_record(self, record):
        table_name, values = record
        query = f"INSERT INTO {table_name} VALUES (NULL, {values})"
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()


if __name__ == "__main__":
    database = Database()
