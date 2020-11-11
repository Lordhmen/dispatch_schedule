from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
import sqlite3
from datetime import datetime
import openpyxl

from untitled import *
import otchet
import tabel


class Otchet(otchet.MyWinn):
    def __init__(self):
        super().__init__()
        # self.setupUi(self)


class Tabel(tabel.MyWin):
    def __init__(self):
        super().__init__()
        # self.setupUi(self)


class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.action_5.triggered.connect(self.tabel)
        self.ui.action_6.triggered.connect(self.otchet)
        self.ui.action_8.triggered.connect(self.ObAvtore)
        self.ui.action_7.triggered.connect(self.Oprogram)
        self.ui.action_2.triggered.connect(self.close)
        current_datetime = str(datetime.now())
        current_date = current_datetime.split()
        del current_date[1]
        current_date = current_date[0].split('-')[::-1]

        self.ui.dateEdit.setDateTime(
            QtCore.QDateTime(QtCore.QDate(int(current_date[2]), int(current_date[1]), int(current_date[0])),
                             QtCore.QTime(0, 0, 0)))
        item = 'a'
        font = QtGui.QFont()
        font.setFamily("Tabellsymboler")
        font.setPointSize(60)
        self.ui.label_4.setFont(font)
        self.ui.label_4.setText(item)
        self.ui.label_4.setStyleSheet("color: rgb(85, 170, 0);")
        self.ui.comboBox.activated.connect(self.start_status)
        self.ui.tableWidget.cellClicked.connect(self.row_column_clicked)
        self.ui.tableWidget.cellPressed.connect(self.clean_clicked)
        self.ui.dateEdit.dateChanged.connect(self.start_prog)
        self.start_prog()
        global timing
        timing = ['00:00', '00:10', '00:20', '00:30', '00:40', '00:50', '01:00', '01:10', '01:20', '01:30', '01:40',
                  '01:50',
                  '02:00', '2:10', '2:20', '2:30', '2:40', '2:50', '3:00', '3:10', '3:20', '3:30', '3:40', '3:50',
                  '4:00',
                  '4:10', '4:20', '4:30', '4:40', '4:50', '5:00', '5:10', '5:20', '5:30', '5:40', '5:50', '6:00',
                  '6:10',
                  '6:20', '6:30', '6:40', '6:50', '7:00', '7:10', '7:20', '7:30', '7:40', '7:50', '8:00', '8:10',
                  '8:20',
                  '8:30', '8:40', '8:50', '9:00', '9:10', '9:20', '9:30', '9:40', '9:50', '10:00', '10:10', '10:20',
                  '10:30',
                  '10:40', '10:50', '11:00', '11:10', '11:20', '11:30', '11:40', '11:50', '12:00', '12:10', '12:20',
                  '12:30',
                  '12:40', '12:50', '13:00', '13:10', '13:20', '13:30', '13:40', '13:50', '14:00', '14:10', '14:20',
                  '14:30',
                  '14:40', '14:50', '15:00', '15:10', '15:20', '15:30', '15:40', '15:50', '16:00', '16:10', '16:20',
                  '16:30',
                  '16:40', '16:50', '17:00', '17:10', '17:20', '17:30', '17:40', '17:50', '18:00', '18:10', '18:20',
                  '18:30',
                  '18:40', '18:50', '19:00', '19:10', '19:20', '19:30', '19:40', '19:50', '20:00', '20:10', '20:20',
                  '20:30',
                  '20:40', '20:50', '21:00', '21:10', '21:20', '21:30', '21:40', '21:50', '22:00', '22:10', '22:20',
                  '22:30',
                  '22:40', '22:50', '23:00', '23:10', '23:20', '23:30', '23:40', '23:50']
        h = 0
        self.ui.tableWidget.setColumnCount(144)
        for i in timing:
            item = QtWidgets.QTableWidgetItem(i)
            font = QtGui.QFont()
            font.setFamily("Segoe UI")
            font.setPointSize(8)
            item.setFont(font)
            self.ui.tableWidget.setHorizontalHeaderItem(h, item)
            h += 1

        conn = sqlite3.connect("bd.db")
        cursor = conn.cursor()

        conn.commit()

    def tabel(self):
        self.aabout = Tabel()
        self.aabout.show()

    def otchet(self):
        self.iinst = Otchet()
        self.iinst.show()

    def ObAvtore(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Об авторе")
        msg.setText('Данный программный продукт разработан курсантам 431 группы Кирсанов Г.В. по специальности: 09.02.03 «Программирование в компьютерных системах»')
        okButton = msg.addButton('Хорошо', QMessageBox.AcceptRole)
        msg.exec()

    def Oprogram(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("О программе")
        msg.setText('Данный программный продукт разработан для автоматизация учета исправности и использования самолетов в эксплуатационном авиапредприятии')
        okButton = msg.addButton('Хорошо', QMessageBox.AcceptRole)
        msg.exec()

    def datat(self):
        global data
        data = str(self.ui.dateEdit.date())[str(self.ui.dateEdit.date()).find('('):].replace('(', '').replace(')',
                                                                                                              '').replace(
            ',', '').split()[::-1]
        if len(data[1]) == 1:
            data = data[0] + '.0' + data[1] + '.' + data[2]
        else:
            data = data[0] + '.' + data[1] + '.' + data[2]
        print(data)

    def clean_clicked(self):
        global timing
        row = self.ui.tableWidget.currentRow()
        col = self.ui.tableWidget.currentColumn()
        sostoynie = self.ui.comboBox.currentIndex()
        self.datat()
        # data = '22.10.2020'
        conn = sqlite3.connect("bd.db")
        cursor = conn.cursor()
        item = QtWidgets.QTableWidgetItem('')
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.ui.tableWidget.setItem(row, col, item)
        if row == 0:
            table = 'Боинг-767'
        if row == 1:
            table = 'Боинг-777'
        if row == 2:
            table = 'Ил-96'
        if row == 3:
            table = 'Ту-134'
        if row == 4:
            table = 'Ту-154'
        item = ''
        cursor.execute("UPDATE " + "'" + table + "'" + " SET " + "'" + timing[col] + "'" + " = " + "'" + str(
            item) + "'" + " WHERE Data = " + "'" + str(data) + "'")
        conn.commit()

    def start_prog(self):
        self.datat()

        conn = sqlite3.connect("bd.db")
        cursor = conn.cursor()

        # Получаем данные с таблица Фильмы
        cursor.execute("SELECT * FROM 'Боинг-767'")
        boing_767 = cursor.fetchall()
        cursor.execute("SELECT * FROM 'Боинг-777'")
        boing_777 = cursor.fetchall()
        cursor.execute("SELECT * FROM 'Ил-96'")
        il_96 = cursor.fetchall()
        cursor.execute("SELECT * FROM 'Ту-134'")
        tu_134 = cursor.fetchall()
        cursor.execute("SELECT * FROM 'Ту-154'")
        tu_154 = cursor.fetchall()
        for i in boing_767:
            for j in range(144):
                self.ui.tableWidget.setItem(0, j, QTableWidgetItem(''))
                self.ui.tableWidget.setItem(1, j, QTableWidgetItem(''))
                self.ui.tableWidget.setItem(2, j, QTableWidgetItem(''))
                self.ui.tableWidget.setItem(3, j, QTableWidgetItem(''))
                self.ui.tableWidget.setItem(4, j, QTableWidgetItem(''))
        for i in boing_767:
            if i[0] == data:
                for j in range(144):
                    if i[j + 1] == 'a':
                        item = QtWidgets.QTableWidgetItem('a')
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(0, j, item)
                    if i[j + 1] == 'b':
                        item = QtWidgets.QTableWidgetItem('b')
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(0, j, item)
                    if i[j + 1] == 'c':
                        item = QtWidgets.QTableWidgetItem('c')
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(0, j, item)
                    if i[j + 1] == 'd':
                        item = QtWidgets.QTableWidgetItem('d')
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(0, j, item)
                    if i[j + 1] == 'e':
                        item = QtWidgets.QTableWidgetItem('e')
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(0, j, item)
                    if i[j + 1] == 'f':
                        item = QtWidgets.QTableWidgetItem('f')
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(0, j, item)
                    if i[j + 1] == 'g':
                        item = QtWidgets.QTableWidgetItem('g')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(0, j, item)
                    if i[j + 1] == 'h':
                        item = QtWidgets.QTableWidgetItem('h')
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(0, j, item)
                    if i[j + 1] == 'i':
                        item = QtWidgets.QTableWidgetItem('i')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(0, j, item)
                    if i[j + 1] == 'j':
                        item = QtWidgets.QTableWidgetItem('j')
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(0, j, item)
                    if i[j + 1] == 'k':
                        item = QtWidgets.QTableWidgetItem('k')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(0, j, item)
                    if i[j + 1] == 'l':
                        item = QtWidgets.QTableWidgetItem('l')
                        brush = QtGui.QBrush(QtGui.QColor(150, 75, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(150, 75, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(0, j, item)
                    if i[j + 1] == 'm':
                        item = QtWidgets.QTableWidgetItem('m')
                        brush = QtGui.QBrush(QtGui.QColor(150, 75, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(150, 75, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(0, j, item)
                    if i[j + 1] == 'n':
                        item = QtWidgets.QTableWidgetItem('n')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(0, j, item)
                    if i[j + 1] == 'o':
                        item = QtWidgets.QTableWidgetItem('o')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(0, j, item)
                    if i[j + 1] == 'p':
                        item = QtWidgets.QTableWidgetItem('p')
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(0, j, item)
                    if i[j + 1] == 'q':
                        item = QtWidgets.QTableWidgetItem('q')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(0, j, item)
                    if i[j + 1] == 'r':
                        item = QtWidgets.QTableWidgetItem('r')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(0, j, item)
                    if i[j + 1] == 's':
                        item = QtWidgets.QTableWidgetItem('s')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(0, j, item)
                    if i[j + 1] == 't':
                        item = QtWidgets.QTableWidgetItem('t')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(0, j, item)
                    if i[j + 1] == 'u':
                        item = QtWidgets.QTableWidgetItem('u')
                        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(0, j, item)
        for i in boing_777:
            if i[0] == data:
                for j in range(144):
                    if i[j + 1] == 'a':
                        item = QtWidgets.QTableWidgetItem('a')
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(1, j, item)
                    if i[j + 1] == 'b':
                        item = QtWidgets.QTableWidgetItem('b')
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(1, j, item)
                    if i[j + 1] == 'c':
                        item = QtWidgets.QTableWidgetItem('c')
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(1, j, item)
                    if i[j + 1] == 'd':
                        item = QtWidgets.QTableWidgetItem('d')
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(1, j, item)
                    if i[j + 1] == 'e':
                        item = QtWidgets.QTableWidgetItem('e')
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(1, j, item)
                    if i[j + 1] == 'f':
                        item = QtWidgets.QTableWidgetItem('f')
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(1, j, item)
                    if i[j + 1] == 'g':
                        item = QtWidgets.QTableWidgetItem('g')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(1, j, item)
                    if i[j + 1] == 'h':
                        item = QtWidgets.QTableWidgetItem('h')
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(1, j, item)
                    if i[j + 1] == 'i':
                        item = QtWidgets.QTableWidgetItem('i')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(1, j, item)
                    if i[j + 1] == 'j':
                        item = QtWidgets.QTableWidgetItem('j')
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(1, j, item)
                    if i[j + 1] == 'k':
                        item = QtWidgets.QTableWidgetItem('k')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(1, j, item)
                    if i[j + 1] == 'l':
                        item = QtWidgets.QTableWidgetItem('l')
                        brush = QtGui.QBrush(QtGui.QColor(150, 75, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(150, 75, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(1, j, item)
                    if i[j + 1] == 'm':
                        item = QtWidgets.QTableWidgetItem('m')
                        brush = QtGui.QBrush(QtGui.QColor(150, 75, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(150, 75, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(1, j, item)
                    if i[j + 1] == 'n':
                        item = QtWidgets.QTableWidgetItem('n')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(1, j, item)
                    if i[j + 1] == 'o':
                        item = QtWidgets.QTableWidgetItem('o')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(1, j, item)
                    if i[j + 1] == 'p':
                        item = QtWidgets.QTableWidgetItem('p')
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(1, j, item)
                    if i[j + 1] == 'q':
                        item = QtWidgets.QTableWidgetItem('q')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(1, j, item)
                    if i[j + 1] == 'r':
                        item = QtWidgets.QTableWidgetItem('r')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(1, j, item)
                    if i[j + 1] == 's':
                        item = QtWidgets.QTableWidgetItem('s')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(1, j, item)
                    if i[j + 1] == 't':
                        item = QtWidgets.QTableWidgetItem('t')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(1, j, item)
                    if i[j + 1] == 'u':
                        item = QtWidgets.QTableWidgetItem('u')
                        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(1, j, item)
        for i in il_96:
            if i[0] == data:
                for j in range(144):
                    if i[j + 1] == 'a':
                        item = QtWidgets.QTableWidgetItem('a')
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(2, j, item)
                    if i[j + 1] == 'b':
                        item = QtWidgets.QTableWidgetItem('b')
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(2, j, item)
                    if i[j + 1] == 'c':
                        item = QtWidgets.QTableWidgetItem('c')
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(2, j, item)
                    if i[j + 1] == 'd':
                        item = QtWidgets.QTableWidgetItem('d')
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(2, j, item)
                    if i[j + 1] == 'e':
                        item = QtWidgets.QTableWidgetItem('e')
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(2, j, item)
                    if i[j + 1] == 'f':
                        item = QtWidgets.QTableWidgetItem('f')
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(2, j, item)
                    if i[j + 1] == 'g':
                        item = QtWidgets.QTableWidgetItem('g')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(2, j, item)
                    if i[j + 1] == 'h':
                        item = QtWidgets.QTableWidgetItem('h')
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(2, j, item)
                    if i[j + 1] == 'i':
                        item = QtWidgets.QTableWidgetItem('i')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(2, j, item)
                    if i[j + 1] == 'j':
                        item = QtWidgets.QTableWidgetItem('j')
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(2, j, item)
                    if i[j + 1] == 'k':
                        item = QtWidgets.QTableWidgetItem('k')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(2, j, item)
                    if i[j + 1] == 'l':
                        item = QtWidgets.QTableWidgetItem('l')
                        brush = QtGui.QBrush(QtGui.QColor(150, 75, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(150, 75, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(2, j, item)
                    if i[j + 1] == 'm':
                        item = QtWidgets.QTableWidgetItem('m')
                        brush = QtGui.QBrush(QtGui.QColor(150, 75, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(150, 75, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(2, j, item)
                    if i[j + 1] == 'n':
                        item = QtWidgets.QTableWidgetItem('n')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(2, j, item)
                    if i[j + 1] == 'o':
                        item = QtWidgets.QTableWidgetItem('o')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(2, j, item)
                    if i[j + 1] == 'p':
                        item = QtWidgets.QTableWidgetItem('p')
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(2, j, item)
                    if i[j + 1] == 'q':
                        item = QtWidgets.QTableWidgetItem('q')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(2, j, item)
                    if i[j + 1] == 'r':
                        item = QtWidgets.QTableWidgetItem('r')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(2, j, item)
                    if i[j + 1] == 's':
                        item = QtWidgets.QTableWidgetItem('s')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(2, j, item)
                    if i[j + 1] == 't':
                        item = QtWidgets.QTableWidgetItem('t')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(2, j, item)
                    if i[j + 1] == 'u':
                        item = QtWidgets.QTableWidgetItem('u')
                        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(2, j, item)
        for i in tu_134:
            if i[0] == data:
                for j in range(144):
                    if i[j + 1] == 'a':
                        item = QtWidgets.QTableWidgetItem('a')
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(3, j, item)
                    if i[j + 1] == 'b':
                        item = QtWidgets.QTableWidgetItem('b')
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(3, j, item)
                    if i[j + 1] == 'c':
                        item = QtWidgets.QTableWidgetItem('c')
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(3, j, item)
                    if i[j + 1] == 'd':
                        item = QtWidgets.QTableWidgetItem('d')
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(3, j, item)
                    if i[j + 1] == 'e':
                        item = QtWidgets.QTableWidgetItem('e')
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(3, j, item)
                    if i[j + 1] == 'f':
                        item = QtWidgets.QTableWidgetItem('f')
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(3, j, item)
                    if i[j + 1] == 'g':
                        item = QtWidgets.QTableWidgetItem('g')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(3, j, item)
                    if i[j + 1] == 'h':
                        item = QtWidgets.QTableWidgetItem('h')
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(3, j, item)
                    if i[j + 1] == 'i':
                        item = QtWidgets.QTableWidgetItem('i')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(3, j, item)
                    if i[j + 1] == 'j':
                        item = QtWidgets.QTableWidgetItem('j')
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(3, j, item)
                    if i[j + 1] == 'k':
                        item = QtWidgets.QTableWidgetItem('k')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(3, j, item)
                    if i[j + 1] == 'l':
                        item = QtWidgets.QTableWidgetItem('l')
                        brush = QtGui.QBrush(QtGui.QColor(150, 75, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(150, 75, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(3, j, item)
                    if i[j + 1] == 'm':
                        item = QtWidgets.QTableWidgetItem('m')
                        brush = QtGui.QBrush(QtGui.QColor(150, 75, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(150, 75, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(3, j, item)
                    if i[j + 1] == 'n':
                        item = QtWidgets.QTableWidgetItem('n')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(3, j, item)
                    if i[j + 1] == 'o':
                        item = QtWidgets.QTableWidgetItem('o')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(3, j, item)
                    if i[j + 1] == 'p':
                        item = QtWidgets.QTableWidgetItem('p')
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(3, j, item)
                    if i[j + 1] == 'q':
                        item = QtWidgets.QTableWidgetItem('q')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(3, j, item)
                    if i[j + 1] == 'r':
                        item = QtWidgets.QTableWidgetItem('r')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(3, j, item)
                    if i[j + 1] == 's':
                        item = QtWidgets.QTableWidgetItem('s')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(3, j, item)
                    if i[j + 1] == 't':
                        item = QtWidgets.QTableWidgetItem('t')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(3, j, item)
                    if i[j + 1] == 'u':
                        item = QtWidgets.QTableWidgetItem('u')
                        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(3, j, item)
        for i in tu_154:
            if i[0] == data:
                for j in range(144):
                    if i[j + 1] == 'a':
                        item = QtWidgets.QTableWidgetItem('a')
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(4, j, item)
                    if i[j + 1] == 'b':
                        item = QtWidgets.QTableWidgetItem('b')
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(4, j, item)
                    if i[j + 1] == 'c':
                        item = QtWidgets.QTableWidgetItem('c')
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(4, j, item)
                    if i[j + 1] == 'd':
                        item = QtWidgets.QTableWidgetItem('d')
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(4, j, item)
                    if i[j + 1] == 'e':
                        item = QtWidgets.QTableWidgetItem('e')
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(4, j, item)
                    if i[j + 1] == 'f':
                        item = QtWidgets.QTableWidgetItem('f')
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(4, j, item)
                    if i[j + 1] == 'g':
                        item = QtWidgets.QTableWidgetItem('g')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(4, j, item)
                    if i[j + 1] == 'h':
                        item = QtWidgets.QTableWidgetItem('h')
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(4, j, item)
                    if i[j + 1] == 'i':
                        item = QtWidgets.QTableWidgetItem('i')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(4, j, item)
                    if i[j + 1] == 'j':
                        item = QtWidgets.QTableWidgetItem('j')
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(4, j, item)
                    if i[j + 1] == 'k':
                        item = QtWidgets.QTableWidgetItem('k')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(4, j, item)
                    if i[j + 1] == 'l':
                        item = QtWidgets.QTableWidgetItem('l')
                        brush = QtGui.QBrush(QtGui.QColor(150, 75, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(150, 75, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(4, j, item)
                    if i[j + 1] == 'm':
                        item = QtWidgets.QTableWidgetItem('m')
                        brush = QtGui.QBrush(QtGui.QColor(150, 75, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(150, 75, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(4, j, item)
                    if i[j + 1] == 'n':
                        item = QtWidgets.QTableWidgetItem('n')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(4, j, item)
                    if i[j + 1] == 'o':
                        item = QtWidgets.QTableWidgetItem('o')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(4, j, item)
                    if i[j + 1] == 'p':
                        item = QtWidgets.QTableWidgetItem('p')
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(4, j, item)
                    if i[j + 1] == 'q':
                        item = QtWidgets.QTableWidgetItem('q')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(4, j, item)
                    if i[j + 1] == 'r':
                        item = QtWidgets.QTableWidgetItem('r')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(4, j, item)
                    if i[j + 1] == 's':
                        item = QtWidgets.QTableWidgetItem('s')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(4, j, item)
                    if i[j + 1] == 't':
                        item = QtWidgets.QTableWidgetItem('t')
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(4, j, item)
                    if i[j + 1] == 'u':
                        item = QtWidgets.QTableWidgetItem('u')
                        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setBackground(brush)
                        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        self.ui.tableWidget.setItem(4, j, item)

    def start_status(self):
        sostoynie = self.ui.comboBox.currentIndex()
        if sostoynie == 0:
            item = 'a'
            self.ui.label_4.setText(item)
            self.ui.label_4.setStyleSheet("color: rgb(85, 170, 0);")
        if sostoynie == 1:
            item = 'b'
            self.ui.label_4.setText(item)
            self.ui.label_4.setStyleSheet("color: rgb(85, 170, 0);")
        if sostoynie == 2:
            item = 'c'
            self.ui.label_4.setText(item)
            self.ui.label_4.setStyleSheet("color: rgb(85, 170, 0);")
        if sostoynie == 3:
            item = 'd'
            self.ui.label_4.setText(item)
            self.ui.label_4.setStyleSheet("color: rgb(85, 170, 0);")
        if sostoynie == 4:
            item = 'e'
            self.ui.label_4.setText(item)
            self.ui.label_4.setStyleSheet("color: rgb(85, 170, 0);")
        if sostoynie == 5:
            item = 'f'
            self.ui.label_4.setText(item)
            self.ui.label_4.setStyleSheet("color: rgb(0, 0, 255);")
        if sostoynie == 6:
            item = 'g'
            self.ui.label_4.setText(item)
            self.ui.label_4.setStyleSheet("color: rgb(255, 0, 0);")
        if sostoynie == 7:
            item = 'h'
            self.ui.label_4.setText(item)
            self.ui.label_4.setStyleSheet("color: rgb(0, 0, 255);")
        if sostoynie == 8:
            item = 'i'
            self.ui.label_4.setText(item)
            self.ui.label_4.setStyleSheet("color: rgb(255, 0, 0);")
        if sostoynie == 9:
            item = 'j'
            self.ui.label_4.setText(item)
            self.ui.label_4.setStyleSheet("color: rgb(0, 0, 255);")
        if sostoynie == 10:
            item = 'k'
            self.ui.label_4.setText(item)
            self.ui.label_4.setStyleSheet("color: rgb(255, 0, 0);")
        if sostoynie == 11:
            item = 'l'
            self.ui.label_4.setText(item)
            self.ui.label_4.setStyleSheet("color: rgb(150, 75, 0);")
        if sostoynie == 12:
            item = 'm'
            self.ui.label_4.setText(item)
            self.ui.label_4.setStyleSheet("color: rgb(150, 75, 0);")
        if sostoynie == 13:
            item = 'n'
            self.ui.label_4.setText(item)
            self.ui.label_4.setStyleSheet("color: rgb(255, 0, 0);")
        if sostoynie == 14:
            item = 'o'
            self.ui.label_4.setText(item)
            self.ui.label_4.setStyleSheet("color: rgb(255, 0, 0);")
        if sostoynie == 15:
            item = 'p'
            self.ui.label_4.setText(item)
            self.ui.label_4.setStyleSheet("color: rgb(0, 0, 255);")
        if sostoynie == 16:
            item = 'q'
            self.ui.label_4.setText(item)
            self.ui.label_4.setStyleSheet("color: rgb(255, 0, 0);")
        if sostoynie == 17:
            item = 'r'
            self.ui.label_4.setText(item)
            self.ui.label_4.setStyleSheet("color: rgb(255, 0, 0);")
        if sostoynie == 18:
            item = 's'
            self.ui.label_4.setText(item)
            self.ui.label_4.setStyleSheet("color: rgb(255, 0, 0);")
        if sostoynie == 19:
            item = 't'
            self.ui.label_4.setText(item)
            self.ui.label_4.setStyleSheet("color: rgb(255, 0, 0);")
        if sostoynie == 20:
            item = 'u'
            self.ui.label_4.setText(item)
            self.ui.label_4.setStyleSheet("color: rgb(255, 255, 0);")

    def row_column_clicked(self):
        global timing
        row = self.ui.tableWidget.currentRow()
        col = self.ui.tableWidget.currentColumn()
        sostoynie = self.ui.comboBox.currentIndex()
        self.datat()
        conn = sqlite3.connect("bd.db")
        cursor = conn.cursor()
        # Получаем данные с таблица Фильмы
        cursor.execute("SELECT * FROM 'Боинг-767'")
        boing_767 = cursor.fetchall()
        for i in boing_767:
            if i[0] == data:
                break
        else:
            cursor.execute(
                "INSERT INTO 'Боинг-767' VALUES (" + "'" + data + "'" + ", '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')")
            cursor.execute(
                "INSERT INTO 'Боинг-777' VALUES (" + "'" + data + "'" + ", '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')")
            cursor.execute(
                "INSERT INTO 'Ил-96' VALUES (" + "'" + data + "'" + ", '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')")
            cursor.execute(
                "INSERT INTO 'Ту-134' VALUES (" + "'" + data + "'" + ", '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')")
            cursor.execute(
                "INSERT INTO 'Ту-154' VALUES (" + "'" + data + "'" + ", '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')")

            conn.commit()
        # cursor.execute("SELECT * FROM Боинг-777")
        # boing_777 = cursor.fetchall()
        # cursor.execute("SELECT * FROM Ил-96")
        # il_96 = cursor.fetchall()
        # cursor.execute("SELECT * FROM Ту-134")
        # tu_134 = cursor.fetchall()
        # cursor.execute("SELECT * FROM Ту-154")
        # tu_154 = cursor.fetchall()

        if sostoynie == 0:
            item = QtWidgets.QTableWidgetItem('a')
            brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setBackground(brush)
            brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setForeground(brush)
            print(row, col)
            self.ui.tableWidget.setItem(row, col, item)
            if row == 0:
                table = 'Боинг-767'
            if row == 1:
                table = 'Боинг-777'
            if row == 2:
                table = 'Ил-96'
            if row == 3:
                table = 'Ту-134'
            if row == 4:
                table = 'Ту-154'
            item = 'a'
            cursor.execute("UPDATE " + "'" + table + "'" + " SET " + "'" + timing[col] + "'" + " = " + "'" + str(
                item) + "'" + " WHERE Data = " + "'" + str(data) + "'")
            conn.commit()
        if sostoynie == 1:
            item = QtWidgets.QTableWidgetItem('b')
            brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setBackground(brush)
            brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setForeground(brush)
            self.ui.tableWidget.setItem(row, col, item)
            if row == 0:
                table = 'Боинг-767'
            if row == 1:
                table = 'Боинг-777'
            if row == 2:
                table = 'Ил-96'
            if row == 3:
                table = 'Ту-134'
            if row == 4:
                table = 'Ту-154'
            item = 'b'
            cursor.execute("UPDATE " + "'" + table + "'" + " SET " + "'" + timing[col] + "'" + " = " + "'" + str(
                item) + "'" + " WHERE Data = " + "'" + str(data) + "'")
            conn.commit()
        if sostoynie == 2:
            item = QtWidgets.QTableWidgetItem('c')
            brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setBackground(brush)
            brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setForeground(brush)
            self.ui.tableWidget.setItem(row, col, item)
            if row == 0:
                table = 'Боинг-767'
            if row == 1:
                table = 'Боинг-777'
            if row == 2:
                table = 'Ил-96'
            if row == 3:
                table = 'Ту-134'
            if row == 4:
                table = 'Ту-154'
            item = 'c'
            cursor.execute("UPDATE " + "'" + table + "'" + " SET " + "'" + timing[col] + "'" + " = " + "'" + str(
                item) + "'" + " WHERE Data = " + "'" + str(data) + "'")
            conn.commit()
        if sostoynie == 3:
            item = QtWidgets.QTableWidgetItem('d')
            brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setBackground(brush)
            brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setForeground(brush)
            self.ui.tableWidget.setItem(row, col, item)
            if row == 0:
                table = 'Боинг-767'
            if row == 1:
                table = 'Боинг-777'
            if row == 2:
                table = 'Ил-96'
            if row == 3:
                table = 'Ту-134'
            if row == 4:
                table = 'Ту-154'
            item = 'd'
            cursor.execute("UPDATE " + "'" + table + "'" + " SET " + "'" + timing[col] + "'" + " = " + "'" + str(
                item) + "'" + " WHERE Data = " + "'" + str(data) + "'")
            conn.commit()
        if sostoynie == 4:
            item = QtWidgets.QTableWidgetItem('e')
            brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setBackground(brush)
            brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setForeground(brush)
            self.ui.tableWidget.setItem(row, col, item)
            if row == 0:
                table = 'Боинг-767'
            if row == 1:
                table = 'Боинг-777'
            if row == 2:
                table = 'Ил-96'
            if row == 3:
                table = 'Ту-134'
            if row == 4:
                table = 'Ту-154'
            item = 'e'
            cursor.execute("UPDATE " + "'" + table + "'" + " SET " + "'" + timing[col] + "'" + " = " + "'" + str(
                item) + "'" + " WHERE Data = " + "'" + str(data) + "'")
            conn.commit()
        if sostoynie == 5:
            item = QtWidgets.QTableWidgetItem('f')
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setBackground(brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setForeground(brush)
            self.ui.tableWidget.setItem(row, col, item)
            if row == 0:
                table = 'Боинг-767'
            if row == 1:
                table = 'Боинг-777'
            if row == 2:
                table = 'Ил-96'
            if row == 3:
                table = 'Ту-134'
            if row == 4:
                table = 'Ту-154'
            item = 'f'
            cursor.execute("UPDATE " + "'" + table + "'" + " SET " + "'" + timing[col] + "'" + " = " + "'" + str(
                item) + "'" + " WHERE Data = " + "'" + str(data) + "'")
            conn.commit()
        if sostoynie == 6:
            item = QtWidgets.QTableWidgetItem('g')
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setBackground(brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setForeground(brush)
            self.ui.tableWidget.setItem(row, col, item)
            if row == 0:
                table = 'Боинг-767'
            if row == 1:
                table = 'Боинг-777'
            if row == 2:
                table = 'Ил-96'
            if row == 3:
                table = 'Ту-134'
            if row == 4:
                table = 'Ту-154'
            item = 'g'
            cursor.execute("UPDATE " + "'" + table + "'" + " SET " + "'" + timing[col] + "'" + " = " + "'" + str(
                item) + "'" + " WHERE Data = " + "'" + str(data) + "'")
            conn.commit()
        if sostoynie == 7:
            item = QtWidgets.QTableWidgetItem('h')
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setBackground(brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setForeground(brush)
            self.ui.tableWidget.setItem(row, col, item)
            if row == 0:
                table = 'Боинг-767'
            if row == 1:
                table = 'Боинг-777'
            if row == 2:
                table = 'Ил-96'
            if row == 3:
                table = 'Ту-134'
            if row == 4:
                table = 'Ту-154'
            item = 'h'
            cursor.execute("UPDATE " + "'" + table + "'" + " SET " + "'" + timing[col] + "'" + " = " + "'" + str(
                item) + "'" + " WHERE Data = " + "'" + str(data) + "'")
            conn.commit()
        if sostoynie == 8:
            item = QtWidgets.QTableWidgetItem('i')
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setBackground(brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setForeground(brush)
            self.ui.tableWidget.setItem(row, col, item)
            if row == 0:
                table = 'Боинг-767'
            if row == 1:
                table = 'Боинг-777'
            if row == 2:
                table = 'Ил-96'
            if row == 3:
                table = 'Ту-134'
            if row == 4:
                table = 'Ту-154'
            item = 'i'
            cursor.execute("UPDATE " + "'" + table + "'" + " SET " + "'" + timing[col] + "'" + " = " + "'" + str(
                item) + "'" + " WHERE Data = " + "'" + str(data) + "'")
            conn.commit()
        if sostoynie == 9:
            item = QtWidgets.QTableWidgetItem('j')
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setBackground(brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setForeground(brush)
            self.ui.tableWidget.setItem(row, col, item)
            if row == 0:
                table = 'Боинг-767'
            if row == 1:
                table = 'Боинг-777'
            if row == 2:
                table = 'Ил-96'
            if row == 3:
                table = 'Ту-134'
            if row == 4:
                table = 'Ту-154'
            item = 'j'
            cursor.execute("UPDATE " + "'" + table + "'" + " SET " + "'" + timing[col] + "'" + " = " + "'" + str(
                item) + "'" + " WHERE Data = " + "'" + str(data) + "'")
            conn.commit()
        if sostoynie == 10:
            item = QtWidgets.QTableWidgetItem('k')
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setBackground(brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setForeground(brush)
            self.ui.tableWidget.setItem(row, col, item)
            if row == 0:
                table = 'Боинг-767'
            if row == 1:
                table = 'Боинг-777'
            if row == 2:
                table = 'Ил-96'
            if row == 3:
                table = 'Ту-134'
            if row == 4:
                table = 'Ту-154'
            item = 'k'
            cursor.execute("UPDATE " + "'" + table + "'" + " SET " + "'" + timing[col] + "'" + " = " + "'" + str(
                item) + "'" + " WHERE Data = " + "'" + str(data) + "'")
            conn.commit()
        if sostoynie == 11:
            item = QtWidgets.QTableWidgetItem('l')
            brush = QtGui.QBrush(QtGui.QColor(150, 75, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setBackground(brush)
            brush = QtGui.QBrush(QtGui.QColor(150, 75, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setForeground(brush)
            self.ui.tableWidget.setItem(row, col, item)
            if row == 0:
                table = 'Боинг-767'
            if row == 1:
                table = 'Боинг-777'
            if row == 2:
                table = 'Ил-96'
            if row == 3:
                table = 'Ту-134'
            if row == 4:
                table = 'Ту-154'
            item = 'l'
            cursor.execute("UPDATE " + "'" + table + "'" + " SET " + "'" + timing[col] + "'" + " = " + "'" + str(
                item) + "'" + " WHERE Data = " + "'" + str(data) + "'")
            conn.commit()
        if sostoynie == 12:
            item = QtWidgets.QTableWidgetItem('m')
            brush = QtGui.QBrush(QtGui.QColor(150, 75, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setBackground(brush)
            brush = QtGui.QBrush(QtGui.QColor(150, 75, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setForeground(brush)
            self.ui.tableWidget.setItem(row, col, item)
            if row == 0:
                table = 'Боинг-767'
            if row == 1:
                table = 'Боинг-777'
            if row == 2:
                table = 'Ил-96'
            if row == 3:
                table = 'Ту-134'
            if row == 4:
                table = 'Ту-154'
            item = 'm'
            cursor.execute("UPDATE " + "'" + table + "'" + " SET " + "'" + timing[col] + "'" + " = " + "'" + str(
                item) + "'" + " WHERE Data = " + "'" + str(data) + "'")
            conn.commit()
        if sostoynie == 13:
            item = QtWidgets.QTableWidgetItem('n')
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setBackground(brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setForeground(brush)
            self.ui.tableWidget.setItem(row, col, item)
            if row == 0:
                table = 'Боинг-767'
            if row == 1:
                table = 'Боинг-777'
            if row == 2:
                table = 'Ил-96'
            if row == 3:
                table = 'Ту-134'
            if row == 4:
                table = 'Ту-154'
            item = 'n'
            cursor.execute("UPDATE " + "'" + table + "'" + " SET " + "'" + timing[col] + "'" + " = " + "'" + str(
                item) + "'" + " WHERE Data = " + "'" + str(data) + "'")
            conn.commit()
        if sostoynie == 14:
            item = QtWidgets.QTableWidgetItem('o')
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setBackground(brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setForeground(brush)
            self.ui.tableWidget.setItem(row, col, item)
            if row == 0:
                table = 'Боинг-767'
            if row == 1:
                table = 'Боинг-777'
            if row == 2:
                table = 'Ил-96'
            if row == 3:
                table = 'Ту-134'
            if row == 4:
                table = 'Ту-154'
            item = 'o'
            cursor.execute("UPDATE " + "'" + table + "'" + " SET " + "'" + timing[col] + "'" + " = " + "'" + str(
                item) + "'" + " WHERE Data = " + "'" + str(data) + "'")
            conn.commit()
        if sostoynie == 15:
            item = QtWidgets.QTableWidgetItem('p')
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setBackground(brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setForeground(brush)
            self.ui.tableWidget.setItem(row, col, item)
            if row == 0:
                table = 'Боинг-767'
            if row == 1:
                table = 'Боинг-777'
            if row == 2:
                table = 'Ил-96'
            if row == 3:
                table = 'Ту-134'
            if row == 4:
                table = 'Ту-154'
            item = 'p'
            cursor.execute("UPDATE " + "'" + table + "'" + " SET " + "'" + timing[col] + "'" + " = " + "'" + str(
                item) + "'" + " WHERE Data = " + "'" + str(data) + "'")
            conn.commit()
        if sostoynie == 16:
            item = QtWidgets.QTableWidgetItem('q')
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setBackground(brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setForeground(brush)
            self.ui.tableWidget.setItem(row, col, item)
            if row == 0:
                table = 'Боинг-767'
            if row == 1:
                table = 'Боинг-777'
            if row == 2:
                table = 'Ил-96'
            if row == 3:
                table = 'Ту-134'
            if row == 4:
                table = 'Ту-154'
            item = 'q'
            cursor.execute("UPDATE " + "'" + table + "'" + " SET " + "'" + timing[col] + "'" + " = " + "'" + str(
                item) + "'" + " WHERE Data = " + "'" + str(data) + "'")
            conn.commit()
        if sostoynie == 17:
            item = QtWidgets.QTableWidgetItem('r')
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setBackground(brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setForeground(brush)
            self.ui.tableWidget.setItem(row, col, item)
            if row == 0:
                table = 'Боинг-767'
            if row == 1:
                table = 'Боинг-777'
            if row == 2:
                table = 'Ил-96'
            if row == 3:
                table = 'Ту-134'
            if row == 4:
                table = 'Ту-154'
            item = 'r'
            cursor.execute("UPDATE " + "'" + table + "'" + " SET " + "'" + timing[col] + "'" + " = " + "'" + str(
                item) + "'" + " WHERE Data = " + "'" + str(data) + "'")
            conn.commit()
        if sostoynie == 18:
            item = QtWidgets.QTableWidgetItem('s')
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setBackground(brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setForeground(brush)
            self.ui.tableWidget.setItem(row, col, item)
            if row == 0:
                table = 'Боинг-767'
            if row == 1:
                table = 'Боинг-777'
            if row == 2:
                table = 'Ил-96'
            if row == 3:
                table = 'Ту-134'
            if row == 4:
                table = 'Ту-154'
            item = 's'
            cursor.execute("UPDATE " + "'" + table + "'" + " SET " + "'" + timing[col] + "'" + " = " + "'" + str(
                item) + "'" + " WHERE Data = " + "'" + str(data) + "'")
            conn.commit()
        if sostoynie == 19:
            item = QtWidgets.QTableWidgetItem('t')
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setBackground(brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setForeground(brush)
            self.ui.tableWidget.setItem(row, col, item)
            if row == 0:
                table = 'Боинг-767'
            if row == 1:
                table = 'Боинг-777'
            if row == 2:
                table = 'Ил-96'
            if row == 3:
                table = 'Ту-134'
            if row == 4:
                table = 'Ту-154'
            item = 't'
            cursor.execute("UPDATE " + "'" + table + "'" + " SET " + "'" + timing[col] + "'" + " = " + "'" + str(
                item) + "'" + " WHERE Data = " + "'" + str(data) + "'")
            conn.commit()
        if sostoynie == 20:
            item = QtWidgets.QTableWidgetItem('u')
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setBackground(brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setForeground(brush)
            self.ui.tableWidget.setItem(row, col, item)
            if row == 0:
                table = 'Боинг-767'
            if row == 1:
                table = 'Боинг-777'
            if row == 2:
                table = 'Ил-96'
            if row == 3:
                table = 'Ту-134'
            if row == 4:
                table = 'Ту-154'
            item = 'u'
            cursor.execute("UPDATE " + "'" + table + "'" + " SET " + "'" + timing[col] + "'" + " = " + "'" + str(
                item) + "'" + " WHERE Data = " + "'" + str(data) + "'")
            conn.commit()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
