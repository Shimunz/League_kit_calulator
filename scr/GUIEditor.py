from msilib.schema import ComboBox
from re import L
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name
from tkinter import *

class GUIEditor():
    def run():
        app = App()
        frame = MainFrame(app)
        app.mainloop()

class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.label = ttk.Label(self, text="Search Champion")
        self.label.pack(side="left")

        current_var = tk.StringVar()
        self.comboBox = ttk.Combobox(self, textvariable=current_var)
        self.comboBox['values'] = [month_name[m][0:3] for m in range(1, 13)] 
        self.comboBox.pack(side="left")
        
        self.pack()

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        # Configure Root window
        self.title("Editor")

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
        option_menu.add_command(label='Update')

        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.destroy)


if __name__ == "__main__":
    app = App()
    frame = MainFrame(app)
    app.mainloop()
