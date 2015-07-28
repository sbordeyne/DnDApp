# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 10:07:19 2015

@author: Simon
"""
from tkinter import Frame, Button


class DiseaseTab(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        buttonDisease=Button(self,text="Disease", command=self.disease)
        buttonDisease.grid(row=0,column=0)

    def disease(self):
        print("disease")
