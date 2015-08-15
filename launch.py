from PyQt4 import QtCore, QtGui
import sys
from time import strftime

from lib import resources_rc
from lib.main_window_ui import Ui_MainWindow
from lib.host_window_ui import Ui_host_window
from lib.connect_window_ui import Ui_connect_window

from lib.functions import *

log_out = open("stdout.log", "a")
log_out.write("\n--------------\n{0}\n--------------\n".format(strftime("%A %d %B %Y %H:%M:%S")))
sys.stderr = log_out
print = log

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

class main_window(Ui_MainWindow):
    '''
    This class inherits the Ui_Mainwindow class. The inheritance is 
    used to add bindings to launch the host/connect window dialog
    '''
    def __init__(self, MainWindow):
        self.main_window = MainWindow
        self.setupUi(self.main_window)
        self.ui_connect = Ui_connect_window()
        self.main_window.resize(1280,720)
        
        self.dock_campain.hide()
        self.dock_client.hide()
        
        self.actionHost_Game.triggered.connect(self.launch_host_game)
        self.actionConnect_to.triggered.connect(self.launch_connect_window)
        self.actionNew_Campain.triggered.connect(self.new_camapain)
        self.button_rollatable.clicked.connect(self.set_encounter_table)
        self.line_treasure_value.editingFinished.connect(self.set_treasure)
        self.button_generate_npc.clicked.connect(self.set_npc)
        self.button_clear_text.clicked.connect(self.clear_generated_npc)

        self.list_of_encounters = ["_"]*12
        self.treasure_value = self.line_treasure_value.text()

    def launch_host_game(self):
        '''
        This method will launch the host window as a dialog.
        '''       
        host_dialog = QtGui.QDialog()
        ui = Ui_host_window()
        ui.setupUi(host_dialog)
        host_dialog.exec_()

    def new_campain(self):
        self.dock_campain.hide()        
        
        self.display_disease.clear()
        self.display_generated_npc.clear()
        self.display_gems.clear()
        self.display_jewels.clear()
        self.display_magicitems.clear()
        self.display_plant.clear()
        self.display_poison.clear()
        
        self.lineedit_numberofcoins_copper.clear()
        self.lineedit_numberofcoins_silver.clear()
        self.lineedit_numberofcoins_electrum.clear()
        self.lineedit_numberofcoins_gold.clear()
        self.lineedit_numberofcoins_platinum.clear()
        
        self.label_nameofrolledmonster_1.setText("_")
        self.label_nameofrolledmonster_2.setText("_")
        self.label_nameofrolledmonster_3.setText("_")
        self.label_nameofrolledmonster_4.setText("_")
        self.label_nameofrolledmonster_5.setText("_")
        self.label_nameofrolledmonster_6.setText("_")
        self.label_nameofrolledmonster_7.setText("_")
        self.label_nameofrolledmonster_8.setText("_")
        self.label_nameofrolledmonster_9.setText("_")
        self.label_nameofrolledmonster_10.setText("_")
        self.label_nameofrolledmonster_11.setText("_")
        self.label_nameofrolledmonster_12.setText("_")
        
        self.dock_campain.show()

    def launch_connect_window(self):
        '''
        This method will launch the connect window dialog
        '''
        connect_dialog = QtGui.QDialog()
        self.ui_connect.setupUi(connect_dialog)
        self.ui_connect.button_connect.clicked.connect(self.launch_dock_client)
        connect_dialog.exec_()
        if self.ui_connect.button_connect.isDown():
            connect_dialog.close()

    def launch_dock_client(self):
        self.dock_client.show()
        host_ip = self.ui_connect.line_host_ip.text()
        port = self.ui_connect.line_port.text()
        name = self.ui_connect.line_name.text()

    def set_encounter_table(self):
        environment = str(self.combo_environmentofencounter.currentText())
        list_of_encounters = get_random_encounters_table(get_monster_dict(),environment)
        self.label_nameofrolledmonster_1.setText(list_of_encounters[0])
        self.label_nameofrolledmonster_2.setText(list_of_encounters[1])
        self.label_nameofrolledmonster_3.setText(list_of_encounters[2])
        self.label_nameofrolledmonster_4.setText(list_of_encounters[3])
        self.label_nameofrolledmonster_5.setText(list_of_encounters[4])
        self.label_nameofrolledmonster_6.setText(list_of_encounters[5])
        self.label_nameofrolledmonster_7.setText(list_of_encounters[6])
        self.label_nameofrolledmonster_8.setText(list_of_encounters[7])
        self.label_nameofrolledmonster_9.setText(list_of_encounters[8])
        self.label_nameofrolledmonster_10.setText(list_of_encounters[9])
        self.label_nameofrolledmonster_11.setText(list_of_encounters[10])
        self.label_nameofrolledmonster_12.setText(list_of_encounters[11])

    def set_monster_stats(self):
        chance_of_encounter = self.slider_chanceofencounter.value()
        chosen_monster = get_a_monster(self.list_of_encounters, chance_of_encounter)
        life, ac, movement, attacks, damages, number_met, save_poison, save_wands,\
        save_paralysis, save_dragon, save_spells, moral, treasure, alignment,\
        xp_value = get_a_monster_stats(get_monster_dict(), chosen_monster)
        
        self.group_statsofrolledmonster.setTitle("Stats of Rolled Monster : {0}".format(chosen_monster))
        #self.label_statsofrolledmonster_ac

    def set_treasure(self):
        #Variables used
        self.treasure_value = self.line_treasure_value.text()
        has_gems = self.check_gems.isChecked()
        has_jewels = self.check_jewels.isChecked()
        has_magic = self.check_magic_items.isChecked()
        gem_string = ""
        jewel_string = ""
        magic_string = ""
        #try to convert to an int, if it is a string, returns 0 and doesn't generate a treasure
        try:
            treasure_value = int(self.treasure_value)
        except ValueError:
            self.line_treasure_value.setText("")
            treasure_value = 0
            pass
        #generate treasure, returns a dict where keys are "pieces", "jewels", "gems", "magic_items"
        treasure = get_treasure(treasure_value, has_magic, has_gems, has_jewels)
        #formatting gems, magic items and jewels asserting we have all keys in the dict
        try:        
            for gem_tuple in treasure["gems"]:
                gem_string += "{0} : {1}\n".format(gem_tuple[0], gem_tuple[1])
            for jewel_tuple in treasure["jewels"]:
                jewel_string += "{0} : {1}\n".format(jewel_tuple[0], jewel_tuple[1])
            for magic_item in treasure["magic_items"]:
                magic_string += magic_item + "\n"
        except KeyError:
            if not has_gems:
                gem_string = ""
            if not has_jewels:
                jewel_string = ""
            if not has_magic:
                magic_string = ""

        #sets the text in the lineedits and plaintextviewers
        self.display_gems.setPlainText(gem_string)
        self.display_jewels.setPlainText(jewel_string)
        self.display_magicitems.setPlainText(magic_string)
        self.lineedit_numberofcoins_platinum.setText(str(treasure["pieces"][0]))
        self.lineedit_numberofcoins_gold.setText(str(treasure["pieces"][1]))
        self.lineedit_numberofcoins_electrum.setText(str(treasure["pieces"][2]))
        self.lineedit_numberofcoins_silver.setText(str(treasure["pieces"][3]))
        self.lineedit_numberofcoins_copper.setText(str(treasure["pieces"][4]))
        pass

    def set_npc(self):
        print("set_npc")
        alignment = str(self.combobox_alignmentofnpc.currentText())
        print(alignment)
        gender = str(self.combobox_genderofnpc.currentText())
        print(gender)
        race = str(self.combobox_raceofnpc.currentText())
        print(race)
        class_ = str(self.combobox_classofnpc.currentText())
        print(class_)
        stats = str(self.combobox_statsofnpc.currentText())
        print(stats)
        level = int(self.slider_levelofnpc.value())
        print(level)
        generated_npc = generate_npc(alignment, gender, race, class_, level, stats)
        print(generated_npc)
        self.display_generated_npc.append(generated_npc + "\n")
        pass

    def clear_generated_npc(self):
        self.display_generated_npc.clear()
        pass

app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()
ui = main_window(MainWindow)
MainWindow.show()
sys.exit(app.exec_())