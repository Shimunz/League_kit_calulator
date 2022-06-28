import tkinter as tk
from tkinter import *
from tkinter import ttk

from DAO.ChampionDAO import *
from GUIEditor import *

def update():
    PatchDAO.update()

def open_editor(self):
    EditorFrame(self)

class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        ttk.Button(self,
                text='Editor',
                command=lambda:open_editor(self)).pack()
        self.pack()

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

        file_menu.add_command(label='Updater', command=lambda: open_editor(self))
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.destroy)


if __name__ == "__main__":

    ChampionDAO.all_champion_names = PatchUpdate.getAllLocalChampionNames()
    ChampionDAO.champion_list = ChampionDAO.getAllChampionStats(ChampionDAO.all_champion_names)

    app = App()
    frame = MainFrame(app)
    app.mainloop()
