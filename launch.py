# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:27:47 2015

@author: Dogeek
@contributors: Sinderella, solumos

Version : 0.0.1
"""

#CONVENTION : module_name, package_name, ClassName, method_name,
#ExceptionName, function_name, GLOBAL_CONSTANT_NAME, global_var_name,
#instance_var_name, function_parameter_name, local_var_name

import socket as sk
from tkinter import Tk, Frame, BOTH, Menu, StringVar, Toplevel, Label, Entry, Button
from tkinter.ttk import Notebook
import tkinter.messagebox as messagebox

from tabs.character import CharacterSheetTab
from tabs.dice import DiceTab
from tabs.encounters import EncountersTab
from tabs.map import MapTab
from tabs.treasure import TreasureTab
from tabs.disease import DiseaseTab
from functions import log, translate

log('', True)

class MainFrame(Frame):
    """MainFrame class to hold every widget used by the app. Inherits from tkinter.Frame"""
    def __init__(self, master=None):
        """Init method for the MainFrame class that contains every widget used"""
        Frame.__init__(self, master)
        #Defining Attributes :
        self.host_ip = str()
        self.host_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        self.port = StringVar()       
        self.max_connections = StringVar()
        self.users = dict()
        self.language = "EN-us"
        self.window = master
        
        self.pack(fill=BOTH)
        self.init_tabs()
        self.init_menu_bar()
        self.load_options()
        self.translation = translate()  


    def init_tabs(self):
        """Creating Tabs : Dice, Map, Encounters, Treasure"""
        tab_bar = Notebook(self)
        tab_bar.pack(fill=BOTH, padx=2, pady=3)
        #Dice
        self.tab_dice = DiceTab(tab_bar)
        tab_bar.add(self.tab_dice, text="Dice")
        #Map
        self.tab_map = MapTab(tab_bar)
        tab_bar.add(self.tab_map, text="Map")
        #Encounters
        self.tab_encounters = EncountersTab(tab_bar)
        tab_bar.add(self.tab_encounters, text="Encounters")
        #Treasure
        self.tab_treasure = TreasureTab(tab_bar)
        tab_bar.add(self.tab_treasure, text="Treasure")
        #Character Sheet
        self.tab_character_sheet = CharacterSheetTab(tab_bar)
        tab_bar.add(self.tab_character_sheet, text="Character Sheet")
        #Disease Generator
        self.tab_disease = DiseaseTab(tab_bar)
        tab_bar.add(self.tab_disease, text="Disease")

    def init_menu_bar(self):
        """Creating MenuBar : File, Connect, Help"""
        menu_bar = Menu(self)

        menu_file = Menu(menu_bar, tearoff=0)
        menu_file.add_command(label="Quit", command=self._quit)
        menu_bar.add_cascade(label="File", menu=menu_file)

        menu_connect = Menu(menu_bar, tearoff=0)
        menu_connect.add_command(label="Host", command=self.host)
        menu_connect.add_command(label="Connect", command=self.connect)
        menu_bar.add_cascade(label="Connect", menu=menu_connect)

        menu_character_sheet = Menu(menu_bar, tearoff=0)
        menu_character_sheet.add_command(label="Save As...", command=self.tab_character_sheet.save)
        menu_character_sheet.add_command(label="Load", command=self.tab_character_sheet.load)
        menu_character_sheet.add_command(label="Reset", command=self.tab_character_sheet.reset)
        menu_character_sheet.add_command(label="Roll Characteristics", \
                                        command=self.tab_character_sheet.rollCharacteristics)
        menu_character_sheet.add_checkbutton(label="Freeze Characteristics", \
                                        variable=self.tab_character_sheet.freeze)
        menu_bar.add_cascade(label="Character Sheet", menu=menu_character_sheet)        
        
        menu_help = Menu(menu_bar, tearoff=0)
        menu_help.add_command(label="About", command=self.about)
        menu_bar.add_cascade(label="Help", menu=menu_help)

        self.window.config(menu=menu_bar)

    def host(self):
        """Creates a host window to input the vraible needed"""
        self.port.set("25665")
        self.max_connections.set("5")
        
        host_window = Toplevel()
        host_window.title("Host Config")
        host_window.geometry("256x144")
        host_frame = Frame(host_window)
        host_frame.pack(fill=BOTH)

        Label(host_frame, text="Port :").grid(row=0, column=0)
        Label(host_frame, text="Maximum users").grid(row=1, column=0)
        
        Entry(host_frame, textvariable=self.port, width=30).grid(row=0, column=1)
        Entry(host_frame, textvariable=self.max_connections, width=30)\
        .grid(row=1, column=1)
        
        Button(host_frame, text="Host", command=self.host_connection)\
        .grid(row=2, column=1, columnspan=2)

    def host_connection(self):
        """Procedure for the server side of the app"""
        listen_port = int(self.port.get())
        max_users = int(self.max_connections.get())
        host = ''
        
        self.host_socket.bind((host, listen_port))
        
        self.host_ip = self.host_socket.getsockname()
        messagebox.showinfo(title="IP Address", message=str(self.host_ip))
        self.host_socket.listen(max_users)
        
        for i in range(max_users):
            self.users["Player{}".format(i)] = self.host_socket.accept()

    def connect(self):
        """Displays a connect window to connect to the server"""
        connect_window = Toplevel()
        connect_window.title("Connect to host")
        connect_window.geometry("256x144")

    def about(self):
        """Displays information about the app"""
        messagebox.showinfo("About", """DnDApp by Dogeek\nFor
            http://www.reddit.com/r/DnD\n(C)/u/Dogeek\nLicense :
            Creative Commons\n--------------\nCredit To:\n\
            Sinderella\nsolumos""")


    def _quit(self):
        """Quit procedure. Unloads everything and quit"""
        self.destroy()
        self.master.destroy()

    def load_options(self):
        """Method to load every option from the option.cfg file"""
        with open("options.cfg", "r") as options:
            for line in options:
                if "lng:" in line:                
                    self.language = line.split("lng:")[1]

if __name__ == '__main__':
    k = 0
    ROOT = Tk()
    ROOT.geometry("853x480")
    ROOT.title("D&D App")
    FRAME = MainFrame(ROOT)
    FRAME.mainloop()
