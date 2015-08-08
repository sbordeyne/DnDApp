# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\connect_window.ui'
#
# Created: Sat Aug  8 09:24:14 2015
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_connect_window(object):
    def setupUi(self, connect_window):
        connect_window.setObjectName(_fromUtf8("connect_window"))
        connect_window.resize(433, 298)
        connect_window.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.gridLayout = QtGui.QGridLayout(connect_window)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(connect_window)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label = QtGui.QLabel(connect_window)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(connect_window)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(connect_window)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(connect_window)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(connect_window)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.retranslateUi(connect_window)
        QtCore.QMetaObject.connectSlotsByName(connect_window)

    def retranslateUi(self, connect_window):
        connect_window.setWindowTitle(_translate("connect_window", "Connect to...", None))
        self.label_2.setText(_translate("connect_window", "Host IP :", None))
        self.label.setText(_translate("connect_window", "Port :", None))
        self.label_3.setText(_translate("connect_window", "Name :", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    connect_window = QtGui.QDialog()
    ui = Ui_connect_window()
    ui.setupUi(connect_window)
    connect_window.show()
    sys.exit(app.exec_())

