# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 10:07:19 2015

@author: Simon
"""
from tkinter import Frame, Button


class TreasureTab(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        buttonTreasure=Button(self,text="Treasure", command=self.treasure)
        buttonTreasure.grid(row=0,column=0)
        
        
    def treasure(self):
        print("treasure")
