from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from .MainWindow import Ui_MainWindow
from Utils.db import *
from Utils.utils import Worker


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.worker = None
        self.thread = None
        self.setupUi(self)
        self.choose_1.hide()
        self.choose_2.hide()
        self.init_action()
        self.db = DatabaseManager("Data\\employee.db")
        self.db.create_table()
        self.tableWidget.horizontalHeader().setDisabled(True)
        column_widths = [60, 100, 120, 80]
        for col, width in enumerate(column_widths):
            self.tableWidget.setColumnWidth(col, width)
        self.custom_button.clicked.connect(lambda: self.change_page(self.bd_page))
        self.main_menu_button.clicked.connect(lambda: self.change_page(self.main_page))
        self.region_cb.addItems(regions())
        self.region_cb.setCurrentIndex(23)
        self.generaty_db_button.clicked.connect(
            lambda: self.add_random_data(self.region_cb.currentText(), int(self.amount_spinbox.value())))
        self.add_button.clicked.connect(
            lambda: self.add_one_data(self.name_input.text(), self.surname_input.text(), self.age_input.text()))
        self.search_button.clicked.connect(
            lambda: self.search_info(self.name_input.text(), self.surname_input.text(), self.age_input.text()))
        self.delete_button.clicked.connect(self.delete_data)
        self.generaty_button.clicked.connect(lambda: self.action(self.action_cb.currentText()))
        self.save_new.clicked.connect(self.save)
        self.action_cb.currentIndexChanged.connect(self.action_combobox_changed)

    def action_combobox_changed(self, index):
        if index == 8:
            self.choose_1.show()
            self.choose_2.show()
            data = self.db.load_column("id")
            self.choose_1.addItems(data)
            self.choose_2.addItems(data)

        else:
            self.choose_1.hide()
            self.choose_2.hide()

    def action(self, text):
        result = ""
        spltext = text.split(" ")
        if "most" in spltext:
            value, amount = self.db.most_common(spltext[1])
            result = f"Most common {spltext[1]} is {value}, amount {amount}."
        elif "least" in spltext:
            value, amount = self.db.least_common(spltext[1])
            result = f"Least common {spltext[1]} is {value}, amount {amount}."
        elif "Average age of all employees?" == text:
            avg = self.db.average_age()
            result = f"Average age of employee is {avg}"
        elif "Employees whose first, last name and age are the same." == text:
            ids = []
            for i in self.db.same_name_surname_age():
                id, _, _, _ = i
                ids.append(id)
            if ids:
                result = f"Employees with the same first name, last name and age have this id's {ids}"
            else:
                result = "There is no employee who has all three data matches."
        elif "Compare age by ID" == text:
            id1, _, _, age1 = self.db.search(id=self.choose_1.currentText())[0]
            id2, _, _, age2 = self.db.search(id=self.choose_2.currentText())[0]
            if age1 - age2 > 0:
                result = (f"Employee with {id1} ID is older than the employee with {id2} ID,\nthe difference between "
                          f"them {age1 - age2}.")
            elif age2 - age1 > 0:
                result = (f"Employee with {id1} ID is younger than the employee with {id2} ID,\nthe difference between "
                          f"them {age2 - age1}.")
            else:
                result = f"Employee with {id1} ID of the same age as an employee with {id2} ID."
        self.result_lbl.setText(result)

    def init_action(self):
        actions = ["What name are most common?", "Which name are the least common?",
                   "What surname are most common?", "Which surname is the least common?",
                   "What age people are most common?", "What age people are the least common?",
                   "Average age of all employees?", "Employees whose first, last name and age are the same.",
                   "Compare age by ID"]
        self.action_cb.addItems(actions)

    def change_page(self, name):
        self.stackedWidget.setCurrentWidget(name)
        if name == self.bd_page:
            self.load_data_into_table(self.db.load_data())

    def save(self):
        for row in range(self.tableWidget.rowCount()):
            name = self.tableWidget.item(row, 1).text()
            surname = self.tableWidget.item(row, 2).text()
            age = self.tableWidget.item(row, 3).text()

            row_id = int(self.tableWidget.item(row, 0).text())
            self.db.update(name, surname, age, row_id)

        QMessageBox.information(self, "Success", "Successfully saved all changes.")

    def add_random_data(self, region, number):
        self.groupBox.setEnabled(False)
        self.generaty_db_button.setEnabled(False)
        self.thread = QThread()
        self.worker = Worker(region, number)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.thread.start()
        self.worker.progress_bar.connect(self.handle_progressbar)
        self.worker.finished.connect(self.handle_results)

    def handle_progressbar(self, percentage):
        self.progressBar.setValue(percentage)

    def handle_results(self):
        QMessageBox.information(self, "Success", "Successfully generated and saved.")
        self.groupBox.setEnabled(True)
        self.generaty_db_button.setEnabled(True)

    def add_one_data(self, name, surname, age):
        if name and surname and age:
            self.db.add_data(name, surname, age)
            self.load_data_into_table(self.db.load_data())
        else:
            QMessageBox.warning(self, "Warning", "Please enter all information.")

    def delete_data(self):
        selected_rows = self.tableWidget.selectedItems()
        selected_indexes = set()
        for item in selected_rows:
            selected_indexes.add(item.row())

        confirm_dialog = QMessageBox.question(
            self,
            "Confirm Deletion",
            f"Do you really want to delete data in  {list(selected_indexes)}?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if confirm_dialog == QMessageBox.Yes:

            for index in sorted(selected_indexes, reverse=True):
                row_id = self.tableWidget.item(index, 0).text()
                self.db.delete_row(row_id)
            self.load_data_into_table(self.db.load_data())

    def search_info(self, name, surname, age):
        self.load_data_into_table(self.db.search(name, surname, age))

    def load_data_into_table(self, data):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        for row_index, row_data in enumerate(data):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for column_index, column_data in enumerate(row_data):
                item = QTableWidgetItem(str(column_data))
                self.tableWidget.setItem(row_index, column_index, item)
            item = self.tableWidget.item(row_index, 0)
            item.setFlags(item.flags() ^ 2)
