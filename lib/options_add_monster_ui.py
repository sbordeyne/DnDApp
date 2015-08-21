# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\options_add_monster.ui'
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

class Ui_monsters_options(object):
    def setupUi(self, monsters_options):
        monsters_options.setObjectName(_fromUtf8("monsters_options"))
        monsters_options.resize(560, 560)
        self.gridLayout_2 = QtGui.QGridLayout(monsters_options)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.list_monsters = QtGui.QListWidget(monsters_options)
        self.list_monsters.setObjectName(_fromUtf8("list_monsters"))
        self.gridLayout_2.addWidget(self.list_monsters, 0, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.line_monster_environment = QtGui.QLineEdit(monsters_options)
        self.line_monster_environment.setObjectName(_fromUtf8("line_monster_environment"))
        self.gridLayout.addWidget(self.line_monster_environment, 1, 1, 1, 1)
        self.line_monster_alignment = QtGui.QLineEdit(monsters_options)
        self.line_monster_alignment.setObjectName(_fromUtf8("line_monster_alignment"))
        self.gridLayout.addWidget(self.line_monster_alignment, 11, 1, 1, 1)
        self.label = QtGui.QLabel(monsters_options)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(monsters_options)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(monsters_options)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_5 = QtGui.QLabel(monsters_options)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_6 = QtGui.QLabel(monsters_options)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_7 = QtGui.QLabel(monsters_options)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.label_8 = QtGui.QLabel(monsters_options)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)
        self.label_9 = QtGui.QLabel(monsters_options)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)
        self.label_10 = QtGui.QLabel(monsters_options)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 8, 0, 1, 1)
        self.label_11 = QtGui.QLabel(monsters_options)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 11, 0, 1, 1)
        self.label_12 = QtGui.QLabel(monsters_options)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 9, 0, 1, 1)
        self.label_13 = QtGui.QLabel(monsters_options)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout.addWidget(self.label_13, 10, 0, 1, 1)
        self.line_monster_name = QtGui.QLineEdit(monsters_options)
        self.line_monster_name.setObjectName(_fromUtf8("line_monster_name"))
        self.gridLayout.addWidget(self.line_monster_name, 0, 1, 1, 1)
        self.line_monster_life = QtGui.QLineEdit(monsters_options)
        self.line_monster_life.setObjectName(_fromUtf8("line_monster_life"))
        self.gridLayout.addWidget(self.line_monster_life, 2, 1, 1, 1)
        self.line_monster_ac = QtGui.QLineEdit(monsters_options)
        self.line_monster_ac.setObjectName(_fromUtf8("line_monster_ac"))
        self.gridLayout.addWidget(self.line_monster_ac, 3, 1, 1, 1)
        self.line_monster_movement = QtGui.QLineEdit(monsters_options)
        self.line_monster_movement.setObjectName(_fromUtf8("line_monster_movement"))
        self.gridLayout.addWidget(self.line_monster_movement, 4, 1, 1, 1)
        self.line_monster_attacks = QtGui.QLineEdit(monsters_options)
        self.line_monster_attacks.setObjectName(_fromUtf8("line_monster_attacks"))
        self.gridLayout.addWidget(self.line_monster_attacks, 5, 1, 1, 1)
        self.line_monster_damages = QtGui.QLineEdit(monsters_options)
        self.line_monster_damages.setObjectName(_fromUtf8("line_monster_damages"))
        self.gridLayout.addWidget(self.line_monster_damages, 6, 1, 1, 1)
        self.line_monster_numbermet = QtGui.QLineEdit(monsters_options)
        self.line_monster_numbermet.setObjectName(_fromUtf8("line_monster_numbermet"))
        self.gridLayout.addWidget(self.line_monster_numbermet, 7, 1, 1, 1)
        self.line_monster_saves = QtGui.QLineEdit(monsters_options)
        self.line_monster_saves.setObjectName(_fromUtf8("line_monster_saves"))
        self.gridLayout.addWidget(self.line_monster_saves, 8, 1, 1, 1)
        self.line_monster_treasure = QtGui.QLineEdit(monsters_options)
        self.line_monster_treasure.setObjectName(_fromUtf8("line_monster_treasure"))
        self.gridLayout.addWidget(self.line_monster_treasure, 10, 1, 1, 1)
        self.label_2 = QtGui.QLabel(monsters_options)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 12, 0, 1, 1)
        self.line_monster_xp = QtGui.QLineEdit(monsters_options)
        self.line_monster_xp.setObjectName(_fromUtf8("line_monster_xp"))
        self.gridLayout.addWidget(self.line_monster_xp, 12, 1, 1, 1)
        self.line_monster_moral = QtGui.QLineEdit(monsters_options)
        self.line_monster_moral.setObjectName(_fromUtf8("line_monster_moral"))
        self.gridLayout.addWidget(self.line_monster_moral, 9, 1, 1, 1)
        self.button_generate_monster = QtGui.QPushButton(monsters_options)
        self.button_generate_monster.setObjectName(_fromUtf8("button_generate_monster"))
        self.gridLayout.addWidget(self.button_generate_monster, 13, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.retranslateUi(monsters_options)
        QtCore.QMetaObject.connectSlotsByName(monsters_options)

    def retranslateUi(self, monsters_options):
        monsters_options.setWindowTitle(_translate("monsters_options", "Options - Add Monsters", None))
        self.label.setText(_translate("monsters_options", "Name :", None))
        self.label_3.setText(_translate("monsters_options", "Environment :", None))
        self.label_4.setText(_translate("monsters_options", "Life :", None))
        self.label_5.setText(_translate("monsters_options", "AC :", None))
        self.label_6.setText(_translate("monsters_options", "Movement :", None))
        self.label_7.setText(_translate("monsters_options", "Attacks :", None))
        self.label_8.setText(_translate("monsters_options", "Damages :", None))
        self.label_9.setText(_translate("monsters_options", "Number Met :", None))
        self.label_10.setText(_translate("monsters_options", "Saves :", None))
        self.label_11.setText(_translate("monsters_options", "Alignment :", None))
        self.label_12.setText(_translate("monsters_options", "Moral :", None))
        self.label_13.setText(_translate("monsters_options", "Treasure Value :", None))
        self.label_2.setText(_translate("monsters_options", "XP Value :", None))
        self.button_generate_monster.setText(_translate("monsters_options", "Generate a Random Monster", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    monsters_options = QtGui.QDialog()
    ui = Ui_monsters_options()
    ui.setupUi(monsters_options)
    monsters_options.show()
    sys.exit(app.exec_())

