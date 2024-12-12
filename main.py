import sqlite3
from PyQt6 import QtWidgets, uic


class CoffeeApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(CoffeeApp, self).__init__()
        uic.loadUi('main.ui', self)
        self.load_data()

    def load_data(self):
        connection = sqlite3.connect('coffee.sqlite')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM coffee")
        rows = cursor.fetchall()
        for row in rows:
            self.listWidget.addItem(f"ID: {row[0]}, Название: {row[1]}, Обжарка: {row[2]}, "
                                    f"Тип: {row[3]}, Вкус: {row[4]}, Цена: {row[5]}, Объем: {row[6]}")
        connection.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = CoffeeApp()
    window.show()
    app.exec()
