# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 10:21:25 2015

@author: Simon
"""
from time import strftime, sleep

def readConfig(fileName):
    return_dict=dict()
    temp_list=list()
    i=0
    with open("cfg/{}.cfg".format(fileName),"r") as file_:
        for line in file_:
            if line != "$":
                splitted=line.split(";")
                temp_list.append((splitted[0],splitted[1]))
            else:
                i+=1
                return_dict["{}".format(i)]=temp_list
                temp_list=[]
    return return_dict
    
def method_once(method): #http://code.activestate.com/recipes/425445-once-decorator/
    "A decorator that runs a method only once."
    attrname = "_%s_once_result" % id(method)
    def decorated(self, *args, **kwargs):
        try:
            return getattr(self, attrname)
        except AttributeError:
            setattr(self, attrname, method(self, *args, **kwargs))
            return getattr(self, attrname)
    return decorated

def log(message,FirstTime=False):
    message=str(message)
    with open("log.txt","a") as log:
        if FirstTime:
            log.write("\n--------------\n{0}\n--------------\n".format(strftime("%A %d %B %Y %H:%M:%S")))
        else:
            log.write("\n[{}] {}".format(strftime("%H:%M:%S"),message))
