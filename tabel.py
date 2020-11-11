from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QTableWidgetItem
import sqlite3
from datetime import datetime
import openpyxl

from tabel_ui import *


class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Tabel()
        self.ui.setupUi(self)
        self.ui.comboBox.activated.connect(self.variant_air)
        self.ui.comboBox_2.activated.connect(self.activate_tabel)
        self.ui.tableWidget_3.cellClicked.connect(self.ycheika)
        self.variant_air()
        # Табель
        self.ui.tableWidget_3.verticalHeader().hide()
        self.ui.tableWidget_3.horizontalHeader().hide()
        self.ui.tableWidget_3.setSpan(0, 0, 2, 1)
        self.ui.tableWidget_3.setSpan(0, 1, 2, 2)
        self.ui.tableWidget_3.setSpan(0, 3, 2, 1)
        self.ui.tableWidget_3.setSpan(0, 4, 1, 30)
        self.ui.tableWidget_3.setSpan(0, 34, 2, 1)

        for i in range(2, 30):
            self.ui.tableWidget_3.setSpan(i, 1, 1, 2)

        conn = sqlite3.connect("bd.db")
        cursor = conn.cursor()

        self.ui.comboBox.addItem('Боинг-767')
        self.ui.comboBox.addItem('Боинг-777')
        self.ui.comboBox.addItem('Ил-96')
        self.ui.comboBox.addItem('Ту-134')
        self.ui.comboBox.addItem('Ту-154')

    def variant_air(self):
        conn = sqlite3.connect("bd.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM 'Боинг-767'")
        air = cursor.fetchall()
        if self.ui.comboBox.currentIndex() == 0:
            cursor.execute("SELECT * FROM 'Боинг-767'")
            air = cursor.fetchall()
        if self.ui.comboBox.currentIndex() == 1:
            cursor.execute("SELECT * FROM 'Боинг-777'")
            air = cursor.fetchall()
        if self.ui.comboBox.currentIndex() == 2:
            cursor.execute("SELECT * FROM 'Ил-96'")
            air = cursor.fetchall()
        if self.ui.comboBox.currentIndex() == 3:
            cursor.execute("SELECT * FROM 'Ту-134'")
            air = cursor.fetchall()
        if self.ui.comboBox.currentIndex() == 4:
            cursor.execute("SELECT * FROM 'Ту-154'")
            air = cursor.fetchall()
        self.ui.comboBox_2.clear()
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
            self.ui.comboBox_2.addItem(i)
        self.activate_tabel()

    def activate_tabel(self):
        bb = 2
        hh = 4
        for i in range(31):
            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(''))
            bb += 1
            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(''))
            bb += 1
            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(''))
            bb += 1
            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(''))
            bb += 1
            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(''))
            bb += 3
            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(''))
            bb += 1
            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(''))
            bb += 1
            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(''))
            bb += 1
            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(''))
            bb += 1
            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(''))
            bb += 1
            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(''))
            bb += 1
            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(''))
            bb += 1
            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(''))
            bb += 1
            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(''))
            bb += 1
            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(''))
            bb += 1
            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(''))
            bb += 1
            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(''))
            bb += 1
            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(''))
            bb += 1
            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(''))
            bb += 1
            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(''))
            bb += 1
            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(''))
            bb += 1
            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(''))
            hh += 1
            bb = 2
        conn = sqlite3.connect("bd.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM 'Боинг-767'")
        air = cursor.fetchall()
        if self.ui.comboBox.currentIndex() == 0:
            cursor.execute("SELECT * FROM 'Боинг-767'")
            air = cursor.fetchall()
        if self.ui.comboBox.currentIndex() == 1:
            cursor.execute("SELECT * FROM 'Боинг-777'")
            air = cursor.fetchall()
        if self.ui.comboBox.currentIndex() == 2:
            cursor.execute("SELECT * FROM 'Ил-96'")
            air = cursor.fetchall()
        if self.ui.comboBox.currentIndex() == 3:
            cursor.execute("SELECT * FROM 'Ту-134'")
            air = cursor.fetchall()
        if self.ui.comboBox.currentIndex() == 4:
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
        bb = 2
        hh = 4
        if self.ui.comboBox_2.currentText() == 'Декабрь':
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
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str((
                                                                                                   lenk + lene + lenm + leng + lena + leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 // 60) + ':' + str(
                                (
                                            lenk + lene + lenm + leng + lena + leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str(
                                    (lenk + lene + lenm + leng + lena) * 10 % 60)))
                            bb += 2
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str((
                                                                                                   leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 // 60) + ':' + str(
                                (
                                            leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 % 60)))
                            bb += 2
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(round((24 - ((
                                                                                                                leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10)) / (
                                                                                                         (
                                                                                                                     leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10),
                                                                                             2))))
                            hh += 1
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
                        bb = 2
        if self.ui.comboBox_2.currentText() == 'Ноябрь':
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
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str((
                                                                                                   lenk + lene + lenm + leng + lena + leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 // 60) + ':' + str(
                                (
                                            lenk + lene + lenm + leng + lena + leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str(
                                    (lenk + lene + lenm + leng + lena) * 10 % 60)))
                            bb += 2
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str((
                                                                                                   leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 // 60) + ':' + str(
                                (
                                            leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 % 60)))
                            bb += 2
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(round((24 - ((
                                                                                                                leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10)) / (
                                                                                                         (
                                                                                                                     leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10),
                                                                                             2))))
                            hh += 1
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
                        bb = 2
        if self.ui.comboBox_2.currentText() == 'Октябрь':
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
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str((lenk + lene + lenm + leng + lena + leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena + leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str((lenk + lene + lenm + leng + lena) * 10 % 60)))
                            bb += 2
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str((leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 // 60) + ':' + str((leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 % 60)))
                            bb += 2
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(round((24 - ((leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10)) / ((leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10),2))))
                            hh += 1
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
                        bb = 2
        if self.ui.comboBox_2.currentText() == 'Сентябрь':
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
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str((
                                                                                                   lenk + lene + lenm + leng + lena + leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 // 60) + ':' + str(
                                (
                                            lenk + lene + lenm + leng + lena + leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str(
                                    (lenk + lene + lenm + leng + lena) * 10 % 60)))
                            bb += 2
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str((
                                                                                                   leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 // 60) + ':' + str(
                                (
                                            leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 % 60)))
                            bb += 2
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(round((24 - ((
                                                                                                                leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10)) / (
                                                                                                         (
                                                                                                                     leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10),
                                                                                             2))))
                            hh += 1
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
                        bb = 2
        if self.ui.comboBox_2.currentText() == 'Август':
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
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str((
                                                                                                   lenk + lene + lenm + leng + lena + leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 // 60) + ':' + str(
                                (
                                            lenk + lene + lenm + leng + lena + leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str(
                                    (lenk + lene + lenm + leng + lena) * 10 % 60)))
                            bb += 2
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str((
                                                                                                   leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 // 60) + ':' + str(
                                (
                                            leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 % 60)))
                            bb += 2
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(round((24 - ((
                                                                                                                leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10)) / (
                                                                                                         (
                                                                                                                     leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10),
                                                                                             2))))
                            hh += 1
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
                        bb = 2
        if self.ui.comboBox_2.currentText() == 'Июль':
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
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str((
                                                                                                   lenk + lene + lenm + leng + lena + leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 // 60) + ':' + str(
                                (
                                            lenk + lene + lenm + leng + lena + leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str(
                                    (lenk + lene + lenm + leng + lena) * 10 % 60)))
                            bb += 2
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str((
                                                                                                   leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 // 60) + ':' + str(
                                (
                                            leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 % 60)))
                            bb += 2
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(round((24 - ((
                                                                                                                leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10)) / (
                                                                                                         (
                                                                                                                     leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10),
                                                                                             2))))
                            hh += 1
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
                        bb = 2
        if self.ui.comboBox_2.currentText() == 'Июнь':
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
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str((
                                                                                                   lenk + lene + lenm + leng + lena + leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 // 60) + ':' + str(
                                (
                                            lenk + lene + lenm + leng + lena + leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str(
                                    (lenk + lene + lenm + leng + lena) * 10 % 60)))
                            bb += 2
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str((
                                                                                                   leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 // 60) + ':' + str(
                                (
                                            leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 % 60)))
                            bb += 2
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(round((24 - ((
                                                                                                                leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10)) / (
                                                                                                         (
                                                                                                                     leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10),
                                                                                             2))))
                            hh += 1
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
                        bb = 2
        if self.ui.comboBox_2.currentText() == 'Май':
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
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str((
                                                                                                   lenk + lene + lenm + leng + lena + leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 // 60) + ':' + str(
                                (
                                            lenk + lene + lenm + leng + lena + leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str(
                                    (lenk + lene + lenm + leng + lena) * 10 % 60)))
                            bb += 2
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str((
                                                                                                   leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 // 60) + ':' + str(
                                (
                                            leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 % 60)))
                            bb += 2
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(round((24 - ((
                                                                                                                leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10)) / (
                                                                                                         (
                                                                                                                     leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10),
                                                                                             2))))
                            hh += 1
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
                        bb = 2
        if self.ui.comboBox_2.currentText() == 'Апрель':
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
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str((
                                                                                                   lenk + lene + lenm + leng + lena + leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 // 60) + ':' + str(
                                (
                                            lenk + lene + lenm + leng + lena + leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str(
                                    (lenk + lene + lenm + leng + lena) * 10 % 60)))
                            bb += 2
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str((
                                                                                                   leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 // 60) + ':' + str(
                                (
                                            leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 % 60)))
                            bb += 2
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(round((24 - ((
                                                                                                                leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10)) / (
                                                                                                         (
                                                                                                                     leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10),
                                                                                             2))))
                            hh += 1
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
                        bb = 2
        if self.ui.comboBox_2.currentText() == 'Март':
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
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str((
                                                                                                   lenk + lene + lenm + leng + lena + leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 // 60) + ':' + str(
                                (
                                            lenk + lene + lenm + leng + lena + leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str(
                                    (lenk + lene + lenm + leng + lena) * 10 % 60)))
                            bb += 2
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str((
                                                                                                   leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 // 60) + ':' + str(
                                (
                                            leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 % 60)))
                            bb += 2
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(round((24 - ((
                                                                                                                leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10)) / (
                                                                                                         (
                                                                                                                     leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10),
                                                                                             2))))
                            hh += 1
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
                        bb = 2
        if self.ui.comboBox_2.currentText() == 'Февраль':
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
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str((
                                                                                                   lenk + lene + lenm + leng + lena + leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 // 60) + ':' + str(
                                (
                                            lenk + lene + lenm + leng + lena + leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str(
                                    (lenk + lene + lenm + leng + lena) * 10 % 60)))
                            bb += 2
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str((
                                                                                                   leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 // 60) + ':' + str(
                                (
                                            leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 % 60)))
                            bb += 2
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(round((24 - ((
                                                                                                                leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10)) / (
                                                                                                         (
                                                                                                                     leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10),
                                                                                             2))))
                            hh += 1
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
                        bb = 2
        if self.ui.comboBox_2.currentText() == 'Январь':
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
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str((
                                                                                                   lenk + lene + lenm + leng + lena + leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 // 60) + ':' + str(
                                (
                                            lenk + lene + lenm + leng + lena + leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str((lenk + lene + lenm + leng + lena) * 10 // 60) + ':' + str(
                                    (lenk + lene + lenm + leng + lena) * 10 % 60)))
                            bb += 2
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenk * 10 // 60) + ':' + str(lenk * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lene * 10 // 60) + ':' + str(lene * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenm * 10 // 60) + ':' + str(lenm * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(leng * 10 // 60) + ':' + str(leng * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lena * 10 // 60) + ':' + str(lena * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str((
                                                                                                   leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 // 60) + ':' + str(
                                (
                                            leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10 % 60)))
                            bb += 2
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(leny * 10 // 60) + ':' + str(leny * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenob * 10 // 60) + ':' + str(lenob * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lentb * 10 // 60) + ':' + str(lentb * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenop * 10 // 60) + ':' + str(lenop * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lentp * 10 // 60) + ':' + str(lentp * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lensh * 10 // 60) + ':' + str(lensh * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenor * 10 // 60) + ':' + str(lenor * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenr * 10 // 60) + ':' + str(lenr * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenz * 10 // 60) + ':' + str(lenz * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lendv * 10 // 60) + ':' + str(lendv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lend * 10 // 60) + ':' + str(lend * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenj * 10 // 60) + ':' + str(lenj * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenjr * 10 // 60) + ':' + str(lenjr * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenl * 10 // 60) + ':' + str(lenl * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lenv * 10 // 60) + ':' + str(lenv * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(
                                str(lens * 10 // 60) + ':' + str(lens * 10 % 60)))
                            bb += 1
                            self.ui.tableWidget_3.setItem(bb, hh, QTableWidgetItem(str(round((24 - ((
                                                                                                                leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10)) / (
                                                                                                         (
                                                                                                                     leny + lenob + lentb + lenop + lentp + lendv + lensh + lenor + lenr + lenz + lendv + lend + lenj + lenjr + lenl + lenv + lens) * 10),
                                                                                             2))))
                            hh += 1
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
                        bb = 2
        self.vsego()

    def vsego(self):
        bb = 2
        hh = 4
        summ = 0
        for i in range(1, 776):
            if hh <= 33:
                q = self.ui.tableWidget_3.item(bb, hh).text().split(':')

                summ += int(q[0]) * 60 + int(q[1])
                hh += 1
            else:
                self.ui.tableWidget_3.setItem(bb, 34, QTableWidgetItem(str(summ // 60) + ':' + str(summ % 60)))
                summ = 0
                hh = 4
                bb += 1
                if bb == 4 or bb == 11:
                    bb += 1


    def ycheika(self):
        row = self.ui.tableWidget_3.currentRow()
        col = self.ui.tableWidget_3.currentColumn()
        print(row, col)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
