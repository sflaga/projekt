import sqlite3

class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, columns):
        # Tworzenie tabeli
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.cursor.execute(query)
        self.connection.commit()

    def insert_record(self, table_name, values):
        # Dodawanie nowego rekordu do tabeli
        query = f"INSERT INTO {table_name} VALUES ({values})"
        self.cursor.execute(query)
        self.connection.commit()

    def update_record(self, table_name, record_id, new_values):
        # Aktualizowanie istniejącego rekordu w tabeli
        query = f"UPDATE {table_name} SET {new_values} WHERE id = {record_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_record(self, table_name, record_id):
        # Usuwanie rekordu z tabeli
        query = f"DELETE FROM {table_name} WHERE id = {record_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_records(self, table_name):
        # Pobieranie wszystkich rekordów z tabeli
        query = f"SELECT * FROM {table_name}"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        return records

    def search_records(self, table_name, condition):
        # Wyszukiwanie rekordów spełniających określone warunki
        query = f"SELECT * FROM {table_name} WHERE {condition}"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        return records

    def close(self):
        # Zamknięcie połączenia z bazą danych
        self.connection.close()

