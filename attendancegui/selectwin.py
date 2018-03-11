# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectwindow.ui'
#
# Created: Sat Sep 24 22:50:12 2016
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
        self.course_listWidget = QtGui.QListWidget(self.centralwidget)
        self.course_listWidget.setGeometry(QtCore.QRect(90, 60, 301, 201))
        self.course_listWidget.setObjectName("course_listWidget")
        self.select_label = QtGui.QLabel(self.centralwidget)
        self.select_label.setGeometry(QtCore.QRect(20, 30, 121, 16))
        self.select_label.setObjectName("select_label")
        self.nxt_btn = QtGui.QPushButton(self.centralwidget)
        self.nxt_btn.setGeometry(QtCore.QRect(350, 280, 91, 23))
        self.nxt_btn.setObjectName("nxt_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.select_label.setText(QtGui.QApplication.translate("MainWindow", "Select Current Course :", None, QtGui.QApplication.UnicodeUTF8))
        self.nxt_btn.setText(QtGui.QApplication.translate("MainWindow", "Next >>", None, QtGui.QApplication.UnicodeUTF8))

