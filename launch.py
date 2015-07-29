# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:27:47 2015

@author: Dogeek
@contributors: Sinderella, solumos

Version : 0.0.1
"""
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
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack(fill=BOTH)
        self.window = master
        self.init_tabs()
        self.init_menu_bar()
        self.translation=translate()

    def init_tabs(self):
        """Creating Tabs : Dice, Map, Encounters, Treasure"""
        tabBar = Notebook(self)
        tabBar.pack(fill=BOTH, padx=2, pady=3)
        #Dice
        self.tabDice = DiceTab(tabBar)
        tabBar.add(self.tabDice, text="Dice")
        #Map
        self.tabMap = MapTab(tabBar)
        tabBar.add(self.tabMap, text="Map")
        #Encounters
        self.tabEncounters = EncountersTab(tabBar)
        tabBar.add(self.tabEncounters, text="Encounters")
        #Treasure
        self.tabTreasure = TreasureTab(tabBar)
        tabBar.add(self.tabTreasure, text="Treasure")
        #Character Sheet
        self.tabCharacterSheet = CharacterSheetTab(tabBar)
        tabBar.add(self.tabCharacterSheet, text="Character Sheet")
        #Disease Generator
        self.tabDisease = DiseaseTab(tabBar)
        tabBar.add(self.tabDisease, text="Disease")

    def init_menu_bar(self):
        """Creating MenuBar : File, Connect, Help"""
        menuBar = Menu(self)

        menuFile = Menu(menuBar, tearoff=0)
        menuFile.add_command(label="Quit", command=self._quit)
        menuBar.add_cascade(label="File", menu=menuFile)

        menuConnect = Menu(menuBar, tearoff=0)
        menuConnect.add_command(label="Host", command=self.host)
        menuConnect.add_command(label="Connect", command=self.connect)
        menuBar.add_cascade(label="Connect", menu=menuConnect)

        menuCharacterSheet = Menu(menuBar, tearoff=0)
        menuCharacterSheet.add_command(label="Save As...", command=self.tabCharacterSheet.save)
        menuCharacterSheet.add_command(label="Load", command=self.tabCharacterSheet.load)
        menuCharacterSheet.add_command(label="Reset", command=self.tabCharacterSheet.reset)
        menuCharacterSheet.add_command(label="Roll Characteristics", command=self.tabCharacterSheet.rollCharacteristics)
        menuCharacterSheet.add_checkbutton(label="Freeze Characteristics", variable=self.tabCharacterSheet.freeze)
        menuBar.add_cascade(label="Character Sheet", menu=menuCharacterSheet)        
        
        menuHelp = Menu(menuBar, tearoff=0)
        menuHelp.add_command(label="About", command=self.about)
        menuBar.add_cascade(label="Help", menu=menuHelp)

        self.window.config(menu=menuBar)

    def host(self):
        """Procedure which host the server version of the app"""
        self.port = StringVar()
        self.port.set("25665")
        
        self.maxConnections = StringVar()
        self.maxConnections.set("5")
        
        hostWindow = Toplevel()
        hostWindow.title("Host Config")
        hostWindow.geometry("256x144")
        hostFrame = Frame(hostWindow)
        hostFrame.pack(fill=BOTH)

        Label(hostFrame, text="Port :").grid(row=0, column=0)
        Label(hostFrame, text="Maximum users").grid(row=1,column=0)
        
        Entry(hostFrame, textvariable=self.port, width=30).grid(row=0, column=1)
        Entry(hostFrame, textvariable=self.maxConnections, width=30).grid(row=1,column=1)
        
        Button(hostFrame, text="Host", command=self.hostConnection).grid(row=2, column=1, columnspan=2)

    def hostConnection(self):
        listenPort = int(self.port.get())
        maxUsers=int(self.maxConnections.get())
        host = ''
        self.users=dict()
        self.hostConnection = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        self.hostConnection.bind((host, listenPort))
        
        self.IP = self.hostConnection.getsockname()
        messagebox.showinfo(title="IP Address", message=str(self.IP))
        self.hostConnection.listen(maxUsers)
        
        for i in range(maxUsers):
            self.users["Player{}".format(i)]=self.hostConnection.accept()
        pass

    def connect(self):
        connectWindow = Toplevel()
        connectWindow.title("Connect to host")
        connectWindow.geometry("256x144")

    def about(self):
        messagebox.showinfo("About", """DnDApp by Dogeek\nFor
            http://www.reddit.com/r/DnD\n(C)/u/Dogeek\nLicense :
            Creative Commons\n--------------\nCredit To:\n\
            Sinderella\nsolumos""")

    def _quit(self):
        """Quit procedure. unloads everything and quit"""
        self.destroy()
        self.master.destroy()

if __name__ == '__main__':
    k = 0
    root = Tk()
    root.geometry("853x480")
    root.title("D&D App")
    frame = MainFrame(root)
    frame.mainloop()
