# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stock_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1237, 790)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 140, 911, 351))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 20, 1001, 31))
        self.label_2.setObjectName("label_2")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(1140, 710, 81, 31))
        self.exit.setObjectName("exit")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(1002, 600, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton.setFont(font)
        self.toolButton.setObjectName("toolButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 550, 911, 171))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(11)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(1020, 130, 123, 34))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.search.setFont(font)
        self.search.setObjectName("search")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 510, 911, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.oned = QtWidgets.QPushButton(self.layoutWidget)
        self.oned.setObjectName("oned")
        self.horizontalLayout.addWidget(self.oned)
        self.fived = QtWidgets.QPushButton(self.layoutWidget)
        self.fived.setObjectName("fived")
        self.horizontalLayout.addWidget(self.fived)
        self.onem = QtWidgets.QPushButton(self.layoutWidget)
        self.onem.setObjectName("onem")
        self.horizontalLayout.addWidget(self.onem)
        self.sixm = QtWidgets.QPushButton(self.layoutWidget)
        self.sixm.setObjectName("sixm")
        self.horizontalLayout.addWidget(self.sixm)
        self.oney = QtWidgets.QPushButton(self.layoutWidget)
        self.oney.setObjectName("oney")
        self.horizontalLayout.addWidget(self.oney)
        self.twoy = QtWidgets.QPushButton(self.layoutWidget)
        self.twoy.setObjectName("twoy")
        self.horizontalLayout.addWidget(self.twoy)
        self.fivey = QtWidgets.QPushButton(self.layoutWidget)
        self.fivey.setObjectName("fivey")
        self.horizontalLayout.addWidget(self.fivey)
        self.max = QtWidgets.QPushButton(self.layoutWidget)
        self.max.setObjectName("max")
        self.horizontalLayout.addWidget(self.max)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 70, 931, 64))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.code = QtWidgets.QLineEdit(self.layoutWidget1)
        self.code.setText("")
        self.code.setObjectName("code")
        self.horizontalLayout_2.addWidget(self.code)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.start = QtWidgets.QLineEdit(self.layoutWidget1)
        self.start.setText("")
        self.start.setObjectName("start")
        self.horizontalLayout_2.addWidget(self.start)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.end = QtWidgets.QLineEdit(self.layoutWidget1)
        self.end.setText("")
        self.end.setObjectName("end")
        self.horizontalLayout_2.addWidget(self.end)
        self.treemap = QtWidgets.QPushButton(self.centralwidget)
        self.treemap.setGeometry(QtCore.QRect(1020, 460, 123, 34))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.treemap.setFont(font)
        self.treemap.setObjectName("treemap")
        self.index = QtWidgets.QToolButton(self.centralwidget)
        self.index.setGeometry(QtCore.QRect(1020, 420, 123, 34))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.index.setFont(font)
        self.index.setObjectName("index")
        self.industrymap = QtWidgets.QPushButton(self.centralwidget)
        self.industrymap.setGeometry(QtCore.QRect(1020, 500, 123, 34))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.industrymap.setFont(font)
        self.industrymap.setObjectName("industrymap")
        self.today = QtWidgets.QPushButton(self.centralwidget)
        self.today.setGeometry(QtCore.QRect(1020, 330, 123, 34))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.today.setFont(font)
        self.today.setObjectName("today")
        self.areachart = QtWidgets.QPushButton(self.centralwidget)
        self.areachart.setGeometry(QtCore.QRect(1020, 540, 123, 34))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.areachart.setFont(font)
        self.areachart.setObjectName("areachart")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1000, 380, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1000, 90, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.rate = QtWidgets.QPushButton(self.centralwidget)
        self.rate.setGeometry(QtCore.QRect(1020, 210, 123, 34))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.rate.setFont(font)
        self.rate.setObjectName("rate")
        self.oc = QtWidgets.QPushButton(self.centralwidget)
        self.oc.setGeometry(QtCore.QRect(1020, 250, 123, 34))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.oc.setFont(font)
        self.oc.setObjectName("oc")
        self.volume = QtWidgets.QPushButton(self.centralwidget)
        self.volume.setGeometry(QtCore.QRect(1020, 170, 123, 34))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.volume.setFont(font)
        self.volume.setObjectName("volume")
        self.hl = QtWidgets.QPushButton(self.centralwidget)
        self.hl.setGeometry(QtCore.QRect(1020, 290, 123, 34))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.hl.setFont(font)
        self.hl.setObjectName("hl")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1237, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Stock Information Search</span></p></body></html>"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        self.toolButton.setText(_translate("MainWindow", "multiple stocks"))
        self.search.setText(_translate("MainWindow", "Search"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Date range:</span></p></body></html>"))
        self.oned.setText(_translate("MainWindow", "1 Day"))
        self.fived.setText(_translate("MainWindow", "5 Days"))
        self.onem.setText(_translate("MainWindow", "1 Month"))
        self.sixm.setText(_translate("MainWindow", "6 Months"))
        self.oney.setText(_translate("MainWindow", "1 Year"))
        self.twoy.setText(_translate("MainWindow", "2 Years"))
        self.fivey.setText(_translate("MainWindow", "5 Years"))
        self.max.setText(_translate("MainWindow", "Max"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Please enter the stock code:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Start date:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">End date:</span></p></body></html>"))
        self.treemap.setText(_translate("MainWindow", "Treemap"))
        self.index.setText(_translate("MainWindow", "Check index"))
        self.industrymap.setText(_translate("MainWindow", "Industry Map"))
        self.today.setText(_translate("MainWindow", "Show today"))
        self.areachart.setText(_translate("MainWindow", "Area Chart"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Stock Market</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Individual stocks</span></p></body></html>"))
        self.rate.setText(_translate("MainWindow", "rate"))
        self.oc.setText(_translate("MainWindow", "Open and Close"))
        self.volume.setText(_translate("MainWindow", "volume"))
        self.hl.setText(_translate("MainWindow", "High and Low"))
