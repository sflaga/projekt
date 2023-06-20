#Test dodawania rekordu
import sqlite3
from tkinter import *

# Funkcja dodająca nowy rekord do bazy danych
def dodaj_rekord():
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    c.execute("INSERT INTO tabela1 (nazwa, cena) VALUES (?, ?)", (pole1.get(), pole2.get()))
    conn.commit()
    conn.close()

# Test dodawania rekordu
def test_dodawania_rekordu():
    pole1.insert(0, "Nowy produkt")
    pole2.insert(0, "99.99")
    dodaj_rekord()
    wyswietl_rekordy()

# Tworzenie interfejsu użytkownika przy użyciu biblioteki Tkinter
root = Tk()

pole1 = Entry(root)
pole1.pack()

pole2 = Entry(root)
pole2.pack()

przycisk_dodaj = Button(root, text="Dodaj rekord", command=test_dodawania_rekordu)
przycisk_dodaj.pack()

root.mainloop()
