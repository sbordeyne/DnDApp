# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 10:08:56 2015

@author: Simon
"""

from tkinter import Frame, Label, StringVar


class EncountersTab(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.creatures_names_list = [''] * 12
        self.environment = StringVar()
        self.chance = StringVar()

        Label(self, text="Environment of the Encounter :").grid(
            row=0, column=0, columnspan=3)
        Label(self, text="Chance of the Encounter :").grid(
            row=1, column=0, columnspan=3)
        Label(self, text=" %").grid(row=1, column=4)
        Label(self, text="1 :").grid(row=2, column=0)
        Label(self, text="2 :").grid(row=3, column=0)
        Label(self, text="3 :").grid(row=4, column=0)
        Label(self, text="4 :").grid(row=5, column=0)
        Label(self, text="5 :").grid(row=6, column=0)
        Label(self, text="6 :").grid(row=7, column=0)
        Label(self, text="7 :").grid(row=2, column=4)
        Label(self, text="8 :").grid(row=3, column=4)
        Label(self, text="9 :").grid(row=4, column=4)
        Label(self, text="10 :").grid(row=5, column=4)
        Label(self, text="11 :").grid(row=6, column=4)
        Label(self, text="12 :").grid(row=7, column=4)
        Label(self, text="AC :").grid(row=3, column=7)
        Label(self, text="HP :").grid(row=4, column=7)
        Label(self, text="ATK :").grid(row=5, column=7)
        Label(self, text="DMG :").grid(row=6, column=7)
        Label(self, text="NUMBER :").grid(row=7, column=7)
        Label(self, text="SAVES:").grid(row=8, column=7)
        Label(self, text="ALIGN :").grid(row=9, column=7)
        Label(self, text="XP :").grid(row=10, column=7)

    def generate(self):
        print("generate")

    def encounter(self):
        print("encounter")

    def get_creatures_names(self):
        creatures = readConfig("creatures_names")
