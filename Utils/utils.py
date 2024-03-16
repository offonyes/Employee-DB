from PyQt5.QtCore import *
from .db import DatabaseManager
import json
import random


class Worker(QObject):
    progress_bar = pyqtSignal(int)
    finished = pyqtSignal(bool)

    def __init__(self, region, number):
        super(Worker, self).__init__()
        self.region = region
        self.number = number
        self.db = DatabaseManager("Data\\employee.db")

    def random_data(self):
        with open("Data\\data.json", "r") as f:
            data = json.load(f)
        names = data[self.region]["male"] + data[self.region]["female"]
        surnames = data[self.region]["surnames"]

        name = random.choice(names)
        surname = random.choice(surnames)
        age = random.randint(18, 105)

        return name, surname, age

    def run(self):
        for i in range(self.number):
            name, surname, age = self.random_data()
            self.db.add_data(name, surname, age)
            self.progress_bar.emit(int((i / self.number) * 100 + 1))
        self.finished.emit(True)
