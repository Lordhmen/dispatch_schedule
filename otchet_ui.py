# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'otchet_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_otchet(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1203, 675)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 1051, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(787, 20, 181, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 1201, 541))
        self.tableWidget_2.setStyleSheet("")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(26)
        self.tableWidget_2.setRowCount(13)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(25, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_2.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_2.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_2.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_2.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_2.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_2.setItem(1, 10, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setItem(1, 11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_2.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_2.setItem(2, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_2.setItem(3, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_2.setItem(3, 6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_2.setItem(3, 7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_2.setItem(3, 8, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_2.setItem(3, 9, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_2.setItem(3, 10, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_2.setItem(3, 11, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_2.setItem(3, 12, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_2.setItem(3, 13, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_2.setItem(3, 14, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_2.setItem(3, 15, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_2.setItem(3, 16, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_2.setItem(3, 17, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_2.setItem(3, 18, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_2.setItem(3, 19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(3, 20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(3, 21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(3, 22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(3, 23, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(3, 24, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(3, 25, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(6, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(7, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(8, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(8, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(9, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(9, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(9, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(10, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(10, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(10, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(11, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(11, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(11, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(11, 3, item)
        self.verticalLayout.addWidget(self.frame_2)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1203, 26))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Отчет"))
        self.label.setText(_translate("mainWindow", "Отчет об исправности и использовании самолетов и вертолетов за_____________  2020г."))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("mainWindow", "New Row"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("mainWindow", "New Row"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("mainWindow", "New Row"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("mainWindow", "New Row"))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("mainWindow", "New Row"))
        item = self.tableWidget_2.verticalHeaderItem(5)
        item.setText(_translate("mainWindow", "New Row"))
        item = self.tableWidget_2.verticalHeaderItem(6)
        item.setText(_translate("mainWindow", "New Row"))
        item = self.tableWidget_2.verticalHeaderItem(7)
        item.setText(_translate("mainWindow", "New Row"))
        item = self.tableWidget_2.verticalHeaderItem(8)
        item.setText(_translate("mainWindow", "New Row"))
        item = self.tableWidget_2.verticalHeaderItem(9)
        item.setText(_translate("mainWindow", "New Row"))
        item = self.tableWidget_2.verticalHeaderItem(10)
        item.setText(_translate("mainWindow", "New Row"))
        item = self.tableWidget_2.verticalHeaderItem(11)
        item.setText(_translate("mainWindow", "New Row"))
        item = self.tableWidget_2.verticalHeaderItem(12)
        item.setText(_translate("mainWindow", "New Row"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("mainWindow", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("mainWindow", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("mainWindow", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("mainWindow", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("mainWindow", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("mainWindow", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(8)
        item.setText(_translate("mainWindow", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(9)
        item.setText(_translate("mainWindow", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(10)
        item.setText(_translate("mainWindow", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(11)
        item.setText(_translate("mainWindow", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(12)
        item.setText(_translate("mainWindow", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(13)
        item.setText(_translate("mainWindow", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(14)
        item.setText(_translate("mainWindow", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(15)
        item.setText(_translate("mainWindow", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(16)
        item.setText(_translate("mainWindow", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(17)
        item.setText(_translate("mainWindow", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(18)
        item.setText(_translate("mainWindow", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(19)
        item.setText(_translate("mainWindow", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(20)
        item.setText(_translate("mainWindow", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(21)
        item.setText(_translate("mainWindow", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(22)
        item.setText(_translate("mainWindow", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(23)
        item.setText(_translate("mainWindow", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(24)
        item.setText(_translate("mainWindow", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(25)
        item.setText(_translate("mainWindow", "New Column"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        item = self.tableWidget_2.item(0, 0)
        item.setText(_translate("mainWindow", "№ п/п"))
        item = self.tableWidget_2.item(0, 1)
        item.setText(_translate("mainWindow", "Тип самолета"))
        item = self.tableWidget_2.item(0, 2)
        item.setText(_translate("mainWindow", "Количество самолетов"))
        item = self.tableWidget_2.item(0, 3)
        item.setText(_translate("mainWindow", "Календарный фонд времени самолето-час"))
        item = self.tableWidget_2.item(0, 4)
        item.setText(_translate("mainWindow", "Сведения о распределении фонда времени по состояниям эксплуатации"))
        item = self.tableWidget_2.item(1, 4)
        item.setText(_translate("mainWindow", "Исправные"))
        item = self.tableWidget_2.item(1, 10)
        item.setText(_translate("mainWindow", "Неисправные"))
        item = self.tableWidget_2.item(2, 4)
        item.setText(_translate("mainWindow", "Всего исправных самолето-час"))
        item = self.tableWidget_2.item(2, 5)
        item.setText(_translate("mainWindow", "в том числе"))
        item = self.tableWidget_2.item(3, 5)
        item.setText(_translate("mainWindow", "время в рейсе"))
        item = self.tableWidget_2.item(3, 6)
        item.setText(_translate("mainWindow", "обеспечение вылета"))
        item = self.tableWidget_2.item(3, 7)
        item.setText(_translate("mainWindow", "в резерве"))
        item = self.tableWidget_2.item(3, 8)
        item.setText(_translate("mainWindow", "простой по метеоусловиям и запретам"))
        item = self.tableWidget_2.item(3, 9)
        item.setText(_translate("mainWindow", "исправные, не совершающие полетов"))
        item = self.tableWidget_2.item(3, 10)
        item.setText(_translate("mainWindow", "устранение неисправностейпо Ф-Б"))
        item = self.tableWidget_2.item(3, 11)
        item.setText(_translate("mainWindow", "ожидание обслуживания по ф-б"))
        item = self.tableWidget_2.item(3, 12)
        item.setText(_translate("mainWindow", "обслуживание по ф-б"))
        item = self.tableWidget_2.item(3, 13)
        item.setText(_translate("mainWindow", "ожидание переодического ТО"))
        item = self.tableWidget_2.item(3, 14)
        item.setText(_translate("mainWindow", "переодическое ТО"))
        item = self.tableWidget_2.item(3, 15)
        item.setText(_translate("mainWindow", "смена двигателя"))
        item = self.tableWidget_2.item(3, 16)
        item.setText(_translate("mainWindow", "ночные и межсменные простои"))
        item = self.tableWidget_2.item(3, 17)
        item.setText(_translate("mainWindow", "ожидание ремонт"))
        item = self.tableWidget_2.item(3, 18)
        item.setText(_translate("mainWindow", "в ремонте"))
        item = self.tableWidget_2.item(3, 19)
        item.setText(_translate("mainWindow", "отсутствие запчастей"))
        item = self.tableWidget_2.item(3, 20)
        item.setText(_translate("mainWindow", "дороботка по бюллетеням"))
        item = self.tableWidget_2.item(3, 21)
        item.setText(_translate("mainWindow", "рекламация промышленности"))
        item = self.tableWidget_2.item(3, 22)
        item.setText(_translate("mainWindow", "рекламация ремзаводам"))
        item = self.tableWidget_2.item(3, 23)
        item.setText(_translate("mainWindow", "расследование происшествий"))
        item = self.tableWidget_2.item(3, 24)
        item.setText(_translate("mainWindow", "восстановление после происшествия"))
        item = self.tableWidget_2.item(3, 25)
        item.setText(_translate("mainWindow", "ожидание списания"))
        item = self.tableWidget_2.item(7, 0)
        item.setText(_translate("mainWindow", "1"))
        item = self.tableWidget_2.item(7, 1)
        item.setText(_translate("mainWindow", "Ту-134"))
        item = self.tableWidget_2.item(7, 2)
        item.setText(_translate("mainWindow", "1"))
        item = self.tableWidget_2.item(7, 3)
        item.setText(_translate("mainWindow", "720:00"))
        item = self.tableWidget_2.item(8, 0)
        item.setText(_translate("mainWindow", "2"))
        item = self.tableWidget_2.item(8, 1)
        item.setText(_translate("mainWindow", "Ил-96"))
        item = self.tableWidget_2.item(8, 2)
        item.setText(_translate("mainWindow", "1"))
        item = self.tableWidget_2.item(8, 3)
        item.setText(_translate("mainWindow", "720:00"))
        item = self.tableWidget_2.item(9, 0)
        item.setText(_translate("mainWindow", "3"))
        item = self.tableWidget_2.item(9, 1)
        item.setText(_translate("mainWindow", "Боинг-767"))
        item = self.tableWidget_2.item(9, 2)
        item.setText(_translate("mainWindow", "1"))
        item = self.tableWidget_2.item(9, 3)
        item.setText(_translate("mainWindow", "720:00"))
        item = self.tableWidget_2.item(10, 0)
        item.setText(_translate("mainWindow", "4"))
        item = self.tableWidget_2.item(10, 1)
        item.setText(_translate("mainWindow", "Боинг-777"))
        item = self.tableWidget_2.item(10, 2)
        item.setText(_translate("mainWindow", "1"))
        item = self.tableWidget_2.item(10, 3)
        item.setText(_translate("mainWindow", "720:00"))
        item = self.tableWidget_2.item(11, 0)
        item.setText(_translate("mainWindow", "5"))
        item = self.tableWidget_2.item(11, 1)
        item.setText(_translate("mainWindow", "Ту-154"))
        item = self.tableWidget_2.item(11, 2)
        item.setText(_translate("mainWindow", "1"))
        item = self.tableWidget_2.item(11, 3)
        item.setText(_translate("mainWindow", "720:00"))
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
