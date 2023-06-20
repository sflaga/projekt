#Test tworzenia tabel
import sqlite3

# Utworzenie połączenia z bazą danych
conn = sqlite3.connect('baza_danych.db')
c = conn.cursor()

# Sprawdzenie czy tabela1 została utworzona
c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tabela1'")
table_exists = c.fetchone() is not None
assert table_exists, "Tabela tabela1 nie została utworzona."

# Sprawdzenie czy tabela2 została utworzona
c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tabela2'")
table_exists = c.fetchone() is not None
assert table_exists, "Tabela tabela2 nie została utworzona."

# Sprawdzenie czy tabela3 została utworzona
c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tabela3'")
table_exists = c.fetchone() is not None
assert table_exists, "Tabela tabela3 nie została utworzona."

# Sprawdzenie czy tabela4 została utworzona
c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tabela4'")
table_exists = c.fetchone() is not None
assert table_exists, "Tabela tabela4 nie została utworzona."
conn.close()
