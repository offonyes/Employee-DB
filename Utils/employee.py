import sqlite3

conn = sqlite3.connect('employee.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS employee(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, surname TEXT, "
          "age INTEGER)")


class Employee(object):
    def __init__(self, name, surname, age, id=None):
        self.id = id
        self.name = name
        self.surname = surname
        self.age = age

    @classmethod
    def get(cls, employee_id):
        result = c.execute("SELECT * FROM employee WHERE id = ?", (employee_id,))
        values = result.fetchone()
        if values is None:
            return None
        employee = Employee(values["name"], values["surname"], values["age"], values["id"])
        return employee

    @classmethod
    def get_list(cls, **kwargs):
        query = "SELECT * FROM employee WHERE "
        conditions = []
        values = []
        for key, value in kwargs.items():
            conditions.append(f"{key} = ?")
            values.append(value)
        query += " AND ".join(conditions)
        result = c.execute(query, tuple(values))
        employees = []
        for row in result:
            employee = Employee(row["name"], row["surname"], row["age"], row["id"])
            employees.append(employee)
        return employees

    def __repr__(self):
        return f"<Employee {self.name}>"

    def update(self):
        c.execute("UPDATE employee SET name = ?, surname = ?, age = ? WHERE id = ?",
                  (self.name, self.surname, self.age, self.id))

    def create(self):
        c.execute("INSERT INTO employee (name, surname, age) VALUES (?, ?, ?)", (self.name, self.surname, self.age))
        self.id = c.lastrowid

    def save(self):
        if self.id is not None:
            self.update()
        else:
            self.create()
        return self

    def delete(self):
        c.execute("DELETE FROM employee WHERE id = ?", (self.id,))
        conn.commit()

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __eq__(self, other):
        return self.age == other.age

    def __ne__(self, other):
        return self.age != other.age

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age
