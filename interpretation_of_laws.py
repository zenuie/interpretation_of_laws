# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interpretation_of_laws.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
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
        self.checkBrowse = QtWidgets.QPushButton(Dialog)
        self.checkBrowse.setGeometry(QtCore.QRect(420, 240, 61, 31))
        self.checkBrowse.setObjectName("checkBrowse")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 160, 471, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.regulation = QtWidgets.QComboBox(Dialog)
        self.regulation.setGeometry(QtCore.QRect(50, 70, 341, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.regulation.setFont(font)
        self.regulation.setObjectName("regulation")
        self.article = QtWidgets.QSpinBox(Dialog)
        self.article.setGeometry(QtCore.QRect(420, 70, 61, 41))
        self.article.setMinimum(1)
        self.article.setMaximum(400)
        self.article.setObjectName("article")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "營造業歷年法規匯入程式 for 二科"))
        self.checkOK.setText(_translate("Dialog", "確定"))
        self.checkCancel.setText(_translate("Dialog", "取消"))
        self.checkBrowse.setText(_translate("Dialog", "瀏覽"))
        self.label.setText(_translate("Dialog", "麻煩請先點選瀏覽選擇要匯入的檔案"))
