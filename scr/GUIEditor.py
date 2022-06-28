from pickle import NONE
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from DAO.ChampionDAO import *
import itertools



class EditorFrame(tk.Toplevel):

    champion_list = ChampionDAO.all_champion_names

    def __init__(self, container):
        super().__init__(container)

        self.champion_selected = tk.StringVar()
        self.champion_selected.trace('w', self.update)

        self.comboBox = ttk.Combobox(self, textvariable=self.champion_selected)
        
        self.create_select_champion_widget()
        self.tree = self.create_tree_widget()
        
    
    #auto updates the combox depending on user input
    #TODO: Make searching not case sensitive.
    def update(self, *args):
        newvalues=[i for i in self.champion_list if self.champion_selected.get() in i]
        self.comboBox['values']=newvalues

    def create_select_champion_widget(self):
        self.label = ttk.Label(self, text="Search Champion")
        #self.label.pack(side="left")
        self.label.grid(column=0, row=0)

        
        self.comboBox['values'] = self.champion_list
        self.comboBox.grid(column=1, row=0)
        #self.comboBox.pack(side="left")

    def create_tree_widget(self):
        champion_list = ChampionDAO.champion_list
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

        champ_stats = []

        for champs in ChampionDAO.champion_list:
            if champs.champion_properties['champion_name']=="Aatrox":
                champ = champs.champion_properties['stats'].total_stats
            break                    

        for c in champ:
            print (c)
            champ_stats.append((c, champ[c]))

        for i in champ_stats:
            tree.insert('', tk.END, values=i)        
            
        return tree

    def item_selected(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values']
            # show a message
            showinfo(title='Information', message=','.join(record))

    