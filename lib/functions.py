# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 10:21:25 2015

@author: Simon
"""
from time import strftime
import sys
import random as rd

if __name__ == "__main__":
    current_folder = "../resources/cfg"
else:
    current_folder = "resources/cfg"

def read_config(file_name):
    """Function that reads the config of given filename, returns dict"""
    return_dict = dict()
    temp_list = list()
    with open("{}/{}.cfg".format(current_folder, file_name), "r") as config_file:
        for line in config_file:
            try:
                assert line != '\n', "line is empty, skipping line"
                if "{" in line:
                    name = line.split("{")[0]
                elif "}" in line:
                    return_dict[name] = temp_list
                    temp_list = []
                else:
                    if ";" in line:
                        line = line.split("\n")[0]
                        to_append = line.split(";")
                    else:
                        to_append = line.split("\n")[0]
                    temp_list.append(to_append)
                    del to_append
            except AssertionError:
                continue
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
            log_string = "\n--------------\n{0}\n--------------\n".format(strftime("%A %d %B %Y %H:%M:%S"))
            log_out.write(log_string)
        else:
            log_out.write("\n[{0}] {1}".format(strftime("%H:%M:%S"), message))

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

    with open("./resources/cfg/monsters.cfg", "r") as monster_config:
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

def pick_magic_items(odds={"scroll":30,"weapons":5,"potions":50,"ring":10,"other":5,"wands":10}):
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

def class_differenciation(class_, race, characteristics):
    base_xp = 0
    main_char = {"class":0,"race":0}
    if class_ == "Warrior":
        base_xp += 2000
        main_char["class"] = int(characteristics["str"])
    elif class_ == "Wizard":
        base_xp += 2500
        main_char["class"] = int(characteristics["int"])
    elif class_ == "Cleric":
        base_xp += 1500
        main_char["class"] = int(characteristics["wis"])
    elif class_ == "Thief":
        base_xp += 1200
        main_char["class"] = int(characteristics["dex"])
    else:
        base_xp += 0
    if race == "Human":
        base_xp += 0
        main_char["race"] = int(characteristics["cha"])
    elif race == "Elf":
        base_xp += 1500
        main_char["race"] = int(characteristics["str"])
    elif race == "Dwarf":
        base_xp += 500
        main_char["race"] = int(characteristics["con"])
    elif race == "Halfelin":
        base_xp += 800
        main_char["race"] = int(characteristics["dex"])
    return base_xp, main_char

def get_remaining_xp(base_xp, level, xp_total):
    return (int(base_xp) * int(level)) - int(xp_total)

def get_bonus_xp(main_char):
    bonus_percentage = 0
    if 16 <= main_char["class"] <= 18:
        bonus_percentage += 5
    elif 13 <= main_char["class"] <= 15:
        bonus_percentage += 0
    elif 9 <= main_char["class"] <= 12:
        bonus_percentage -= 5
    elif 3 <= main_char["class"] <= 8:
        bonus_percentage -= 10
    else:
        bonus_percentage = 0

    if 16 <= main_char["race"] <= 18:
        bonus_percentage += 5
    elif 13 <= main_char["race"] <= 15:
        bonus_percentage += 0
    elif 9 <= main_char["race"] <= 12:
        bonus_percentage -= 5
    elif 3 <= main_char["race"] <= 8:
        bonus_percentage -= 10
    else:
        bonus_percentage = 0
    return bonus_percentage

def add_xp(xp_to_add, class_, race, characteristics, level, current_xp):
    base_xp, main_char = class_differenciation(class_, race, characteristics)
    bonus = get_bonus_xp(main_char)
    try:
        xp_to_add = int(xp_to_add)
    except ValueError:
        xp_to_add = 0
    finally:
        xp_total = current_xp
        xp_total += xp_to_add * (1 + bonus/100)
        xp_to_add = 0
        remaining_xp = get_remaining_xp(base_xp, level, xp_total)
        if xp_total >= remaining_xp:
            level += 1
    return level, xp_total

def roll_characteristics(freeze=True):
    characteristics = {"str":0,"int":0,"wis":0,"dex":0,"con":0,"cha":0}
    if not freeze:
        for char, value in characteristics.items():
            characteristics[char] = rd.randint(1, 6) + rd.randint(1, 6) + rd.randint(1, 6)
    return characteristics

def generate_npc(alignment, gender, race, class_, level, stats):
    characteristics = {"str":0,"int":0,"wis":0,"dex":0,"con":0,"cha":0}
    npc_dict = read_config("npc-gen")
    if "Any" in alignment:
        try:
            assert alignment != "Any"
            alignment = alignment.split(" ")[1] + " " + rd.choice(["Good", "Neutral", "Evil"])
        except AssertionError:
            alignment = rd.choice(["Lawful", "Neutral", "Chaotic"]) + " " + rd.choice(["Good", "Neutral", "Evil"])
    if gender == "Any":
        gender = rd.choice(["Male", "Female"])
    if race == "Any":
        race = rd.choice(["Human", "Elf", "Dwarf", "Halfelin"])
    if class_ == "Any":
        class_ = rd.choice(["Warrior", "Wizard", "Thief", "Cleric"])
    if stats == "Best 3 of 5d6":
        for stat, stat_value in characteristics.items():
            dice_rolls=[]
            for i in range(5):
                dice_rolls.append(rd.randint(1,6))
            characteristics[stat] = sum(sorted(dice_rolls)[2:])
    elif stats == "Low":
        for stat, stat_value in characteristics.items():
            dice_rolls=[]
            dice_rolls.append(rd.randint(1,6))
            dice_rolls.append(rd.randint(1,6))
            characteristics[stat] = sum(dice_rolls)
    elif stats == "Average":
        for stat, stat_value in characteristics.items():
            characteristics[stat] = 6 + rd.randint(1,8)
    else:
        for stat, stat_value in characteristics.items():
            characteristics[stat] = 12 + rd.randint(1,6)

    name = get_npc_name(npc_dict, race, gender)
    languages = get_npc_languages(npc_dict, characteristics["int"], race, alignment)
    beliefs = get_npc_beliefs(npc_dict, alignment)
    recent_past, motivation = get_npc_motivation(npc_dict)
    npc_ac, belongings = get_npc_belongings(npc_dict, level)
    life = dice_roll("{}d6+2".format(level))

    string_to_return = \
    """{}, {} {} {}, level {}, {} HP, {} AC\n
    Alignment : {}, believes in : {}\n
    Stats : \tSTR : {}\n
    \t\tINT : {}\n
    \t\tWIS : {}\n
    \t\tDEX : {}\n
    \t\tCON : {}\n
    \t\tCHA : {}\n
    \n
    Language(s) spoken : {}\n
    \n
    Belongings : {}\n
    \n
    Motivation : {}\n
    \n
    Recent Past : {}\n
    """.format(name.capitalize(), gender, class_, race, level, life, npc_ac, alignment, beliefs,\
    characteristics["str"], characteristics["int"], characteristics["wis"],\
    characteristics["dex"], characteristics["con"], characteristics["cha"],\
    languages, belongings, motivation, recent_past)
    return string_to_return

def get_npc_name(npc_dict, race, gender):
    race = race.lower()
    gender = gender.lower()
    names = npc_dict["{}_names".format(race)]
    preffixes = []
    intermediate = []
    suffixes = []
    if gender is "male" or gender is "m":
        gender = "m"
    else:
        gender = "f"
    for value_lists in names:
        if value_lists[0] == "{}pre".format(gender):
            preffixes.append(value_lists[1])
        else:
            preffixes.append(value_lists[1])
        if "{}suf".format(gender) == value_lists[0]:
            suffixes.append(value_lists[1])
        else:
            suffixes.append(value_lists[1])
        if "{}in".format(gender) == value_lists[0]:
            intermediate.append(value_lists[1])
        else:
            intermediate.append("")
    return rd.choice(preffixes) + rd.choice(intermediate) + rd.choice(suffixes)

def get_npc_languages(npc_dict, intelligence, race, alignment):
    languages = "Common, {}".format(alignment.capitalize())
    available_languages = npc_dict["languages"]
    nbr = 0
    if intelligence >= 17:
        nbr += 2
    elif 17 > intelligence >= 14:
        nbr += 1
    elif 9 > intelligence >= 6:
        return "Common spoken with difficulties"
    elif 6 > intelligence >= 3:
        return "Can't read common, speaks with a lot of trouble"
    if race.lower() is not "human":
        languages += ", {}".format(race.capitalize())
        available_languages.remove(race.lower())
    for i in range(nbr):
        lang = rd.choice(available_languages)
        available_languages.remove(lang)
        languages += ", {}".format(lang.capitalize())
    return languages

def get_npc_beliefs(npc_dict, alignment):
    gods = npc_dict["churches"]
    law_gods = []
    neu_gods = []
    cha_gods = []
    for god in gods:
        if "on" in god or "or" in god:
            law_gods.append(god)
        elif "k" in god or "sh" in god or "x" in god or "y" in god:
            cha_gods.append(god)
        else:
            neu_gods.append(god)
    if "Lawful" in alignment:
        return rd.choice(law_gods)
    elif "Chaotic" in alignment:
        return rd.choice(cha_gods)
    else:
        return rd.choice(neu_gods)

def get_npc_motivation(npc_dict):
    recent_past = replace_bracket_words(rd.choice(npc_dict["recent_past"]), npc_dict)
    motivation = replace_bracket_words(rd.choice(npc_dict["motivations"]), npc_dict)
    return recent_past, motivation

def get_npc_belongings(npc_dict, level):
    npc_ac = 9
    npc_belongings_value = int(level) * 100 * rd.gauss(1,0.5)
    weapons = rd.choice(npc_dict["weapons"])
    return npc_ac, npc_belongings

def replace_bracket_words(sentence, npc_dict):
    word = ""
    if "[" in sentence:
        word = sentence[sentence.index("[")+1:sentence.index("]")]
        sentence = sentence.replace("[{}]".format(word), rd.choice(npc_dict[word]), 1)
        return replace_bracket_words(sentence, npc_dict)
    else:
        return sentence

def generate_disease(source, climate, sequel): # change sex, breathing in combo box  scratch that, change every item
    disease_dict = read_config("diseases")
    name = rd.choice(disease_dict["preffix"]) + rd.choice(disease_dict["intermediary"]) + rd.choice(disease_dict["suffix"])
    name = name.capitalize()
    if climate == "Random":
        climate = rd.choice(disease_dict["climates"])
    if source == "Random":
        source = rd.choice(disease_dict["source"])
    if sequel == "Random":
        sequel = rd.choice(disease_dict["sequels"])
    incubation = str(dice_roll("{}d{}+{}".format(rd.randint(1, 3), rd.randint(2, 12), rd.randint(-2, 2)))) \
    + " {}".format(rd.choice(disease_dict["incubation"]))
    time_after_sequel = "{}d{}+{}".format(rd.randint(1, 3), rd.randint(2, 12), rd.randint(-2, 2))\
    + " {}".format(rd.choice(disease_dict["incubation"]))

    effect_immediate = rd.choice(disease_dict["sequels"])
    if "stat" in effect_immediate:
        stat = rd.choice(disease_dict["stats_loss"])
        effect_immediate = effect_immediate.split("stat")[0]
        effect_immediate += " " + stat[1] + " " + stat[0]
    if "stat" in sequel:
        stat = rd.choice(disease_dict["stats_loss"])
        sequel = sequel.split("stat")[0]
        sequel += " " + stat[1] + " " + stat[0]

    string =\
    """
    {}, disease contracted by {}
    
    Incubation time : {}
    
    Effect : immediate {}, {}, {} later if not cured before.
    """.format(name, source, incubation, effect_immediate, sequel, time_after_sequel)
    return string

    
