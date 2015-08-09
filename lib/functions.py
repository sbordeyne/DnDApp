# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 10:21:25 2015

@author: Simon
"""
from time import strftime
import sys
import random as rd

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
    monster_name{
    environment_name\n
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
    monster_dict={}
    name=""
    value={}        

    stats=["environment","life", "ac", "movement", "attacks", "damages", "number_met", "saves", "moral", "treasure", "alignment", "xp_value"]
    for stat in stats:
        value[stat] = ""
    i = 0

    with open("/resources/cfg/monster.cfg", "r") as monster_config:
        for line in monster_config:
            if "{" in line:
                name = line.strip("{")
            elif "}" in line:
                monster_dict[name]=value
                i = 0
                for stat in stats:
                    value[stat] = ""
                name = ""
            else:
                line.strip("\n")
                value[stats[i]] = line
                i += 1     
    return monster_dict

def get_random_encounters_table(monster_dict, environment):
    list_encounters=[""]*12
    monsters_that_can_be_picked=[]
    for name, stats in monster_dict.items():
        if stats["environment"] == environment:
            monsters_that_can_be_picked.append(name)
    for i in range(12):
        list_encounters[i] = rd.choice(monsters_that_can_be_picked)
    return list_encounters

def get_a_monster(list_encounters, chance_encounter):
    dice = rd.randint(1,12)
    chance = rd.randint(1,100)
    if chance <= chance_encounter:
        return list_encounters[dice]
    else:
        return "No Monster Met"

def get_a_monster_stats(monster_dict, name):
    #stats=["environment","life", "ac", "movement", "attacks", "damages",\
    #"number_met", "saves", "moral", "treasure", "alignment", "xp_value"]
    try:
        assert name != "No Monster Met", "no monster met, no stat to retrieve"
    except AssertionError:
        return ("_")*15
    stats_of_monster = monster_dict[name]
    
    #Getting the life points of monster : life => 3d6+-1 => (3 x 6-sided dices) minus 1
    life = stats_of_monster["life"]
    number_of_dices = int(life.split("d")[0])
    sides_of_dice = int(life.split("d")[1].split("+")[0])
    modifier_of_dice = int(life.split("d")[1].split("+")[1])
    temp=[]
    for i in range(number_of_dices):
        temp.append(rd.randint(1,sides_of_dice))
    life=sum(temp)+modifier_of_dice
    
    #Getting the Armor Class (AC)
    ac = stats_of_monster["ac"]
    
    #Getting the movement value
    movement=stats_of_monster["movement"]
    
    return ("_")*15