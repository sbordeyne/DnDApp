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
    with open("../resources/cfg/{}.cfg".format(file_name), "r") as config_file:
        for line in config_file:
            if "{" in line:
                name = line.split("{")[0]
            elif "}" in line:
                return_dict[name] = temp_list
                temp_list = []
            else:
                if ";" in line:
                    to_append = (line.split(";")[0],int(line.split(";")[1]))
                else:
                    to_append = line.split("\n"[0])
                temp_list.append(to_append)
                del to_append
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
    try:
        log_out = open("stdout.log", "a")
    except FileNotFoundError:
        pass
    except IOError:
        pass
    finally:
        if first_time:
            sys.stderr = log_out
            sys.stdout = log_out
            log_string = "\n--------------\n{0}\n--------------\n".format(strftime("%A %d %B %Y %H:%M:%S"))
            print(log_string)
        else:
            print("\n[{0}] {1}".format(strftime("%H:%M:%S"), message))

def get_monster_dict():
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

    with open("../resources/cfg/monster.cfg", "r") as monster_config:
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
                line.split("\n")[0]
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
        try:
            list_encounters[i] = rd.choice(monsters_that_can_be_picked)
            monsters_that_can_be_picked.pop(monsters_that_can_be_picked.index(list_encounters[i]))
        except IndexError:
            list_encounters[i] = "None"
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
    
    #Getting the life points of monster : life => 3d6-1 => (3 x 6-sided dices) minus 1
    life = dice_roll(stats_of_monster["life"])
    ac = stats_of_monster["ac"] #Getting the Armor Class (AC)
    movement = stats_of_monster["movement"] #Getting the movement value
    attacks = stats_of_monster["attacks"]
    damages = stats_of_monster["damages"]
    number_met = dice_roll(stats_of_monster["number_met"])
    save_poison = stats_of_monster["saves"].split(";")[0]
    save_wands = stats_of_monster["saves"].split(";")[1]
    save_paralysis = stats_of_monster["saves"].split(";")[2]
    save_dragon = stats_of_monster["saves"].split(";")[3]
    save_spells = stats_of_monster["saves"].split(";")[4]
    moral = stats_of_monster["moral"]
    treasure = stats_of_monster["treasure"]
    alignment = stats_of_monster["alignment"]
    xp_value = stats_of_monster["xp_value"]
    return life, ac, movement, attacks, damages, number_met, save_poison, save_wands,\
    save_paralysis, save_dragon, save_spells, moral, treasure, alignment, xp_value

def dice_roll(xdypz):
    """returns the result of a roll of dices in the form of a string "xdy+z" or "xdy-z" or "xdy" """
    number_of_dices = int(xdypz.split("d")[0])
    if "+" in xdypz:
        sides_of_dice = int(xdypz.split("d")[1].split("+")[0])
        modifier_of_dice = int(xdypz.split("d")[1].split("+")[1])
    elif "-" in xdypz:
        sides_of_dice = int(xdypz.split("d")[1].split("-")[0])
        modifier_of_dice = int(xdypz.split("d")[1].split("-")[1]) *(-1)
    else:
        sides_of_dice = int(xdypz.split("d")[1])
        modifier_of_dice = 0

    temp=[]
    for i in range(number_of_dices):
        temp.append(rd.randint(1,sides_of_dice))
    return sum(temp)+modifier_of_dice

def get_treasure(treasure_value, has_magic_items=False, has_gems=True, has_jewels=True):
    treasure_value = round(rd.gauss(treasure_value,treasure_value/(rd.random()*10)), 2)
    treasure = {}
    if has_magic_items:
        treasure["magic_items"] = pick_magic_items()
        treasure_value = round(rd.random()*treasure_value, 2)
    if has_gems:
        rand = rd.uniform(0.2, 0.5)
        treasure["gems"] = pick_gems(treasure_value*rand)
        treasure_value = (1 - rand) * treasure_value
    if has_jewels:
        rand = rd.uniform(0.1, 0.3)
        treasure["jewels"] = pick_jewels(treasure_value*rand)
        treasure_value = (1 - rand) * treasure_value
    treasure_value = rd.uniform(0.4, 0.6) * treasure_value
    pp, gp, ep, sp, cp = get_treasure_coins(treasure_value)
    treasure["pieces"] = [pp, gp, ep, sp, cp]
    return treasure

def get_treasure_coins(treasure_value):
    float_part = (treasure_value-int(treasure_value))*100
    int_part = int(treasure_value)
    pp = int_part // 5
    gp = int_part - pp
    ep = float_part // 50
    float_part -= ep
    sp = float_part // 10
    cp = round(float_part - sp, 0)
    return int(pp), int(gp), int(ep), int(sp), int(cp)

def pick_magic_items(odds={"scroll":30,"weapons":5,"potions":50,"ring":10,"other":5,"wand":10}):
    has_item = {}
    magic_items  = read_config("magic_items")
    for key, value in odds.items():    
        if rd.randint(1,100)<=odds[key]:
            has_item[key] = True
        else:
            has_item[key] = False
    temp_list = []
    if has_item["scroll"]:
        temp_list.append(rd.choice(magic_items["scroll"]))
    if has_item["weapons"]:
        temp_list.append(rd.choice(magic_items["weapons"]))
    if has_item["potions"]:
        temp_list.append(rd.choice(magic_items["potions"]))
    if has_item["ring"]:
        temp_list.append(rd.choice(magic_items["ring"]))
    if has_item["other"]:
        temp_list.append(rd.choice(magic_items["other"]))
    if has_item["wands"]:
        temp_list.append(rd.choice(magic_items["wands"]))
    return temp_list

def pick_gems(treasure_value):
    gems = read_config("gems")
    gem_quality = []
    gem_type = []
    for i in range(int(treasure_value//300)):
        gem_quality.append(rd.choice(gems["gem_quality"]))
        gem_type.append(rd.choice(gems["gem_type"]))
    gems = []
    assert len(gem_type) == len(gem_quality)
    for i in range(len(gem_type)):
        gems.append((gem_quality[i][0] + " " + gem_type[i][0], int(gem_quality[i][1]) + int(gem_type[i][1])))
    return gems

def pick_jewels(treasure_value):
    jewels = read_config("jewels")
    jewel_quality = []
    jewel_material = []
    jewel_type = []
    for i in range(int(treasure_value // 250)):
        jewel_quality.append(rd.choice(jewels["jewel_quality"]))
        jewel_type.append(rd.choice(jewels["jewel_type"]))
        jewel_material.append(rd.choice(jewels["jewel_material"]))
    jewels = []
    assert len(jewel_material) == len(jewel_quality) == len(jewel_type)
    for i in range(len(jewel_type)):
        jewels.append((jewel_quality[i][0] + " " + jewel_material[i][0] + " " + jewel_type[i][0], int(jewel_material[i][1]) +\
        int(jewel_quality[i][1]) + int(jewel_type[i][1])))
    return jewels