from ipaddress import collapse_addresses
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

from DAO.ChampionDAO import *


class EditorFrame(tk.Toplevel):
    def __init__(self, container):
        super().__init__(container)

        self.label = ttk.Label(self, text="Search Champion")
        self.label.pack(side="left")

        current_var = tk.StringVar()
        self.comboBox = ttk.Combobox(self, textvariable=current_var)
        self.comboBox['values'] = ChampionDAO.all_champion_names
        self.comboBox.pack(side="left")
        
        columns = ('champion')

        tree = ttk.Treeview(self, columns=columns, show='headings')
        tree.heading('Champion', text="Champion")

        for i in ChampionDAO.all_champion_names:
            tree.insert('', tk.END, values=i)

        tree.grid(row=0, column=0, sticky='nsew')

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        tree.pack()
        self.pack()