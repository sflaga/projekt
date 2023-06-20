#Test wyswietlania rekordow
import sqlite3
from tkinter import *

# Funkcja wyświetlająca rekordy z bazy danych
def wyswietl_rekordy():
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tabela1")
    rekordy = c.fetchall()
    for rekord in rekordy:
        print(rekord)
    conn.close()

# Test wyświetlania rekordów
def test_wyswietlania_rekordow():
    wyswietl_rekordy()

# Tworzenie interfejsu użytkownika przy użyciu biblioteki Tkinter
root = Tk()

przycisk_wyswietl = Button(root, text="Wyświetl rekordy", command=test_wyswietlania_rekordow)
przycisk_wyswietl.pack()

root.mainloop()
