# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 10:01:52 2015

@author: Simon
"""
import random as rd
import socket as sk
from tkinter import Frame, StringVar, IntVar, SUNKEN
from tkinter.ttk import Entry, Button, Checkbutton, Label, OptionMenu
import tkinter.filedialog as filedialog

from functions import method_once


class CharacterSheetTab(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.player = StringVar()
        self.character = StringVar()
        self.dm = StringVar()
        self.str = StringVar()
        self.int = StringVar()
        self.wis = StringVar()
        self.dex = StringVar()
        self.con = StringVar()
        self.cha = StringVar()
        self.JPpoison = StringVar()
        self.JPwands = StringVar()
        self.JPparalysis = StringVar()
        self.JPbreath = StringVar()
        self.JPspell = StringVar()
        self.class_ = StringVar()
        self.race = StringVar()
        self.align = StringVar()
        self.AC = StringVar()
        self.HP = StringVar()
        self.maxHP = StringVar()
        self.XP_to_add = StringVar()
        self.XPbonus = StringVar()
        self.XPtotal = IntVar()
        self.level = StringVar()

        self.init_once()

        (
            self.baseXP,
            self.mainCarRace,
            self.mainCarClass) = self.classDifferenciation()
        self.remainingXP = StringVar()
        self.remainingXP.set(self.getRemainingXP())
        self.bonusXP = StringVar()
        self.bonusXP.set(self.getBonusXP())

        self.freeze = IntVar()
        self.freeze.set(1)

        Label(self, text="Player Name:").grid(row=0, column=0, columnspan=2)
        Label(self, text="Character Name :").grid(
            row=0, column=4, columnspan=2)
        Label(self, text="DM Name:").grid(row=0, column=8, columnspan=2)
        Label(self, text="STR:").grid(row=1, column=0)
        Label(self, text="INT:").grid(row=2, column=0)
        Label(self, text="WIS:").grid(row=3, column=0)
        Label(self, text="DEX:").grid(row=4, column=0)
        Label(self, text="CON:").grid(row=5, column=0)
        Label(self, text="CHA:").grid(row=6, column=0)
        Label(self, text="Poison/Deathray:").grid(row=1, column=2)
        Label(self, text="Wands:").grid(row=2, column=2)
        Label(self, text="Paralysis:").grid(row=3, column=2)
        Label(self, text="Dragon Breath:").grid(row=4, column=2)
        Label(self, text="Spells:").grid(row=5, column=2)
        Label(self, text="Armor Class").grid(row=1, column=4, columnspan=1)
        Label(self, text="Health Points").grid(row=1, column=5, columnspan=3)
        Label(self, text="  /  ").grid(row=2, column=6)
        Label(self, text="Class :").grid(row=3, column=4)
        Label(self, text="Race :").grid(row=4, column=4)
        Label(self, text="XP to add :").grid(row=7, column=0)
        Label(self, text="Remaining :").grid(row=8, column=0)
        Label(self, text="Bonus :").grid(row=7, column=2)
        Label(self, text="Alignment :").grid(row=3, column=6)
        Label(self, text="Level :").grid(row=9, column=0, columnspan=2)
        self.remainingLabel = Label(
            self,
            textvariable=self.remainingXP,
            relief=SUNKEN,
            width=5)
        self.remainingLabel.grid(row=8, column=1)
        self.bonusLabel = Label(
            self,
            textvariable=self.bonusXP,
            relief=SUNKEN,
            width=5)
        self.bonusLabel.grid(row=7, column=3)
        self.levelLabel = Label(
            self,
            textvariable=self.level,
            relief=SUNKEN,
            width=5)
        self.levelLabel.grid(row=9, column=2, columnspan=2)

        Eplayer = Entry(self, textvariable=self.player)
        Eplayer.grid(row=0, column=2, columnspan=2)
        Eplayer.bind(sequence='<KeyRelease>', func=self.refresh)

        Echaracter = Entry(self, textvariable=self.character)
        Echaracter.grid(row=0, column=6, columnspan=2)
        Echaracter.bind(sequence='<KeyRelease>', func=self.refresh)

        EDM = Entry(self, textvariable=self.dm)
        EDM.grid(row=0, column=10, columnspan=2)
        EDM.bind(sequence='<KeyRelease>', func=self.refresh)

        Estr = Entry(self, textvariable=self.str)
        Estr.grid(row=1, column=1)
        Estr.bind(sequence='<KeyRelease>', func=self.refresh)

        Eint = Entry(self, textvariable=self.int)
        Eint.grid(row=2, column=1)
        Eint.bind(sequence='<KeyRelease>', func=self.refresh)

        Ewis = Entry(self, textvariable=self.wis)
        Ewis.grid(row=3, column=1)
        Ewis.bind(sequence='<KeyRelease>', func=self.refresh)

        Edex = Entry(self, textvariable=self.dex)
        Edex.grid(row=4, column=1)
        Edex.bind(sequence='<KeyRelease>', func=self.refresh)

        Econ = Entry(self, textvariable=self.con)
        Econ.grid(row=5, column=1)
        Econ.bind(sequence='<KeyRelease>', func=self.refresh)

        Echa = Entry(self, textvariable=self.cha)
        Echa.grid(row=6, column=1)
        Echa.bind(sequence='<KeyRelease>', func=self.refresh)

        Entry(self, textvariable=self.JPpoison).grid(row=1, column=3)
        Entry(self, textvariable=self.JPwands).grid(row=2, column=3)
        Entry(self, textvariable=self.JPparalysis).grid(row=3, column=3)
        Entry(self, textvariable=self.JPbreath).grid(row=4, column=3)
        Entry(self, textvariable=self.JPspell).grid(row=5, column=3)
        Entry(self, textvariable=self.AC).grid(row=2, column=4)
        Entry(self, textvariable=self.HP).grid(row=2, column=5)
        Entry(self, textvariable=self.maxHP).grid(row=2, column=7)

        EXP = Entry(self, textvariable=self.XP_to_add)
        EXP.grid(row=7, column=1)
        EXP.bind(sequence='<KeyPress-Return>', func=self.addXP)

        OptionMenu(
            self, self.class_,
            "Class",
            "Warrior",
            "Wizard",
            "Thief",
            "Cleric").grid(row=3, column=5)
        OptionMenu(
            self, self.align,
            "Alignment",
            "Lawful Good",
            "Lawful Neutral",
            "Lawful Evil",
            "Neutral Good",
            "Neutral Neutral",
            "Neutral Evil",
            "Chaotic Good",
            "Chaotic Neutral",
            "Chaotic Evil").grid(row=3, column=7)
        OptionMenu(
            self, self.race,
            "Race",
            "Human",
            "Elf",
            "Dwarf",
            "Halfelin").grid(row=4, column=5)

        Button(
            self,
            text="Add XP",
            command=self.refresh,
            width=6).grid(row=10, column=3)

    def refresh(self, event):
        (
            self.baseXP,
            self.mainCarRace,
            self.mainCarClass) = self.classDifferenciation()
        self.remainingXP.set(self.getRemainingXP())
        self.bonusXP.set(self.getBonusXP())
        self.update_idletasks()

    def addXP(self, event):
        (
            self.baseXP,
            self.mainCarRace,
            self.mainCarClass) = self.classDifferenciation()
        self.remainingXP.set(self.getRemainingXP())
        self.bonusXP.set(self.getBonusXP())
        self.addXPToTotal()
        self.update_idletasks()

    def save(self):
        file_ = filedialog.asksaveasfile(
            parent=self,
            mode="w",
            title="Save your Character Sheet",
            defaultextension=".dndcs",
            filetypes=[
                ("Character Sheets", ".dndcs"),
                ("All Files", ".*")])
        string = ""
        list_vars = [
            self.player, self.character, self.dm, self.str, self.int,
            self.wis, self.dex, self.con, self.cha, self.JPpoison,
            self.JPwands, self.JPparalysis, self.JPbreath, self.JPspell,
            self.class_, self.race, self.align, self.AC, self.HP,
            self.maxHP, self.XPtotal, self.level]
        for i in range(len(list_vars)):
            string += str(list_vars[i].get())+"\n"

        string = string[:-2]
        file_.write(string)
        file_.close()

    def load(self):
        self.reset()
        file_ = filedialog.askopenfile(
            parent=self, mode="r", title="Open a Character Sheet",
            defaultextension=".dndcs",
            filetypes=[
                ("Character Sheets", ".dndcs"),
                ("All Files", ".*")]
        )
        list_vars = [
            self.player, self.character, self.dm, self.str, self.int,
            self.wis, self.dex, self.con, self.cha, self.JPpoison,
            self.JPwands, self.JPparalysis, self.JPbreath, self.JPspell,
            self.class_, self.race, self.align, self.AC, self.HP,
            self.maxHP, self.XPtotal, self.level]
        i = 0
        for line in file_:
            line.strip()
            list_vars[i].set(line)
            i += 1
        file_.close()
        self.refresh(1)

    def reset(self):
        self.player.set("")
        self.character.set("")
        self.dm.set("")
        self.str.set("")
        self.int.set("")
        self.wis.set("")
        self.dex.set("")
        self.con.set("")
        self.cha.set("")
        self.JPpoison.set("")
        self.JPwands.set("")
        self.JPparalysis.set("")
        self.JPbreath.set("")
        self.JPspell.set("")
        self.class_.set("Class")
        self.race.set("Race")
        self.align.set("Alignment")
        self.AC.set("")
        self.HP.set("")
        self.maxHP.set("")
        self.XP_to_add.set("")
        self.XPbonus.set("")
        self.XPtotal.set(0)
        self.level.set("1")

    def classDifferenciation(self):
        XPToReturn = 0
        mainCarClass = 0
        mainCarRace = 0
        if self.class_.get() == "Warrior":
            XPToReturn += 2000
            mainCarClass = int(self.str.get())
        elif self.class_.get() == "Wizard":
            XPToReturn += 2500
            mainCarClass = int(self.int.get())
        elif self.class_.get() == "Cleric":
            XPToReturn += 1500
            mainCarClass = int(self.wis.get())
        elif self.class_.get() == "Thief":
            XPToReturn += 1200
            mainCarClass = int(self.dex.get())
        else:
            XPToReturn += 0
        if self.race.get() == "Human":
            XPToReturn += 0
            mainCarRace = int(self.cha.get())
        elif self.race.get() == "Elf":
            XPToReturn += 1500
            mainCarRace = int(self.str.get())
        elif self.race.get() == "Dwarf":
            XPToReturn += 500
            mainCarRace = int(self.con.get())
        elif self.race.get() == "Halfelin":
            XPToReturn += 800
            mainCarRace = int(self.dex.str.get())
        return XPToReturn, mainCarClass, mainCarRace

    def getRemainingXP(self):
        remainingXP = int(self.baseXP) * int(self.level.get()) - \
            int(self.XPtotal.get())
        return str(remainingXP)

    def getBonusXP(self):
        bonusPercentage = 0
        if 16 <= self.mainCarClass <= 18:
            bonusPercentage += 5
        elif 13 <= self.mainCarClass <= 15:
            bonusPercentage += 0
        elif 9 <= self.mainCarClass <= 12:
            bonusPercentage -= 5
        elif 3 <= self.mainCarClass <= 8:
            bonusPercentage -= 10
        else:
            bonusPercentage = 0

        if 16 <= self.mainCarRace <= 18:
            bonusPercentage += 5
        elif 13 <= self.mainCarRace <= 15:
            bonusPercentage += 0
        elif 9 <= self.mainCarRace <= 12:
            bonusPercentage -= 5
        elif 3 <= self.mainCarRace <= 8:
            bonusPercentage -= 10
        else:
            bonusPercentage = 0
        self.bonus = bonusPercentage
        return str(bonusPercentage) + "%"

    def addXPToTotal(self):
        (
            self.baseXP,
            self.mainCarRace,
            self.mainCarClass) = self.classDifferenciation()
        self.remainingXP.set(self.getRemainingXP())
        self.bonusXP.set(self.getBonusXP())
        remaining = int(self.getRemainingXP())
        bonus = int(self.getBonusXP().strip("%"))
        if self.XP_to_add.get() != '':
            XP_to_add = int(self.XP_to_add.get())
        else:
            XP_to_add = 0
        self.XP_to_add.set("")
        total = self.XPtotal.get()
        total += XP_to_add*(1+bonus/100)
        self.XPtotal.set(total)
        if total >= remaining:
            self.level.set(str(int(self.level.get())+1))

    def rollCharacteristics(self):
        if self.freeze.get() == 0:
            chars = [
                self.str, self.int, self.wis,
                self.dex, self.con, self.cha]
            for char in chars:
                char.set(str(
                    rd.randint(1, 6) + rd.randint(1, 6) + rd.randint(1, 6)))
        pass

    @method_once
    def init_once(self):
        self.level.set("1")
        self.baseXP = 0
        self.mainCarRace = 0
        self.mainCarClass = 0
        self.bonus = 0
        self.XP_to_add.set("0")
