import tkinter as tk
from tkinter import messagebox

class GUI:
    def __init__(self, database):
        self.database = database
        self.window = tk.Tk()
        self.window.title("Aplikacja bazodanowa")

        # Tworzenie elementów interfejsu użytkownika
        self.label = tk.Label(self.window, text="Witaj w aplikacji bazodanowej!")
        self.label.pack()

        self.entry = tk.Entry(self.window)
        self.entry.pack()

        self.button = tk.Button(self.window, text="Dodaj rekord", command=self.add_record)
        self.button.pack()

    def add_record(self):
        record = self.entry.get()
        # Wywołanie funkcji obsługi bazy danych
        self.database.add_record(record)
        messagebox.showinfo("Sukces", "Rekord został dodany do bazy danych!")

    def run(self):
        self.window.mainloop()

# Przykładowe użycie klasy GUI
# database = Database()  # Zakładając, że masz zaimplementowaną klasę obsługującą bazę danych
# gui = GUI(database)
# gui.run()

