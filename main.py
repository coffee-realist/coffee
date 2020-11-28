import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import sqlite3


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.load_button.clicked.connect(self.load)
        self.clear_button.clicked.connect(self.clear)

    def load(self):
        db = sqlite3.connect('coffee.sqlite')
        result = db.cursor().execute("""SELECT * FROM coffee""").fetchall()
        db.close()
        rows = [row[:7] for row in result]
        self.add_to_table(rows)

    def add_to_table(self, rows):
        self.table.setRowCount(0)
        for i, row in enumerate(rows):
            self.table.setRowCount(
                self.table.rowCount() + 1)
            for j, elem in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(str(elem)))
        self.table.resizeColumnsToContents()

    def clear(self):
        self.table.clearContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cof = Coffee()
    cof.show()
    sys.exit(app.exec_())
