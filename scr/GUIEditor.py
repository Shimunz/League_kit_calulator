import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from DAO.ChampionDAO import *


class EditorFrame(tk.Toplevel):
    def __init__(self, container):
        super().__init__(container)

        self.searchbox = self.create_select_champion_widget()

        self.tree = self.create_tree_widget()
    
    def create_select_champion_widget(self):
        self.label = ttk.Label(self, text="Search Champion")
        #self.label.pack(side="left")
        self.label.grid(column=0, row=0)

        current_var = tk.StringVar()
        self.comboBox = ttk.Combobox(self, textvariable=current_var)
        self.comboBox['values'] = ChampionDAO.all_champion_names
        self.comboBox.grid(column=1, row=0)
        #self.comboBox.pack(side="left")

    def create_tree_widget(self):
        columns = ('attribute', 'value')
        tree = ttk.Treeview(self, columns=columns, show='headings')

        #define headings
        tree.heading('attribute', text="Attribute")
        tree.heading('value', text="Value")

        tree.bind('<<TreeviewSelect>>', self.item_selected)
        tree.grid(row=1, column=1, sticky=tk.NSEW)
        #tree.pack(fill='x')

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=2, sticky='ns')
        #scrollbar.pack(side='right',fill='y')

        tree.configure(yscrollcommand=scrollbar.set)

        champions = []
        for i in ChampionDAO.all_champion_names:
            champions.append(i)

        for c in ChampionDAO.all_champion_names:
            tree.insert('', tk.END, values=c)

        return tree

    def item_selected(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values']
            # show a message
            showinfo(title='Information', message=','.join(record))

    