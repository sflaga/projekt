#Test usuwania rekordu
import sqlite3
from tkinter import *

# Funkcja usuwająca rekord z bazy danych
def usun_rekord():
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    c.execute("DELETE FROM tabela1 WHERE nazwa=?", (pole1.get(),))
    conn.commit()
    conn.close()

# Test usuwania rekordu
def test_usuwania_rekordu():
    pole1.insert(0, "Nazwa produktu do usunięcia")
    usun_rekord()
    wyswietl_rekordy()

# Tworzenie interfejsu użytkownika przy użyciu biblioteki Tkinter
root = Tk()

pole1 = Entry(root)
pole1.pack()

przycisk_usun = Button(root, text="Usuń rekord", command=test_usuwania_rekordu)
przycisk_usun.pack()

root.mainloop()
