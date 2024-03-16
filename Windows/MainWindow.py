from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(904, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.main_page = QtWidgets.QWidget()
        self.main_page.setObjectName("main_page")
        self.gridLayout = QtWidgets.QGridLayout(self.main_page)
        self.gridLayout.setObjectName("gridLayout")
        self.custom_button = QtWidgets.QPushButton(self.main_page)
        self.custom_button.setObjectName("custom_button")
        self.gridLayout.addWidget(self.custom_button, 5, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 7, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.main_page)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setMinimumSize(QtCore.QSize(2, 0))
        self.label_4.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.region_cb = QtWidgets.QComboBox(self.groupBox)
        self.region_cb.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.region_cb.setFont(font)
        self.region_cb.setObjectName("region_cb")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.region_cb)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setMinimumSize(QtCore.QSize(0, 0))
        self.label_5.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.amount_spinbox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.amount_spinbox.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.amount_spinbox.setFont(font)
        self.amount_spinbox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.amount_spinbox.setDecimals(0)
        self.amount_spinbox.setMaximum(100000.0)
        self.amount_spinbox.setObjectName("amount_spinbox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.amount_spinbox)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.progressBar)
        self.generaty_db_button = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.generaty_db_button.setFont(font)
        self.generaty_db_button.setObjectName("generaty_db_button")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.generaty_db_button)
        self.gridLayout.addWidget(self.groupBox, 3, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.main_page)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.generaty_button = QtWidgets.QPushButton(self.groupBox_2)
        self.generaty_button.setObjectName("generaty_button")
        self.gridLayout_3.addWidget(self.generaty_button, 3, 0, 1, 2)
        self.action_cb = QtWidgets.QComboBox(self.groupBox_2)
        self.action_cb.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.action_cb.setFont(font)
        self.action_cb.setObjectName("action_cb")
        self.gridLayout_3.addWidget(self.action_cb, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.result_lbl = QtWidgets.QLabel(self.groupBox_2)
        self.result_lbl.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.result_lbl.setFont(font)
        self.result_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.result_lbl.setObjectName("result_lbl")
        self.gridLayout_3.addWidget(self.result_lbl, 4, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.choose_1 = QtWidgets.QComboBox(self.groupBox_2)
        self.choose_1.setObjectName("choose_1")
        self.horizontalLayout.addWidget(self.choose_1)
        self.choose_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.choose_2.setObjectName("choose_2")
        self.horizontalLayout.addWidget(self.choose_2)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 2, 2)
        self.gridLayout.addWidget(self.groupBox_2, 6, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 4, 1, 1, 1)
        self.stackedWidget.addWidget(self.main_page)
        self.bd_page = QtWidgets.QWidget()
        self.bd_page.setObjectName("bd_page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.bd_page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.bd_page)
        self.label_3.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)
        self.age_input = QtWidgets.QLineEdit(self.bd_page)
        self.age_input.setMinimumSize(QtCore.QSize(0, 25))
        self.age_input.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.age_input.setFont(font)
        self.age_input.setObjectName("age_input")
        self.gridLayout_2.addWidget(self.age_input, 3, 1, 1, 1)
        self.surname_input = QtWidgets.QLineEdit(self.bd_page)
        self.surname_input.setMinimumSize(QtCore.QSize(0, 25))
        self.surname_input.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.surname_input.setFont(font)
        self.surname_input.setObjectName("surname_input")
        self.gridLayout_2.addWidget(self.surname_input, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.bd_page)
        self.label_2.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.bd_page)
        self.tableWidget.setMinimumSize(QtCore.QSize(550, 396))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.gridLayout_2.addWidget(self.tableWidget, 8, 0, 2, 3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 4, 0, 1, 4)
        self.name_input = QtWidgets.QLineEdit(self.bd_page)
        self.name_input.setMinimumSize(QtCore.QSize(0, 25))
        self.name_input.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name_input.setFont(font)
        self.name_input.setObjectName("name_input")
        self.gridLayout_2.addWidget(self.name_input, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.bd_page)
        self.label.setMinimumSize(QtCore.QSize(0, 25))
        self.label.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.bd_page)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.delete_button = QtWidgets.QPushButton(self.frame)
        self.delete_button.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.delete_button.setFont(font)
        self.delete_button.setObjectName("delete_button")
        self.verticalLayout.addWidget(self.delete_button)
        self.save_new = QtWidgets.QPushButton(self.frame)
        self.save_new.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.save_new.setFont(font)
        self.save_new.setObjectName("save_new")
        self.verticalLayout.addWidget(self.save_new)
        self.gridLayout_2.addWidget(self.frame, 9, 3, 1, 1)
        self.add_button = QtWidgets.QPushButton(self.bd_page)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.gridLayout_2.addWidget(self.add_button, 2, 3, 1, 1)
        self.search_button = QtWidgets.QPushButton(self.bd_page)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.search_button.setFont(font)
        self.search_button.setObjectName("search_button")
        self.gridLayout_2.addWidget(self.search_button, 3, 3, 1, 1)
        self.main_menu_button = QtWidgets.QPushButton(self.bd_page)
        self.main_menu_button.setObjectName("main_menu_button")
        self.gridLayout_2.addWidget(self.main_menu_button, 1, 3, 1, 1)
        self.stackedWidget.addWidget(self.bd_page)
        self.gridLayout_4.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.custom_button.setText(_translate("MainWindow", "Custom Database"))
        self.groupBox.setTitle(_translate("MainWindow", "Random"))
        self.label_4.setText(_translate("MainWindow", "Region:"))
        self.label_5.setText(_translate("MainWindow", "Amount:"))
        self.generaty_db_button.setText(_translate("MainWindow", "Generaty DB"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Action"))
        self.generaty_button.setText(_translate("MainWindow", "Result"))
        self.label_6.setText(_translate("MainWindow", "Choose:"))
        self.label_3.setText(_translate("MainWindow", "Age:"))
        self.label_2.setText(_translate("MainWindow", "Surname:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NAME"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "SURNAME"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "AGE"))
        self.label.setText(_translate("MainWindow", "Name:"))
        self.delete_button.setText(_translate("MainWindow", "Delete Employee"))
        self.save_new.setText(_translate("MainWindow", "Save"))
        self.add_button.setText(_translate("MainWindow", "Add Employee"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.main_menu_button.setText(_translate("MainWindow", "Main Menu"))