import tkinter as tk
import sqlite3

# Połączenie z bazą danych
conn = sqlite3.connect("baza_danych.db")
cursor = conn.cursor()


class SklepRowerowy:
    def __init__(self, master):
        self.master = master
        self.master.title("Sklep rowerowy")
        self.master.geometry("400x300")

        # Ustawienie koloru tła
        self.master.configure(bg="lightgray")

        # Przyciski do wyświetlania danych
        ramy_button = tk.Button(
            self.master,
            text="Wyświetl Ramy",
            command=self.wyswietl_ramy,
            bg="blue",
            fg="white",
        )
        ramy_button.pack(pady=10)

        kola_button = tk.Button(
            self.master,
            text="Wyświetl Koła",
            command=self.wyswietl_kola,
            bg="green",
            fg="white",
        )
        kola_button.pack(pady=10)

        akcesoria_button = tk.Button(
            self.master,
            text="Wyświetl Akcesoria",
            command=self.wyswietl_akcesoria,
            bg="orange",
            fg="white",
        )
        akcesoria_button.pack(pady=10)

        czesci_button = tk.Button(
            self.master,
            text="Wyświetl Części",
            command=self.wyswietl_czesci,
            bg="purple",
            fg="white",
        )
        czesci_button.pack(pady=10)

        # Przycisk do usuwania pozycji
        usun_button = tk.Button(
            self.master,
            text="Usuń pozycję",
            command=self.usun_pozycje,
            bg="red",
            fg="white",
        )
        usun_button.pack(pady=10)

    def wyswietl_ramy(self):
        # Utworzenie nowego okna dla kategorii "Ramy"
        okno_ramy = tk.Toplevel(self.master)
        okno_ramy.title("Ramy")
        okno_ramy.geometry("400x300")

        # Ustawienie koloru tła
        okno_ramy.configure(bg="lightblue")

        # Pobranie danych z tabeli "ramy"
        cursor.execute("SELECT * FROM ramy")
        dane = cursor.fetchall()

        # Wyświetlenie danych w listboxie
        listbox = tk.Listbox(okno_ramy)
        listbox.pack(side="left", fill="both", expand=True)

        # Dodanie pasku przewijania dla listboxa
        scrollbar = tk.Scrollbar(okno_ramy)
        scrollbar.pack(side="right", fill="y")

        # Przypisanie paska przewijania do listboxa
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)

        # Wyświetlenie danych w listboxie
        for rama in dane:
            listbox.insert("end", rama)

    def wyswietl_kola(self):
        # Utworzenie nowego okna dla kategorii "Koła"
        okno_kola =
