import sqlite3
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_name = QtWidgets.QLabel(Form)
        self.label_name.setObjectName("label_name")
        self.horizontalLayout.addWidget(self.label_name)
        self.name_input = QtWidgets.QLineEdit(Form)
        self.name_input.setObjectName("name_input")
        self.horizontalLayout.addWidget(self.name_input)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_name_2 = QtWidgets.QLabel(Form)
        self.label_name_2.setObjectName("label_name_2")
        self.horizontalLayout_2.addWidget(self.label_name_2)
        self.roast_input = QtWidgets.QLineEdit(Form)
        self.roast_input.setObjectName("roast_input")
        self.horizontalLayout_2.addWidget(self.roast_input)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_name_3 = QtWidgets.QLabel(Form)
        self.label_name_3.setObjectName("label_name_3")
        self.horizontalLayout_3.addWidget(self.label_name_3)
        self.beans_input = QtWidgets.QLineEdit(Form)
        self.beans_input.setObjectName("beans_input")
        self.horizontalLayout_3.addWidget(self.beans_input)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_name_4 = QtWidgets.QLabel(Form)
        self.label_name_4.setObjectName("label_name_4")
        self.horizontalLayout_4.addWidget(self.label_name_4)
        self.taste_input = QtWidgets.QLineEdit(Form)
        self.taste_input.setObjectName("taste_input")
        self.horizontalLayout_4.addWidget(self.taste_input)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_name_5 = QtWidgets.QLabel(Form)
        self.label_name_5.setObjectName("label_name_5")
        self.horizontalLayout_5.addWidget(self.label_name_5)
        self.price_input = QtWidgets.QLineEdit(Form)
        self.price_input.setObjectName("price_input")
        self.horizontalLayout_5.addWidget(self.price_input)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_name_6 = QtWidgets.QLabel(Form)
        self.label_name_6.setObjectName("label_name_6")
        self.horizontalLayout_6.addWidget(self.label_name_6)
        self.volume_input = QtWidgets.QLineEdit(Form)
        self.volume_input.setObjectName("volume_input")
        self.horizontalLayout_6.addWidget(self.volume_input)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.finish = QtWidgets.QPushButton(Form)
        self.finish.setObjectName("finish")
        self.verticalLayout.addWidget(self.finish)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_name.setText(_translate("Form", "Name"))
        self.label_name_2.setText(_translate("Form", "Roast"))
        self.label_name_3.setText(_translate("Form", "Beans"))
        self.label_name_4.setText(_translate("Form", "Taste"))
        self.label_name_5.setText(_translate("Form", "Price"))
        self.label_name_6.setText(_translate("Form", "Volume"))
        self.finish.setText(_translate("Form", "Готово"))


class Ui_Espresso(object):
    def setupUi(self, Espresso):
        Espresso.setObjectName("Espresso")
        Espresso.resize(799, 505)
        self.mainLayout = QtWidgets.QWidget(Espresso)
        self.mainLayout.setObjectName("mainLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainLayout)
        self.verticalLayout.setObjectName("verticalLayout")
        self.add = QtWidgets.QPushButton(self.mainLayout)
        self.add.setObjectName("add")
        self.verticalLayout.addWidget(self.add)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.table = QtWidgets.QTableWidget(self.mainLayout)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.horizontalLayout.addWidget(self.table)
        self.change = QtWidgets.QPushButton(self.mainLayout)
        self.change.setObjectName("change")
        self.horizontalLayout.addWidget(self.change)
        self.verticalLayout.addLayout(self.horizontalLayout)
        Espresso.setCentralWidget(self.mainLayout)

        self.retranslateUi(Espresso)
        QtCore.QMetaObject.connectSlotsByName(Espresso)

    def retranslateUi(self, Espresso):
        _translate = QtCore.QCoreApplication.translate
        Espresso.setWindowTitle(_translate("Espresso", "MainWindow"))
        self.add.setText(_translate("Espresso", "Добавить"))
        self.change.setText(_translate("Espresso", "Изменить"))


class App(QtWidgets.QMainWindow, Ui_Espresso):
    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Espresso")

        self.connection = sqlite3.connect("data/coffee.sqlite")
        self.show_bd()

        self.add.clicked.connect(self.add_to_bd)
        self.change.clicked.connect(self.change_in_bd)

    def add_to_bd(self):
        data = self.call_dialog()

        cur = self.connection.cursor()
        q = "INSERT INTO main VALUES "
        q += f"(NULL, '{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}', '{data[5]}')"
        cur.execute(q)
        self.connection.commit()

        self.show_bd()

    def change_in_bd(self):
        data = self.call_dialog()

        id = self.table.item(self.table.selectedItems()[0].row(), 0).text()
        cur = self.connection.cursor()
        q = "UPDATE main SET "
        q += f"Name='{data[0]}', Degree_of_roast='{data[1]}', Beans='{data[2]}', Taste='{data[3]}', Price='{data[4]}', Packing_volume='{data[5]}'"
        q += f"WHERE ID = {id}"
        cur.execute(q)
        self.connection.commit()

        self.show_bd()

    @staticmethod
    def call_dialog():
        dialog = AddUpdateDialog()
        if dialog.exec_():
            return dialog.data

    def show_bd(self):
        res = self.connection.cursor().execute("SELECT * FROM main").fetchall()
        self.table.setColumnCount(7)
        self.table.setRowCount(0)
        for i, row in enumerate(res):
            self.table.setRowCount(self.table.rowCount() + 1)
            for j, elem in enumerate(row):
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(str(elem)))


class AddUpdateDialog(QtWidgets.QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Form.py")
        self.data = []
        self.finish.clicked.connect(self.submitclose)

    def submitclose(self):
        self.data = [
            self.name_input.text(),
            self.roast_input.text(),
            self.beans_input.text(),
            self.taste_input.text(),
            self.price_input.text(),
            self.volume_input.text(),
        ]
        self.accept()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
