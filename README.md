# DnDApp
The GitHub repository for DnDApp 

https://www.reddit.com/r/Python/comments/3evsrz/hello_rpython_im_looking_for_willing_devs_to_work/
# What is it ?

DnD stands for dungeons & dragons a well-known tabletop roleplaying game, where the goal is to play as a character to venture into unknown lands, a magic-filled world, slain powerfull monsters and level up your character. Sounds a lot like skyrim, without any limitation, no scripted NPCs, no annoying unkillable children. Because you imagine everything that happens, and you can do anything. If you want to kill a beggar just for the kicks of it, then be it, if you don't want to save the world through the questline that your DM carefully brewed, you can do it.


This application, or software, is aimed at playing online with friends to tabletop RPGs.  The software will be released with a Creative Commons license, and will be open source, because it should be maintained by its users. Some features could be neat to have, and a dev team can't think of everything, that's why it will be open source.

This started as a hobby I (Dogeek) had, now I think it can grow bigger and be helpful to a bunch of other rolists.

# Goals :

The DnDApp has to be VERY user friendly. Character sheet skins should be made easy to do. It should be modular, and have a clean code (whoa, there's work to do to make it clean !), be lightweight, as much as possible, and portable.

Priorities (decreasing order):

- make every tab work, make the networking work
- handle errors well, autosave features
- make it bandwidth efficient, to be able to use it even with horrible internet connections
- make it customizable using skins, at first for character sheets, then maybe for everything
- support of translations
- in-app chat, nice-looking GUI, streaming music to players, voice chat, video chat maybe, interface designed for playing...


# To Do List :

[ ] "hide" checkbox to hide dice rolls from other players, but not the DM (host)

[ ] network functions

[x] The level, xp, remaining xp features don't work for some reason

 | [ ] It now needs automatic refresh (clicking on the button is kind of a hassle)
 
[ ] Sections not built yet : Encounters, Treasures, Connection to host, Help page, load character sheet, display dices of others connected

[ ] Simultaneous host/Clients connections

[ ] Add a Stop button, to stop hosting

[ ] Handle exceptions

[x] cx_freeze to distribute the program

[ ] improve dice interface

[ ] slightly improve character Sheet interface with some padding, and add a Text Widget to keep track of treasures and inventory

[x] Add a button to roll caracteristics on the character sheet tab.

[ ] Add translation support

[ ] Add character sheet skins for other RPGs

# Design of the map tab :

