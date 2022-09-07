# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1109, 675)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.DevicesBox = QtWidgets.QComboBox(self.centralwidget)
        self.DevicesBox.setGeometry(QtCore.QRect(70, 10, 69, 22))
        self.DevicesBox.setObjectName("DevicesBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 10, 54, 12))
        self.label_2.setObjectName("label_2")
        self.FindNumberEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.FindNumberEdit.setGeometry(QtCore.QRect(220, 10, 161, 20))
        self.FindNumberEdit.setObjectName("FindNumberEdit")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(10, 40, 1081, 301))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.FindNumberButton = QtWidgets.QPushButton(self.centralwidget)
        self.FindNumberButton.setGeometry(QtCore.QRect(390, 10, 51, 23))
        self.FindNumberButton.setObjectName("FindNumberButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 350, 1081, 221))
        self.listWidget.setObjectName("listWidget")
        self.ResButton = QtWidgets.QPushButton(self.centralwidget)
        self.ResButton.setGeometry(QtCore.QRect(10, 590, 75, 23))
        self.ResButton.setObjectName("ResButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1109, 22))
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
        self.label.setText(_translate("MainWindow", "设备选择"))
        self.label_2.setText(_translate("MainWindow", "号码查询"))
        self.FindNumberButton.setText(_translate("MainWindow", "查询"))
        self.ResButton.setText(_translate("MainWindow", "刷新短信"))
