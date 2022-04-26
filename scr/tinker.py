import tkinter as tk
from tkinter import *
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


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        # Configure Root window
        self.title("League Kit Calculator")

        # Create menubar
        menu_bar = Menu(self)
        self.config(menu=menu_bar)

        # create the file menu
        file_menu = Menu(
            menu_bar,
            tearoff=0
        )

        option_menu = Menu(
            menu_bar,
            tearoff=0
        )

        menu_bar.add_cascade(
            label="File",
            menu=file_menu
        )

        menu_bar.add_cascade(
            label="Options",
            menu=option_menu
        )

        # add menu items to file menu
        option_menu.add_command(label='Update', command=lambda: update())

        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.destroy)

        


if __name__ == "__main__":
    app = App()
    app.mainloop()
