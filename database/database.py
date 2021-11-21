import sqlite3


class Database:
    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def create_table(self, sql: str):
        self.cursor.execute(sql)
        self.connection.commit()

    def insert__to_db(self, table, *values):
        self.cursor.execute(f"INSERT INTO {table} VALUES ({', '.join('?' for _ in values)})", values)
        self.connection.commit()

    def fetch_all(self, table, **conditions):
        if conditions.items() != 0:
            return self.cursor.execute(
                f"SELECT * FROM {table} WHERE {' and '.join([f'{condition}=?' for condition in conditions])}",
                tuple(conditions.values())
            )
        else:
            return self.cursor.execute(f"SELECT * FROM {table} ")

    def __del__(self):
        self.connection.close()
