import tkinter as tk
from calendar import month_name
from msilib.schema import ComboBox
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo


class EditorFrame(tk.Toplevel):
    def __init__(self, container):
        super().__init__(container)

        self.label = ttk.Label(self, text="Search Champion")
        self.label.pack(side="left")

        current_var = tk.StringVar()
        self.comboBox = ttk.Combobox(self, textvariable=current_var)
        self.comboBox['values'] = [month_name[m][0:3] for m in range(1, 13)] 
        self.comboBox.pack(side="left")
        