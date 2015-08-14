# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\host_window.ui'
#
# Created: Fri Aug 14 16:58:28 2015
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

class Ui_host_window(object):
    def setupUi(self, host_window):
        host_window.setObjectName(_fromUtf8("host_window"))
        host_window.resize(400, 300)
        host_window.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.gridLayout = QtGui.QGridLayout(host_window)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.button_host = QtGui.QPushButton(host_window)
        self.button_host.setObjectName(_fromUtf8("button_host"))
        self.gridLayout.addWidget(self.button_host, 3, 1, 1, 1)
        self.layout_host_window = QtGui.QGridLayout()
        self.layout_host_window.setObjectName(_fromUtf8("layout_host_window"))
        self.lineedit_maximumplayers = QtGui.QLineEdit(host_window)
        self.lineedit_maximumplayers.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineedit_maximumplayers.setObjectName(_fromUtf8("lineedit_maximumplayers"))
        self.layout_host_window.addWidget(self.lineedit_maximumplayers, 3, 1, 1, 1)
        self.label_2 = QtGui.QLabel(host_window)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.layout_host_window.addWidget(self.label_2, 3, 0, 1, 1)
        self.lineedit_port = QtGui.QLineEdit(host_window)
        self.lineedit_port.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineedit_port.setMaxLength(5)
        self.lineedit_port.setObjectName(_fromUtf8("lineedit_port"))
        self.layout_host_window.addWidget(self.lineedit_port, 1, 1, 1, 1)
        self.label = QtGui.QLabel(host_window)
        self.label.setObjectName(_fromUtf8("label"))
        self.layout_host_window.addWidget(self.label, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.layout_host_window.addItem(spacerItem, 4, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.layout_host_window.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.layout_host_window.addItem(spacerItem2, 6, 1, 1, 1)
        self.display_host_ip = QtGui.QLabel(host_window)
        self.display_host_ip.setFrameShape(QtGui.QFrame.WinPanel)
        self.display_host_ip.setFrameShadow(QtGui.QFrame.Sunken)
        self.display_host_ip.setAlignment(QtCore.Qt.AlignCenter)
        self.display_host_ip.setObjectName(_fromUtf8("display_host_ip"))
        self.layout_host_window.addWidget(self.display_host_ip, 5, 1, 1, 1)
        self.label_3 = QtGui.QLabel(host_window)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.layout_host_window.addWidget(self.label_3, 5, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.layout_host_window.addItem(spacerItem3, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.layout_host_window, 1, 1, 1, 1)

        self.retranslateUi(host_window)
        QtCore.QMetaObject.connectSlotsByName(host_window)

    def retranslateUi(self, host_window):
        host_window.setWindowTitle(_translate("host_window", "Host a Game", None))
        self.button_host.setText(_translate("host_window", "Host", None))
        self.lineedit_maximumplayers.setText(_translate("host_window", "5", None))
        self.label_2.setText(_translate("host_window", "Maximum players :", None))
        self.lineedit_port.setText(_translate("host_window", "25565", None))
        self.label.setText(_translate("host_window", "Port :", None))
        self.display_host_ip.setWhatsThis(_translate("host_window", "Your IP to give to your friends that want to connect to your game.", None))
        self.display_host_ip.setText(_translate("host_window", "xxx.xxx.xxx.xxx", None))
        self.label_3.setText(_translate("host_window", "Your IP :", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    host_window = QtGui.QDialog()
    ui = Ui_host_window()
    ui.setupUi(host_window)
    host_window.show()
    sys.exit(app.exec_())

