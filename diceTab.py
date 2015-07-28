# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 10:04:46 2015

@author: Simon
"""
import random as rd
import socket as sk
from tkinter import *
from tkinter.ttk import *


class DiceTab(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        #Sides of Dice
        labelSides=Label(self,text="Sides")
        labelSides.grid(row=0,column=0)
        self.sides=StringVar()
        self.sides.set(20)
        spinboxSides=Spinbox(self,from_=1,to=20,increment=1,width=4)
        spinboxSides.config(textvariable=self.sides, font="sans 24", justify="center")
        spinboxSides.grid(row=0,column=1)
        #Number of Dices
        labelNumber=Label(self,text="Number")
        labelNumber.grid(row=1,column=0)
        self.number=StringVar()
        self.number.set(1)
        spinboxNumber=Spinbox(self,from_=1,to=30,increment=1,width=4)
        spinboxNumber.config(textvariable=self.number, font="sans 24", justify="center")
        spinboxNumber.grid(row=1,column=1)
        #Modifier
        labelModifier=Label(self,text="Modifier")
        labelModifier.grid(row=2,column=0)
        self.modifier=StringVar()
        self.modifier.set(0)
        spinboxModifier=Spinbox(self,from_=-5,to=5,increment=1,width=4)
        spinboxModifier.config(textvariable=self.modifier, font="sans 24", justify="center")
        spinboxModifier.grid(row=2,column=1)
        #Hide Checkbox
        labelHide=Label(self, text="Hide")
        labelHide.grid(row=2, column=2)
        self.hide=IntVar()
        self.hide.set(0)
        checkbuttonHide=Checkbutton(self,variable=self.hide)
        checkbuttonHide.grid(row=2,column=3)
        #Result display
        self.result=StringVar()
        self.result.set("")
        labelResult1=Label(self,text="Result")
        labelResult1.grid(row=1, column=4)
        labelResult2=Label(self,text=self.result.get(),relief=SUNKEN,width=4)
        labelResult2.grid(row=1,column=5)
        print(self.result.get())
        #Button to roll
        buttonRoll=Button(self,text="Roll!", command=self.roll)
        buttonRoll.grid(row=2,column=5)
        
    def roll(self):
        self.throws=[]
        numberOfDices=int(self.number.get())
        sidesOfDice=int(self.sides.get())
        modifierOfDice=int(self.modifier.get())
        
        for i in range(numberOfDices):
            self.throws.append(rd.randint(1,sidesOfDice))
        self.result.set(str(sum(self.throws)+modifierOfDice))
        labelResult2=Label(self,text=self.result.get(),relief=SUNKEN, width=4)
        labelResult2.grid(row=1,column=5)
        print(self.result.get())
        
        if self.hide.get(): # The variable 'self.hide' = 1 if case is ticked, 0 if not.
            print("Hide")
        else:
            print("Seen")
