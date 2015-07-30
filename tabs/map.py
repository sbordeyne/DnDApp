# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 10:08:54 2015

@author: Simon
"""

from tkinter import Frame, Canvas, StringVar, Toplevel, BOTH
from tkinter.ttk import Button

class MapTab(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.tiles_type=StringVar()
    
    def toolbox_window(self):
        """Creates the window which will host the toolbox buttons"""
        toolbox_root = Toplevel()
        toolbox_root.title("Toolbox")
        toolbox_root.geometry("455x256")
        toolbox_frame = Frame(toolbox_root)
        toolbox_frame.pack(fill=BOTH)
        
        