import tkinter as tk
from tkinter import messagebox

class GUI:
    def __init__(self, database):
        self.database = database
        self.window = tk.Tk()
        self.window.title("Aplikacja bazodanowa")

        self.label = tk.Label(self.window, text="Witaj w aplikacji bazodanowej!")
        self.label.pack()

        self.entry = tk.Entry(self.window)
        self.entry.pack()

        self.button = tk.Button(self.window, text="Dodaj rekord", command=self.add_record)
        self.button.pack()

    def add_record(self):
        record = self.entry.get()
        self.database.insert_record(record)
        messagebox.showinfo("Sukces", "Rekord został dodany do bazy danych!")

    def run(self):
        self.window.mainloop()


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
    gui = GUI(database)
    gui.run()
