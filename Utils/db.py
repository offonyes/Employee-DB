import sqlite3
import json


def regions():
    with open("Data\\data.json", "r") as f:
        data = json.load(f)
    return list(data.keys())


class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path

    def create_table(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS employee (
                               id INTEGER PRIMARY KEY AUTOINCREMENT, 
                               name TEXT, 
                               surname TEXT,
                               age INTEGER
                           )""")
            conn.commit()

    def load_column(self, column):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT {column} FROM employee")
            return [str(row[0]) for row in cursor.fetchall()]

    def add_data(self, name, surname, age):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO employee (name, surname, age) VALUES (?, ?, ?)", (name, surname, age))
            conn.commit()

    def load_data(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM employee")
            return cursor.fetchall()

    def delete_row(self, row_id):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM employee WHERE id = ?", (row_id,))
            conn.commit()

    def search(self, name=None, surname=None, age=None, id=None):
        conditions = []
        values = ()
        if id:
            conditions.append("id LIKE ?")
            values += ('%' + id + '%',)
        if name:
            conditions.append("name LIKE ?")
            values += ('%' + name + '%',)
        if surname:
            conditions.append("surname LIKE ?")
            values += ('%' + surname + '%',)
        if age:
            conditions.append("age LIKE ?")
            values += ('%' + age + '%',)

        if conditions:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                query = "SELECT * FROM employee WHERE " + " AND ".join(conditions)
                cursor.execute(query, values)
                return cursor.fetchall()
        else:
            return self.load_data()

    def update(self, name, surname, age, id):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE employee SET name = ?, surname = ?, age = ? WHERE id = ?", (name, surname, age, id))
            conn.commit()

    def most_common(self, value):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT {value}, COUNT(*) AS count FROM employee GROUP BY {value} ORDER BY count DESC")
            return cursor.fetchone()

    def least_common(self, value):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT {value}, COUNT(*) AS count FROM employee GROUP BY {value} ORDER BY count ASC")
            return cursor.fetchone()

    def average_age(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT AVG(age) FROM employee")
            return cursor.fetchone()[0]

    def same_name_surname_age(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM employee WHERE (name, surname, age) IN (SELECT name, surname, age FROM employee GROUP "
                "BY name, surname, age HAVING COUNT(*) > 1)")
            return cursor.fetchall()
        
    def check_bd(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM employee")
            data = cursor.fetchall()
        return True if not data else False
