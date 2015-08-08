from PyQt4 import QtCore, QtGui
import sys
from random import choice, randint

from lib import resources_rc
from lib.main_window_ui import Ui_MainWindow
from lib.host_window_ui import Ui_host_window
from lib.connect_window_ui import Ui_connect_window

from lib.functions import *

#log("",True)

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
        self.setupUi(MainWindow)
        self.ui_connect = Ui_connect_window()        
        MainWindow.resize(1280,720)
        
        self.dock_campain.hide()
        self.dock_client.hide()
        
        self.actionHost_Game.triggered.connect(self.launch_host_game)
        self.actionConnect_to.triggered.connect(self.launch_connect_window)

    def launch_host_game(self):
        '''
        This method will launch the host window as a dialog.
        '''       
        host_dialog = QtGui.QDialog()
        ui = Ui_host_window()
        ui.setupUi(host_dialog)
        host_dialog.exec_()

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

    def set_encounter_table(self): #should return a dict or whatevs to print with qt in the random encounters tab.
        list_of_encounters=[]
        for i in range(12):
            list_of_encounters.append(self.monster_dictionary["id"])

    
        
app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()
ui = main_window(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
