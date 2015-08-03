# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 10:21:25 2015

@author: Simon
"""
from time import strftime

def read_config(file_name):
    """Function that reads the config of given filename, returns dict"""
    return_dict = dict()
    temp_list = list()
    i = 0
    with open("cfg/{}.cfg".format(file_name), "r") as file_:
        for line in file_:
            if line != "$":
                splitted = line.split(";")
                temp_list.append((splitted[0], splitted[1]))
            else:
                i += 1
                return_dict["{}".format(i)] = temp_list
                temp_list = []
    return return_dict

def method_once(method): #http://code.activestate.com/recipes/425445-once-decorator/
    """A decorator that runs a method only once."""
    attrname = "_%s_once_result" % id(method)
    def decorated(self, *args, **kwargs):
        """function decorated"""
        try:
            return getattr(self, attrname)
        except AttributeError:
            setattr(self, attrname, method(self, *args, **kwargs))
            return getattr(self, attrname)
    return decorated

def log(message, file_="log.txt", first_time=False):
    """
    Inits or writes log messages to log.txt(default)
    
    Use instead of print() for debug
    """
    message = str(message)
    with open(file_, "a") as log_file:
        if first_time:
            log_string = "\n--------------\n{0}\n--------------\n"
            log_file.write(log_string.format(strftime("%A %d %B %Y %H:%M:%S")))
        else:
            log_file.write("\n[{}] {}".format(strftime("%H:%M:%S"), message))

def translate(language="EN-us"):
    """
    Reads the translation file, defaults to EN-us.
    
    Returns a dictionary with the key corresponding to the english sentence
    """
    translation = dict()
    with open("lng/{}.lng".format(language), "r") as lng:
        for line in lng:
            line.strip("\n")
            if "//" in line:
                continue
            translation[line.split("§")[0]] = line.split("§")[1]              
    return translation
