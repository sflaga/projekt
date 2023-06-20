import sqlite3
from tkinter import *
import csv

# Funkcje obsługujące operacje na bazie danych

def dodaj_rekord():
    # Pobranie danych z pól tekstowych
    id = int(id_entry.get())
    nazwa = nazwa_entry.get()
    cena = float(cena_entry.get())
    
    # Utworzenie połączenia z bazą danych
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    
    # Dodanie nowego rekordu do tabeli1
    c.execute("INSERT INTO tabela1 (id, nazwa, cena) VALUES (?, ?, ?)", (id, nazwa, cena))
    
    # Zatwierdzenie zmian i zamknięcie połączenia
    conn.commit()
    conn.close()

def usun_rekord():
    # Pobranie ID rekordu do usunięcia
    id = int(id_entry.get())
    
    # Utworzenie połączenia z bazą danych
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    
    # Usunięcie rekordu o podanym ID z tabeli1
    c.execute("DELETE FROM tabela1 WHERE id=?", (id,))
    
    # Zatwierdzenie zmian i zamknięcie połączenia
    conn.commit()
    conn.close()

def edytuj_rekord():
    # Pobranie danych z pól tekstowych
    id = int(id_entry.get())
    nazwa = nazwa_entry.get()
    cena = float(cena_entry.get())
    
    # Utworzenie połączenia z bazą danych
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    
    # Edycja rekordu o podanym ID w tabeli1
    c.execute("UPDATE tabela1 SET nazwa=?, cena=? WHERE id=?", (nazwa, cena, id))
    
    # Zatwierdzenie zmian i zamknięcie połączenia
    conn.commit()
    conn.close()

def wyswietl_rekordy():
    # Utworzenie połączenia z bazą danych
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    
    # Pobranie wszystkich rekordów z tabeli1
    c.execute("SELECT * FROM tabela1")
    rekordy = c.fetchall()
    
    # Wyświetlenie rekordów w oknie
    for rekord in rekordy:
        print(rekord)
    
    # Zamknięcie połączenia
    conn.close()

def wyszukaj_rekordy():
    # Pobranie nazwy do wyszukania
    nazwa = nazwa_entry.get()
    
    # Utworzenie połączenia z bazą danych
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    
    # Wyszukanie rekordów o podanej nazwie w tabeli1
    c.execute("SELECT * FROM tabela1 WHERE nazwa=?", (nazwa,))
    rekordy = c.fetchall()
    
    # Wyświetlenie rekordów w oknie
    for rekord in rekordy:
        print(rekord)
    
    # Zamknięcie połączenia
    conn.close()

def sortuj_rekordy():
    # Utworzenie połączenia z bazą danych
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    
    # Posortowanie rekordów w tabeli1 po cenie (rosnąco)
    c.execute("SELECT * FROM tabela1 ORDER BY cena ASC")
    rekordy = c.fetchall()
    
    # Wyświetlenie rekordów w oknie
    for rekord in rekordy:
        print(rekord)
    
    # Zamknięcie połączenia
    conn.close()

def filtrowanie_rekordy():
    # Utworzenie połączenia z bazą danych
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    
    # Filtrowanie rekordów w tabeli1 po cenie większej niż 15.00
    c.execute("SELECT * FROM tabela1 WHERE cena > 15.00")
    rekordy = c.fetchall()
    
    # Wyświetlenie rekordów w oknie
    for rekord in rekordy:
        print(rekord)
    
    # Zamknięcie połączenia
    conn.close()

def eksportuj_do_csv():
    # Utworzenie połączenia z bazą danych
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    
    # Pobranie wszystkich rekordów z tabeli1
    c.execute("SELECT * FROM tabela1")
    rekordy = c.fetchall()
    
    # Zapisanie rekordów do pliku CSV
    with open('rekordy.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'Nazwa', 'Cena'])
        writer.writerows(rekordy)
    
    # Zamknięcie połączenia
    conn.close()

def importuj_z_csv():
    # Odczytanie rekordów z pliku CSV
    rekordy = []
    with open('rekordy.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Pominięcie nagłówka
        for row in reader:
            rekordy.append(row)
    
    # Utworzenie połączenia z bazą danych
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    
    # Wyczyszczenie tabeli1
    c.execute("DELETE FROM tabela1")
    
    # Dodanie rekordów z pliku CSV do tabeli1
    c.executemany("INSERT INTO tabela1 (id, nazwa, cena) VALUES (?, ?, ?)", rekordy)
    
    # Zatwierdzenie zmian i zamknięcie połączenia
    conn.commit()
    conn.close()

# Utworzenie okna aplikacji
root = Tk()

# Tworzenie etykiet i pól tekstowych
Label(root, text="ID:").grid(row=0, column=0)
id_entry = Entry(root)
id_entry.grid(row=0, column=1)

Label(root, text="Nazwa:").grid(row=1, column=0)
nazwa_entry = Entry(root)
nazwa_entry.grid(row=1, column=1)

Label(root, text="Cena:").grid(row=2, column=0)
cena_entry = Entry(root)
cena_entry.grid(row=2, column=1)

# Tworzenie przycisków
Button(root, text="Dodaj rekord", command=dodaj_rekord).grid(row=3, column=0)
Button(root, text="Usuń rekord", command=usun_rekord).grid(row=3, column=1)
Button(root, text="Edytuj rekord", command=edytuj_rekord).grid(row=4, column=0)
Button(root, text="Wyświetl rekordy", command=wyswietl_rekordy).grid(row=4, column=1)
Button(root, text="Wyszukaj rekordy", command=wyszukaj_rekordy).grid(row=5, column=0)
Button(root, text="Sortuj rekordy", command=sortuj_rekordy).grid(row=5, column=1)
Button(root, text="Filtrowanie rekordy", command=filtrowanie_rekordy).grid(row=6, column=0)
Button(root, text="Eksportuj do CSV", command=eksportuj_do_csv).grid(row=6, column=1)
Button(root, text="Importuj z CSV", command=importuj_z_csv).grid(row=7, column=0)

# Uruchomienie głównej pętli aplikacji
root.mainloop()
