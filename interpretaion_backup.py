# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interpretation_of_laws.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def __init__(self):
        super().__init__()
        self.retranslateUi()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(505, 581)
        self.splitter_2 = QtWidgets.QSplitter(Dialog)
        self.splitter_2.setGeometry(QtCore.QRect(140, 460, 221, 31))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.checkOK = QtWidgets.QPushButton(self.splitter_2)
        self.checkOK.setObjectName("checkOK")
        self.checkCancel = QtWidgets.QPushButton(self.splitter_2)
        self.checkCancel.setObjectName("checkCancel")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(50, 70, 401, 51))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.regulation = QtWidgets.QComboBox(self.splitter)
        self.regulation.setObjectName("comboBox")
        self.article = QtWidgets.QComboBox(self.splitter)
        self.article.setObjectName("comboBox_2")
        self.checkBrowse = QtWidgets.QPushButton(Dialog)
        self.checkBrowse.setGeometry(QtCore.QRect(400, 160, 51, 31))
        self.checkBrowse.setObjectName("checkBrowse")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 160, 341, 31))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.checkOK.setText(_translate("Dialog", "確定"))
        self.checkCancel.setText(_translate("Dialog", "取消"))
        self.checkBrowse.setText(_translate("Dialog", "瀏覽"))
