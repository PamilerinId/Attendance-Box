# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studshowindow.ui'
#
# Created: Sat Sep 24 22:50:39 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stud_label = QtGui.QLabel(self.centralwidget)
        self.stud_label.setGeometry(QtCore.QRect(20, 20, 131, 16))
        self.stud_label.setObjectName("stud_label")
        self.stud_listWidget = QtGui.QListWidget(self.centralwidget)
        self.stud_listWidget.setEnabled(False)
        self.stud_listWidget.setGeometry(QtCore.QRect(55, 60, 351, 231))
        self.stud_listWidget.setObjectName("stud_listWidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.stud_label.setText(QtGui.QApplication.translate("MainWindow", "List of Students Present :", None, QtGui.QApplication.UnicodeUTF8))

