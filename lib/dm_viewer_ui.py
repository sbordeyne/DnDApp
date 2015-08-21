# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\dm_viewer.ui'
#
# Created: Fri Aug 21 08:59:59 2015
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

class Ui_dm_play_interface(object):
    def setupUi(self, dm_play_interface):
        dm_play_interface.setObjectName(_fromUtf8("dm_play_interface"))
        dm_play_interface.resize(764, 549)
        self.horizontalLayout = QtGui.QHBoxLayout(dm_play_interface)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.dock_campain_viewer = QtGui.QDockWidget(dm_play_interface)
        self.dock_campain_viewer.setObjectName(_fromUtf8("dock_campain_viewer"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.treeWidget = QtGui.QTreeWidget(self.dockWidgetContents)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 1)
        self.dock_campain_viewer.setWidget(self.dockWidgetContents)
        self.horizontalLayout.addWidget(self.dock_campain_viewer)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.group_character_view = QtGui.QGroupBox(dm_play_interface)
        self.group_character_view.setObjectName(_fromUtf8("group_character_view"))
        self.gridLayout_2 = QtGui.QGridLayout(self.group_character_view)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.group_character_view)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(self.group_character_view)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.group_character_view)
        self.graphicsView = QtGui.QGraphicsView(dm_play_interface)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout.addWidget(self.graphicsView)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(dm_play_interface)
        QtCore.QMetaObject.connectSlotsByName(dm_play_interface)

    def retranslateUi(self, dm_play_interface):
        dm_play_interface.setWindowTitle(_translate("dm_play_interface", "Dungeon Master Viewer", None))
        self.dock_campain_viewer.setWindowTitle(_translate("dm_play_interface", "Campain Viewer", None))
        self.group_character_view.setTitle(_translate("dm_play_interface", "Character View", None))
        self.label.setText(_translate("dm_play_interface", "%s :", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dm_play_interface = QtGui.QDialog()
    ui = Ui_dm_play_interface()
    ui.setupUi(dm_play_interface)
    dm_play_interface.show()
    sys.exit(app.exec_())

