# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 10:31:08 2015

@author: Simon
"""

from PyQt4 import QtCore, QtGui
import sys
from random import choice, randint

from lib import main_window_ui, resources_rc

class MainWindow(main_window_ui.Ui_MainWindow()):
    def __init__(self,qt_main_window):
        self.setupUi(qt_main_window)
        self.monster_dictionary = self.get_monster_dict()
        self.environmentofencounter=""

    def get_encounter_table(self): #should return a dict or whatevs to print with qt in the random encounters tab.
        list_of_encounters=[]
        for i in range(12):
            list_of_encounters.append(self.monster_dictionary["id"])

    def get_monster_dict(self):
        return_dict=dict()
        key={}
        key["name"] = ""
        key["environment"] = ""
        value={}        
        
        stats=["life", "ac", "movement", "attacks", "damages", "number_met", "saves", "moral", "treasure", "alignment", "xp_value"]
        for stat in stats:
            value[stat] = ""
        
        with open("/resources/cfg/monster.cfg", "r") as monster_config:
            for line in monster_config:
                