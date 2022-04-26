import tkinter as tk
from tkinter import Menu, ttk
from calculator_package.Calculations import *
from champion_package.AbilityType import *
from champion_package.Champion import *
from patch_updater_package.JsonExtractor import *
from patch_updater_package.PatchUpdate import *
from calculator_package.Points import *
from calculator_package.AbilityCalculations import *

def update():
    PatchUpdate.getAllLastestVersion()
    dd_patch_number = PatchUpdate.getLatestPatch()
    cc_patch_number = Misc.ddToCcPatchNo(dd_patch_number)
    PatchUpdate.getAllLastestChampionNames(dd_patch_number)
    all_champion_name_list = PatchUpdate.getAllLocalChampionNames()
    all_champion_name_list_alpha = Misc.aplhaOnly(all_champion_name_list)
    print(all_champion_name_list)
    PatchUpdate.updateAllChampions(
        cc_patch_number, all_champion_name_list_alpha)

#root window
root = tk.Tk()

#Create menubar
menu_bar = Menu(root)
root.config(menu=menu_bar)

#create the file menu
file_menu = Menu(
    menu_bar,
    tearoff=0
)

#add menu items to file menu
file_menu.add_command(label='Update', command=lambda: update())

menu_bar.add_cascade(
    label="Options",
    menu=file_menu
)

def select(option):
    print(option)





root.mainloop()
