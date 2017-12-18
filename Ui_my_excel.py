# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\python gui\my_excel\my_excel.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(646, 472)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.textBrowser = QtGui.QTextBrowser(self.centralWidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 20, 601, 321))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 380, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 380, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.lineEdit = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 380, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(160, 380, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 646, 23))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuAbout = QtGui.QMenu(self.menuBar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/pic/icon/file.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionClose = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/pic/icon/setting.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon1)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionExit = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/pic/icon/exit.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon2)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/pic/icon/help.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon3)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionInstruction = QtGui.QAction(MainWindow)
        self.actionInstruction.setIcon(icon3)
        self.actionInstruction.setObjectName(_fromUtf8("actionInstruction"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionInstruction)
        self.menuAbout.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "choose file", None))
        self.pushButton_2.setText(_translate("MainWindow", "search", None))
        self.label.setText(_translate("MainWindow", "key word:", None))
        self.menuFile.setTitle(_translate("MainWindow", "file", None))
        self.menuHelp.setTitle(_translate("MainWindow", "help", None))
        self.menuAbout.setTitle(_translate("MainWindow", "about", None))
        self.actionOpen.setText(_translate("MainWindow", "open", None))
        self.actionClose.setText(_translate("MainWindow", "close", None))
        self.actionExit.setText(_translate("MainWindow", "exit", None))
        self.actionAbout.setText(_translate("MainWindow", "about", None))
        self.actionInstruction.setText(_translate("MainWindow", "instruction", None))

import my_pic_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

