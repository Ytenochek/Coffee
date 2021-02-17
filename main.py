import sqlite3
import sys
from PyQt5 import QtWidgets, uic


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        uic.loadUi("main.ui", self)
        self.setWindowTitle("Espresso")

        self.connection = sqlite3.connect("coffee.sqlite")
        self.show_bd()

        self.add.clicked.connect(self.add_to_bd)
        self.change.clicked.connect(self.change_in_bd)

    def add_to_bd(self):
        data = self.call_dialog()

        cur = self.connection.cursor()
        q = "INSERT INTO main VALUES "
        q += f"(NULL, '{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}', '{data[5]}')"
        print(q)
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


class AddUpdateDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("addEditCoffeeForm.ui", self)
        self.setWindowTitle("Form")
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
