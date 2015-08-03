# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 10:07:19 2015

@author: Simon
"""
from tkinter import Frame, Button


class TreasureTab(Frame):
    '''
    Tab object for the Treasure tab.
    '''
    def __init__(self, master=None):
        Frame.__init__(self, master)
        button_treasure = Button(self, text="Treasure", command=self.treasure)
        button_treasure.grid(row=0, column=0)

    def treasure(self):
        '''
        Print 'treasure' to console when the treasure button is pressed.
        '''
        print("treasure")
