#Test dodawania rekordu
import sqlite3

# Utworzenie połączenia z bazą danych
conn = sqlite3.connect('baza_danych.db')
c = conn.cursor()

# Dodanie nowego rekordu do tabela1
c.execute("INSERT INTO tabela1 (nazwa, cena) VALUES ('Nowy produkt', 25.99)")
conn.commit()

# Sprawdzenie czy rekord został dodany
c.execute("SELECT * FROM tabela1 WHERE nazwa='Nowy produkt' AND cena=25.99")
record_exists = c.fetchone() is not None
assert record_exists, "Nowy rekord nie został dodany do tabela1."

conn.close()
