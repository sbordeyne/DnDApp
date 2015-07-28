# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 10:08:54 2015

@author: Simon
"""

from tkinter import Frame, Button

class MapTab(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        buttonMap=Button(self,text="Map", command=self._map)
        buttonMap.grid(row=0,column=0)


    def _map(self):
        print("map")
