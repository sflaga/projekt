import sqlite3

class Database:
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS czesci (
            id INTEGER PRIMARY KEY,
            nazwa TEXT,
            producent TEXT,
            cena REAL,
            ilosc INTEGER
        )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS ramy (
            id INTEGER PRIMARY KEY,
            nazwa TEXT,
            producent TEXT,
            material TEXT,
            cena REAL
        )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS kola (
            id INTEGER PRIMARY KEY,
            nazwa TEXT,
            producent TEXT,
            rozmiar INTEGER,
            cena REAL
        )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS akcesoria (
            id INTEGER PRIMARY KEY,
            nazwa TEXT,
            producent TEXT,
            cena REAL,
            ilosc INTEGER
        )''')

    def insert_czesc(self, data):
        self.cursor.execute('INSERT INTO czesci VALUES (?, ?, ?, ?, ?)', data)
        self.connection.commit()

    def insert_rama(self, data):
        self.cursor.execute('INSERT INTO ramy VALUES (?, ?, ?, ?, ?)', data)
        self.connection.commit()

    def insert_kolo(self, data):
        self.cursor.execute('INSERT INTO kola VALUES (?, ?, ?, ?, ?)', data)
        self.connection.commit()

    def insert_akcesorium(self, data):
        self.cursor.execute('INSERT INTO akcesoria VALUES (?, ?, ?, ?, ?)', data)
        self.connection.commit()

    def delete_czesc(self, czesc_id):
        self.cursor.execute('DELETE FROM czesci WHERE id = ?', (czesc_id,))
        self.connection.commit()

    def delete_rama(self, rama_id):
        self.cursor.execute('DELETE FROM ramy WHERE id = ?', (rama_id,))
        self.connection.commit()

    def delete_kolo(self, kolo_id):
        self.cursor.execute('DELETE FROM kola WHERE id = ?', (kolo_id,))
        self.connection.commit()

    def delete_akcesorium(self, akcesorium_id):
        self.cursor.execute('DELETE FROM akcesoria WHERE id = ?', (akcesorium_id,))
        self.connection.commit()

    def close(self):
        self.connection.close()


# Utwórz instancję klasy Database
database = Database('baza_danych.db')

# Utwórz tabele
database.create_tables()

# Dodaj dane do tabeli "czesci"
dane_czesci = [
    (1, 'Opona', 'Schwalbe', 50.00, 10),
    (2, 'Siodełko', 'Brooks', 100.00, 5),
    (3, 'Kierownica', 'Ritchey', 80.00, 8),
    (4, 'Przerzutka', 'Shimano', 120.00, 4),
    (5, 'Hamulce', 'Magura', 150.00, 6)
]
for czesc in dane_czesci:
    database.insert_czesc(czesc)

# Usuń pozycję z tabeli "czesci" o ID równym 3
database.delete_czesc(3)

# Dodaj dane do tabeli "ramy"
dane_ramy = [
    (1, 'Rama MTB', 'Trek', 'Aluminiowa', 500.00),
    (2, 'Rama szosowa', 'Specialized', 'Węglowa', 1000.00),
    (3, 'Rama miejska', 'Giant', 'Stalowa', 300.00),
    (4, 'Rama BMX', 'Redline', 'Aluminiowa', 400.00),
    (5, 'Rama trekkingowa', 'Scott', 'Aluminiowa', 600.00)
]
for rama in dane_ramy:
    database.insert_rama(rama)

# Usuń pozycję z tabeli "ramy" o ID równym 4
database.delete_rama(4)

# Dodaj dane do tabeli "kola"
dane_kola = [
    (1, 'Koło MTB', 'Mavic', 26, 200.00),
    (2, 'Koło szosowe', 'Zipp', 700, 800.00),
    (3, 'Koło miejskie', 'Shimano', 28, 100.00),
    (4, 'Koło BMX', 'Odyssey', 20, 150.00),
    (5, 'Koło trekkingowe', 'Alexrims', 28, 180.00)
]
for kolo in dane_kola:
    database.insert_kolo(kolo)

# Usuń pozycję z tabeli "kola" o ID równym 2
database.delete_kolo(2)

# Dodaj dane do tabeli "akcesoria"
dane_akcesoria = [
    (1, 'Licznik rowerowy', 'Cateye', 30.00, 7),
    (2, 'Bidon', 'Elite', 10.00, 10),
    (3, 'Lampa przednia', 'Knog', 40.00, 6),
    (4, 'Zapięcie rowerowe', 'Abus', 20.00, 8),
    (5, 'Kask', 'Giro', 100.00, 4)
]
for akcesorium in dane_akcesoria:
    database.insert_akcesorium(akcesorium)

# Usuń pozycję z tabeli "akcesoria" o ID równym 5
database.delete_akcesorium(5)

# Zamknij połączenie z bazą danych
database.close()
