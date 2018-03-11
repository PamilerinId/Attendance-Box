# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studshowindow.ui'
#
# Created: Thu Aug 25 10:24:43 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 320)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stud_label = QtGui.QLabel(self.centralwidget)
        self.stud_label.setGeometry(QtCore.QRect(20, 20, 131, 16))
        self.stud_label.setObjectName("stud_label")
        self.stud_listView = QtGui.QListView(self.centralwidget)
        self.stud_listView.setGeometry(QtCore.QRect(45, 50, 351, 241))
        self.stud_listView.setObjectName("stud_listView")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.stud_label.setText(QtGui.QApplication.translate("MainWindow", "List of Students Present :", None, QtGui.QApplication.UnicodeUTF8))

