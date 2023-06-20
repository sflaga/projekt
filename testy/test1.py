import sqlite3
import unittest
from tkinter import *
import csv

# Import kodu, który ma być przetestowany

class TestBazaDanych(unittest.TestCase):
    def setUp(self):
        # Kod wykonywany przed każdym testem
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()

        # Tworzenie tabel i wypełnienie danymi
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tabela1
                                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nazwa TEXT,
                                cena TEXT)''')

        self.cursor.execute("INSERT INTO tabela1 (id, nazwa, cena) VALUES (1, 'Produkt 1', 10.99)")
        self.cursor.execute("INSERT INTO tabela1 (id, nazwa, cena) VALUES (2, 'Produkt 2', 15.99)")
        self.cursor.execute("INSERT INTO tabela1 (id, nazwa, cena) VALUES (3, 'Produkt 3', 20.50)")

        self.conn.commit()

    def tearDown(self):
        # Kod wykonywany po każdym teście
        self.cursor.execute('DROP TABLE tabela1')
        self.conn.close()

    def test_sortuj_rekordy_kategoria(self):
        # Sprawdź sortowanie rekordów według kategorii dla każdej tabeli
        self.cursor.execute("SELECT * FROM tabela1 ORDER BY cena")
        rekordy_tabela1 = self.cursor.fetchall()

        self.cursor.execute("SELECT * FROM tabela2 ORDER BY ilosc")
        rekordy_tabela2 = self.cursor.fetchall()

        self.cursor.execute("SELECT * FROM tabela3 ORDER BY opis")
        rekordy_tabela3 = self.cursor.fetchall()

        self.cursor.execute("SELECT * FROM tabela4 ORDER BY rok")
        rekordy_tabela4 = self.cursor.fetchall()

        # Przykład asercji
        self.assertEqual(rekordy_tabela1, [(1, 'Produkt 1', '10.99'), (2, 'Produkt 2', '15.99'), (3, 'Produkt 3', '20.50')])
        self.assertEqual(rekordy_tabela2, [(1, 'Marka A', '50'), (3, 'Marka C', '75'), (2, 'Marka B', '100')])
        self.assertEqual(rekordy_tabela3, [(1, 'Kategoria A', 'Opis kategorii A'), (2, 'Kategoria B', 'Opis kategorii B'), (3, 'Kategoria C', 'Opis kategorii C')])
        self.assertEqual(rekordy_tabela4, [(1, 'Producent X', '2019'), (2, 'Producent Y', '2020'), (3, 'Producent Z', '2021')])

if __name__ == '__main__':
    unittest.main()
