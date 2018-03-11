# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat Sep 24 22:48:41 2016
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
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.instr_label = QtGui.QLabel(self.centralWidget)
        self.instr_label.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.instr_label.setObjectName("instr_label")
        self.course_label = QtGui.QLabel(self.centralWidget)
        self.course_label.setGeometry(QtCore.QRect(10, 90, 101, 16))
        self.course_label.setObjectName("course_label")
        self.code_label = QtGui.QLabel(self.centralWidget)
        self.code_label.setGeometry(QtCore.QRect(290, 90, 91, 16))
        self.code_label.setObjectName("code_label")
        self.code_text = QtGui.QTextEdit(self.centralWidget)
        self.code_text.setEnabled(False)
        self.code_text.setGeometry(QtCore.QRect(290, 110, 141, 31))
        self.code_text.setObjectName("code_text")
        self.time_label = QtGui.QLabel(self.centralWidget)
        self.time_label.setGeometry(QtCore.QRect(10, 220, 111, 16))
        self.time_label.setObjectName("time_label")
        self.time_text = QtGui.QTextEdit(self.centralWidget)
        self.time_text.setEnabled(False)
        self.time_text.setGeometry(QtCore.QRect(120, 210, 61, 31))
        self.time_text.setObjectName("time_text")
        self.course_text = QtGui.QTextEdit(self.centralWidget)
        self.course_text.setEnabled(False)
        self.course_text.setGeometry(QtCore.QRect(10, 110, 251, 31))
        self.course_text.setObjectName("course_text")
        self.lect_text = QtGui.QTextEdit(self.centralWidget)
        self.lect_text.setEnabled(False)
        self.lect_text.setGeometry(QtCore.QRect(10, 40, 421, 31))
        self.lect_text.setObjectName("lect_text")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.instr_label.setText(QtGui.QApplication.translate("MainWindow", "Lecturer Name :", None, QtGui.QApplication.UnicodeUTF8))
        self.course_label.setText(QtGui.QApplication.translate("MainWindow", "Course Name :", None, QtGui.QApplication.UnicodeUTF8))
        self.code_label.setText(QtGui.QApplication.translate("MainWindow", "Course Code :", None, QtGui.QApplication.UnicodeUTF8))
        self.time_label.setText(QtGui.QApplication.translate("MainWindow", "Time to Session End :", None, QtGui.QApplication.UnicodeUTF8))
        self.time_text.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.course_text.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

