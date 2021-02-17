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

    def show_bd(self):
        res = self.connection.cursor().execute("SELECT * FROM main").fetchall()
        self.table.setColumnCount(7)
        self.table.setRowCount(0)
        for i, row in enumerate(res):
            self.table.setRowCount(
                self.table.rowCount() + 1)
            for j, elem in enumerate(row):
                self.table.setItem(
                    i, j, QtWidgets.QTableWidgetItem(str(elem)))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())
