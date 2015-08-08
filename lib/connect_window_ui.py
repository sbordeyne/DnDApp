# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\connect_window.ui'
#
# Created: Sat Aug  8 10:59:16 2015
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
        self.line_host_ip = QtGui.QLineEdit(connect_window)
        self.line_host_ip.setObjectName(_fromUtf8("line_host_ip"))
        self.gridLayout.addWidget(self.line_host_ip, 0, 1, 1, 1)
        self.line_port = QtGui.QLineEdit(connect_window)
        self.line_port.setObjectName(_fromUtf8("line_port"))
        self.gridLayout.addWidget(self.line_port, 1, 1, 1, 1)
        self.line_name = QtGui.QLineEdit(connect_window)
        self.line_name.setObjectName(_fromUtf8("line_name"))
        self.gridLayout.addWidget(self.line_name, 2, 1, 1, 1)
        self.button_connect = QtGui.QPushButton(connect_window)
        self.button_connect.setObjectName(_fromUtf8("button_connect"))
        self.gridLayout.addWidget(self.button_connect, 3, 1, 1, 1)
        self.button_cancel = QtGui.QPushButton(connect_window)
        self.button_cancel.setObjectName(_fromUtf8("button_cancel"))
        self.gridLayout.addWidget(self.button_cancel, 3, 0, 1, 1)

        self.retranslateUi(connect_window)
        QtCore.QObject.connect(self.button_cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), connect_window.close)
        QtCore.QMetaObject.connectSlotsByName(connect_window)

    def retranslateUi(self, connect_window):
        connect_window.setWindowTitle(_translate("connect_window", "Connect to...", None))
        self.label_2.setText(_translate("connect_window", "Host IP :", None))
        self.label.setText(_translate("connect_window", "Port :", None))
        self.label_3.setText(_translate("connect_window", "Name :", None))
        self.button_connect.setText(_translate("connect_window", "Connect", None))
        self.button_cancel.setText(_translate("connect_window", "Cancel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    connect_window = QtGui.QDialog()
    ui = Ui_connect_window()
    ui.setupUi(connect_window)
    connect_window.show()
    sys.exit(app.exec_())

