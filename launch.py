# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:27:47 2015

@author: Dogeek (reddit.com/u/Dogeek) a.k.a Simon Bordeyne for reddit.com/r/DnD

Version : 0.13.0
"""
"""
--------------------
Bug Section :
--------------------

[ ] The host function blocks everything unless it catches something.
[ ] You can't catch everything simultaneously
[ ] The "hide" thing is a dummy for now
[ ] The network functioons are not up yet
[x] The level, xp, remaining xp features don't work for some reason
 | [ ] It now needs automatic refresh (clicking on the button is kind of a hassle)
[ ] Sections not built yet : Encounters, Treasures, Connection to host, Help page,
    load character sheet, display dices of others connected
---------------------
Things to improve :
---------------------

[ ] Simultaneous host/Clients connections
[ ] Add a Stop button, to stop hosting
[ ] Handle exceptions
[x] Go modular, this single file becomes too heavy to read and work on
[x] cx_freeze to distribute the program
[ ] improve dice interface
[ ] slightly improve character Sheet interface with some padding, and add
    a Text Widget to keep track of treasures and inventory, maybe
    add a button to roll caracteristics.

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
from functions import log

log('', True)

class MainFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack(fill=BOTH)
        self.window = master
        self.init_menu_bar()
        self.init_tabs()

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

        menuHelp = Menu(menuBar, tearoff=0)
        menuHelp.add_command(label="About", command=self.about)
        menuBar.add_cascade(label="Help", menu=menuHelp)

        self.window.config(menu=menuBar)

    def host(self):
        """Procedure which host the server version of the app"""
        self.port = StringVar()
        self.port.set("25665")

        hostWindow = Toplevel()
        hostWindow.title("Host Config")
        hostWindow.geometry("256x144")
        hostFrame = Frame(hostWindow)
        hostFrame.pack(fill=BOTH)

        Label(hostFrame, text="Port :").grid(row=0, column=0)

        entryPort = Entry(hostFrame, textvariable=self.port, width=30)
        entryPort.grid(row=0, column=1)

        buttonHost = Button(hostFrame, text="Host", command=self.hostConnection)
        buttonHost.grid(row=1, column=1)

    def hostConnection(self):
        listenPort = int(self.port.get())
        host = ''
        self.hostConnection = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        self.hostConnection.bind((host, listenPort))
        self.clientConnection, self.connectionInfos = self.hostConnection.accept()
        self.IP = self.hostConnection.getsockname()
        messagebox.showinfo(title="IP Adress", message=str(self.IP))
        self.hostConnection.listen(5)

    def connect(self):
        connectWindow = Toplevel()
        connectWindow.title("Connect to host")
        connectWindow.geometry("256x144")

    def about(self):
        messagebox.showinfo("About", """DnDApp by Dogeek\nFor
            http://www.reddit.com/r/DnD\n(C)/u/Dogeek\nLicense :
            Creative Commons\n--------------\nCredit To:\n\
            Ori Peleg on activestate.com for a decorator recipe""")

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
