#Test edytowania rekordow
import sqlite3

# Utworzenie połączenia z bazą danych
conn = sqlite3.connect('baza_danych.db')
c = conn.cursor()

# Edycja rekordu w tabela1
c.execute("UPDATE tabela1 SET nazwa='Produkt X', cena=30.0 WHERE id=1")
conn.commit()

# Sprawdzenie czy rekord został zmieniony
c.execute("SELECT * FROM tabela1 WHERE id=1 AND nazwa='Produkt X' AND cena=30.0")
record_exists = c.fetchone() is not None
