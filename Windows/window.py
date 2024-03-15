from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from .MainWindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

class EmployeeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Employee Management System')
        self.setGeometry(100, 100, 600, 400)

        self.init_ui()
        self.load_data()

    def init_ui(self):
        self.name_input = QLineEdit()
        self.surname_input = QLineEdit()
        self.age_input = QLineEdit()

        self.add_button = QPushButton('Add Employee')
        self.add_button.clicked.connect(self.add_employee)

        self.table = QTableView()

        self.delete_button = QPushButton('Delete Employee')
        self.delete_button.clicked.connect(self.delete_employee)

        self.refresh_button = QPushButton('Refresh')
        self.refresh_button.clicked.connect(self.load_data)

        self.search_button = QPushButton('Search')
        self.search_button.clicked.connect(self.search_employee)

        input_layout = QVBoxLayout()
        input_layout.addWidget(QLabel('Name:'))
        input_layout.addWidget(self.name_input)
        input_layout.addWidget(QLabel('Surname:'))
        input_layout.addWidget(self.surname_input)
        input_layout.addWidget(QLabel('Age:'))
        input_layout.addWidget(self.age_input)
        input_layout.addWidget(self.add_button)

        table_layout = QVBoxLayout()
        table_layout.addWidget(self.table)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.refresh_button)
        button_layout.addWidget(self.search_button)

        main_layout = QHBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addLayout(table_layout)

        layout = QVBoxLayout()
        layout.addLayout(main_layout)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def load_data(self):
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['ID', 'Name', 'Surname', 'Age'])

        conn = sqlite3.connect('employee.db')
        c = conn.cursor()
        c.execute("SELECT * FROM employee")
        data = c.fetchall()
        for row in data:
            self.model.appendRow([
                QStandardItem(str(row[0])),
                QStandardItem(row[1]),
                QStandardItem(row[2]),
                QStandardItem(str(row[3]))
            ])
        self.table.setModel(self.model)

    def add_employee(self):
        name = self.name_input.text()
        surname = self.surname_input.text()
        age = self.age_input.text()

        if name and surname and age:
            conn = sqlite3.connect('employee.db')
            c = conn.cursor()
            c.execute("INSERT INTO employee (name, surname, age) VALUES (?, ?, ?)", (name, surname, age))
            conn.commit()
            conn.close()
            self.load_data()
        else:
            QMessageBox.warning(self, 'Warning', 'Please fill in all fields.')

    def delete_employee(self):
        selected_index = self.table.selectedIndexes()
        if selected_index:
            row = selected_index[0].row()
            employee_id = self.model.item(row, 0).text()
            conn = sqlite3.connect('employee.db')
            c = conn.cursor()
            c.execute("DELETE FROM employee WHERE id=?", (employee_id,))
            conn.commit()
            conn.close()
            self.load_data()
        else:
            QMessageBox.warning(self, 'Warning', 'Please select an employee to delete.')

    def search_employee(self):
        name = self.name_input.text()
        surname = self.surname_input.text()
        age = self.age_input.text()

        conn = sqlite3.connect('employee.db')
        c = conn.cursor()

        query = "SELECT * FROM employee WHERE "
        conditions = []
        values = []

        if name:
            conditions.append("name = ?")
            values.append(name)
        if surname:
            conditions.append("surname = ?")
            values.append(surname)
        if age:
            conditions.append("age = ?")
            values.append(age)

        query += " AND ".join(conditions)

        result = c.execute(query, tuple(values))
        data = result.fetchall()

        self.model.clear()
        self.model.setHorizontalHeaderLabels(['ID', 'Name', 'Surname', 'Age'])
        for row in data:
            self.model.appendRow([
                QStandardItem(str(row[0])),
                QStandardItem(row[1]),
                QStandardItem(row[2]),
                QStandardItem(str(row[3]))
            ])
        self.table.setModel(self.model)