from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QTableWidgetItem
import sqlite3
from datetime import datetime
import openpyxl

from otchet_ui import *


class MyWinn(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_otchet()
        self.ui.setupUi(self)
        self.ui.tableWidget_2.verticalHeader().hide()
        self.ui.tableWidget_2.horizontalHeader().hide()
        self.ui.comboBox.activated.connect(self.start_onchet)
        self.ui.tableWidget_2.cellClicked.connect(self.ycheika)

        # Отчет
        for i in range(20):
            self.ui.tableWidget_2.setSpan(0, i, 7, 1)

        self.ui.tableWidget_2.setSpan(0, 4, 2, 1)

        for i in range(5, 10):
            self.ui.tableWidget_2.setSpan(0, i, 1, 1)

        for i in range(10, 20):
            self.ui.tableWidget_2.setSpan(0, i, 1, 1)
            self.ui.tableWidget_2.setSpan(1, i, 2, 1)

        self.ui.tableWidget_2.setSpan(0, 4, 1, 1)
        self.ui.tableWidget_2.setSpan(0, 4, 1, 23)
        self.ui.tableWidget_2.setSpan(1, 4, 1, 6)
        self.ui.tableWidget_2.setSpan(2, 5, 1, 5)

        self.ui.tableWidget_2.setSpan(1, 10, 2, 10)
        self.ui.tableWidget_2.setSpan(2, 4, 5, 1)

        for i in range(4, 26):
            self.ui.tableWidget_2.setSpan(3, i, 4, 1)

        # print(self.ui.tableWidget_3.item(5, 5).text())

        conn = sqlite3.connect("bd.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM 'Боинг-767'")
        air = cursor.fetchall()
        self.ui.comboBox.clear()
        mesyc = []
        for i in air:
            check_m = i[0].split('.')
            if check_m[1] == '01':
                mesyc.append('Январь')
            if check_m[1] == '02':
                mesyc.append('Февраль')
            if check_m[1] == '03':
                mesyc.append('Март')
            if check_m[1] == '04':
                mesyc.append('Апрель')
            if check_m[1] == '05':
                mesyc.append('Май')
            if check_m[1] == '06':
                mesyc.append('Июнь')
            if check_m[1] == '07':
                mesyc.append('Июль')
            if check_m[1] == '08':
                mesyc.append('Август')
            if check_m[1] == '09':
                mesyc.append('Сентябрь')
            if check_m[1] == '10':
                mesyc.append('Октябрь')
            if check_m[1] == '11':
                mesyc.append('Ноябрь')
            if check_m[1] == '12':
                mesyc.append('Декабрь')
        mesyc = list(set(mesyc))
        for i in mesyc:
            self.ui.comboBox.addItem(i)
        self.start_onchet()
    def ycheika(self):
        row = self.ui.tableWidget_2.currentRow()
        col = self.ui.tableWidget_2.currentColumn()
        print(row, col)
    def start_onchet(self):
        conn = sqlite3.connect("bd.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM 'Ту-134'")
        air = cursor.fetchall()
        lenk = 0
        lene = 0
        lenm = 0
        leng = 0
        lena = 0
        leny = 0
        lenob = 0
        lentb = 0
        lenop = 0
        lentp = 0
        lendv = 0
        lensh = 0
        lenor = 0
        lenr = 0
        lenz = 0
        lend = 0
        lenj = 0
        lenjr = 0
        lenl = 0
        lenv = 0
        lens = 0
        if self.ui.comboBox.currentText() == 'Декабрь':
            for i in air:
                if i[0].split('.')[1] == '12':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(7, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Январь':
            for i in air:
                if i[0].split('.')[1] == '01':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(7, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Февраль':
            for i in air:
                if i[0].split('.')[1] == '02':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(7, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Март':
            for i in air:
                if i[0].split('.')[1] == '03':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(7, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Апрель':
            for i in air:
                if i[0].split('.')[1] == '04':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(7, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Май':
            for i in air:
                if i[0].split('.')[1] == '05':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(7, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Июнь':
            for i in air:
                if i[0].split('.')[1] == '06':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(7, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Июль':
            for i in air:
                if i[0].split('.')[1] == '07':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(7, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Август':
            for i in air:
                if i[0].split('.')[1] == '08':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(7, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Сентябрь':
            for i in air:
                if i[0].split('.')[1] == '09':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(7, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Октябрь':
            for i in air:
                if i[0].split('.')[1] == '10':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(7, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Ноябрь':
            for i in air:
                if i[0].split('.')[1] == '11':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(7, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(7, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        cursor.execute("SELECT * FROM 'Ил-96'")
        air = cursor.fetchall()
        lenk = 0
        lene = 0
        lenm = 0
        leng = 0
        lena = 0
        leny = 0
        lenob = 0
        lentb = 0
        lenop = 0
        lentp = 0
        lendv = 0
        lensh = 0
        lenor = 0
        lenr = 0
        lenz = 0
        lend = 0
        lenj = 0
        lenjr = 0
        lenl = 0
        lenv = 0
        lens = 0
        if self.ui.comboBox.currentText() == 'Декабрь':
            for i in air:
                if i[0].split('.')[1] == '12':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(8, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Январь':
            for i in air:
                if i[0].split('.')[1] == '01':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(8, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Февраль':
            for i in air:
                if i[0].split('.')[1] == '02':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(8, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Март':
            for i in air:
                if i[0].split('.')[1] == '03':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(8, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Апрель':
            for i in air:
                if i[0].split('.')[1] == '04':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(8, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Май':
            for i in air:
                if i[0].split('.')[1] == '05':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(8, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Июнь':
            for i in air:
                if i[0].split('.')[1] == '06':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(8, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Июль':
            for i in air:
                if i[0].split('.')[1] == '07':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(8, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Август':
            for i in air:
                if i[0].split('.')[1] == '08':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(8, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Сентябрь':
            for i in air:
                if i[0].split('.')[1] == '09':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(8, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Октябрь':
            for i in air:
                if i[0].split('.')[1] == '10':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(8, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Ноябрь':
            for i in air:
                if i[0].split('.')[1] == '11':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(8, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(8, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        cursor.execute("SELECT * FROM 'Ту-154'")
        air = cursor.fetchall()
        lenk = 0
        lene = 0
        lenm = 0
        leng = 0
        lena = 0
        leny = 0
        lenob = 0
        lentb = 0
        lenop = 0
        lentp = 0
        lendv = 0
        lensh = 0
        lenor = 0
        lenr = 0
        lenz = 0
        lend = 0
        lenj = 0
        lenjr = 0
        lenl = 0
        lenv = 0
        lens = 0
        if self.ui.comboBox.currentText() == 'Декабрь':
            for i in air:
                if i[0].split('.')[1] == '12':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(11, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Январь':
            for i in air:
                if i[0].split('.')[1] == '01':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(11, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Февраль':
            for i in air:
                if i[0].split('.')[1] == '02':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(11, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Март':
            for i in air:
                if i[0].split('.')[1] == '03':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(11, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Апрель':
            for i in air:
                if i[0].split('.')[1] == '04':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(11, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Май':
            for i in air:
                if i[0].split('.')[1] == '05':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(11, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Июнь':
            for i in air:
                if i[0].split('.')[1] == '06':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(11, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Июль':
            for i in air:
                if i[0].split('.')[1] == '07':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(11, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Август':
            for i in air:
                if i[0].split('.')[1] == '08':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(11, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Сентябрь':
            for i in air:
                if i[0].split('.')[1] == '09':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(11, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Октябрь':
            for i in air:
                if i[0].split('.')[1] == '10':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(11, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Ноябрь':
            for i in air:
                if i[0].split('.')[1] == '11':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(11, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(11, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        cursor.execute("SELECT * FROM 'Боинг-777'")
        air = cursor.fetchall()
        lenk = 0
        lene = 0
        lenm = 0
        leng = 0
        lena = 0
        leny = 0
        lenob = 0
        lentb = 0
        lenop = 0
        lentp = 0
        lendv = 0
        lensh = 0
        lenor = 0
        lenr = 0
        lenz = 0
        lend = 0
        lenj = 0
        lenjr = 0
        lenl = 0
        lenv = 0
        lens = 0
        if self.ui.comboBox.currentText() == 'Декабрь':
            for i in air:
                if i[0].split('.')[1] == '12':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(10, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Январь':
            for i in air:
                if i[0].split('.')[1] == '01':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(10, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Февраль':
            for i in air:
                if i[0].split('.')[1] == '02':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(10, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Март':
            for i in air:
                if i[0].split('.')[1] == '03':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(10, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Апрель':
            for i in air:
                if i[0].split('.')[1] == '04':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(10, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Май':
            for i in air:
                if i[0].split('.')[1] == '05':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(10, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Июнь':
            for i in air:
                if i[0].split('.')[1] == '06':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(10, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Июль':
            for i in air:
                if i[0].split('.')[1] == '07':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(10, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Август':
            for i in air:
                if i[0].split('.')[1] == '08':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(10, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Сентябрь':
            for i in air:
                if i[0].split('.')[1] == '09':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(10, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Октябрь':
            for i in air:
                if i[0].split('.')[1] == '10':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(10, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Ноябрь':
            for i in air:
                if i[0].split('.')[1] == '11':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(10, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(10, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        cursor.execute("SELECT * FROM 'Боинг-767'")
        air = cursor.fetchall()
        lenk = 0
        lene = 0
        lenm = 0
        leng = 0
        lena = 0
        leny = 0
        lenob = 0
        lentb = 0
        lenop = 0
        lentp = 0
        lendv = 0
        lensh = 0
        lenor = 0
        lenr = 0
        lenz = 0
        lend = 0
        lenj = 0
        lenjr = 0
        lenl = 0
        lenv = 0
        lens = 0
        if self.ui.comboBox.currentText() == 'Декабрь':
            for i in air:
                if i[0].split('.')[1] == '12':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(9, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Январь':
            for i in air:
                if i[0].split('.')[1] == '01':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(9, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Февраль':
            for i in air:
                if i[0].split('.')[1] == '02':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(9, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Март':
            for i in air:
                if i[0].split('.')[1] == '03':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(9, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Апрель':
            for i in air:
                if i[0].split('.')[1] == '04':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(9, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Май':
            for i in air:
                if i[0].split('.')[1] == '05':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(9, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Июнь':
            for i in air:
                if i[0].split('.')[1] == '06':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(9, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Июль':
            for i in air:
                if i[0].split('.')[1] == '07':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(9, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Август':
            for i in air:
                if i[0].split('.')[1] == '08':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(9, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Сентябрь':
            for i in air:
                if i[0].split('.')[1] == '09':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(9, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Октябрь':
            for i in air:
                if i[0].split('.')[1] == '10':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(9, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
        if self.ui.comboBox.currentText() == 'Ноябрь':
            for i in air:
                if i[0].split('.')[1] == '11':
                    for l in range(1, 31):
                        if i[0].split('.')[0] == str(l):
                            for j in i:
                                if j == 'a':
                                    lenk += 1
                                if j == 'b':
                                    lene += 1
                                if j == 'c':
                                    lenm += 1
                                if j == 'd':
                                    leng += 1
                                if j == 'e':
                                    lena += 1
                                if j == 'f':
                                    leny += 1
                                if j == 'g':
                                    lenob += 1
                                if j == 'h':
                                    lentb += 1
                                if j == 'i':
                                    lenop += 1
                                if j == 'j':
                                    lentp += 1
                                if j == 'o':
                                    lendv += 1
                                if j == 'k':
                                    lensh += 1
                                if j == 'l':
                                    lenor += 1
                                if j == 'm':
                                    lenr += 1
                                if j == 'n':
                                    lenz += 1
                                if j == 'p':
                                    lend += 1
                                if j == 'q':
                                    lenj += 1
                                if j == 'r':
                                    lenjr += 1
                                if j == 's':
                                    lenl += 1
                                if j == 't':
                                    lenv += 1
                                if j == 'u':
                                    lens += 1
                            self.ui.tableWidget_2.setItem(9, 4, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 5, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 6, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 8, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 7, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 9, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 10, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 11, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 12, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 13, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 14, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 15, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 16, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 17, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 18, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 19, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 20, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 21, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 22, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 23, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 24, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            self.ui.tableWidget_2.setItem(9, 25, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWinn()
    myapp.show()
    sys.exit(app.exec_())
