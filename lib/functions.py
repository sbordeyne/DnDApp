# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 10:21:25 2015

@author: Simon
"""
from time import strftime
import sys


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

def log(message, first_time=False):
    """
    Rewrites stdout and stderr to corresponding log files
    
    Use instead of print() for debug
    """
    message = str(message)
    with open("stdout.log", "a") as log_out:
        if first_time:
            sys.stdout = log_out
            log_err = open("stderr.log","a")
            sys.stderr = log_err
            log_string = "\n--------------\n{0}\n--------------\n".format(strftime("%A %d %B %Y %H:%M:%S"))
            log_err.write(log_string)
            print(log_string)
        else:
            print("\n[{0}] {1}".format(strftime("%H:%M:%S"), message))

def get_monster_dict(environment_of_encounter):
        """
        Method to return a dict of all the available monsters. Reads the resource/cfg/monsters.cfg file to fill the dict.
        
        Formatted entry in monsters.cfg:
        monster_name;environment_name{
        life\n
        ac\n
        movement\n
        attacks\n
        damages\n
        number_met\n
        saves\n
        moral\n
        treasure\n
        alignment\n
        xp_value\n
        }
        """
        return_dict=dict()
        key={}
        key["name"] = ""
        key["environment"] = ""
        value={}        
        
        stats=["life", "ac", "movement", "attacks", "damages", "number_met", "saves", "moral", "treasure", "alignment", "xp_value"]
        for stat in stats:
            value[stat] = ""
        
        with open("/resources/cfg/monster.cfg", "r") as monster_config:
            for line in monster_config:
                pass
        return return_dict