from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3


class MainMenu(Menu):
    def __init__(self, parent, *args, **kwargs):
        Menu.__init__(self, parent, *args, **kwargs)
        self.parent = parent


class MainApplication(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pack(fill=BOTH, expand=True)

        # Widgets
        self.main_menu = MainMenu(self)

        # Menu configuration
        self.parent.config(menu=self.main_menu)


if __name__ == '__main__':
    root = Tk()
    root.title('Text editor')
    MainApplication(root).pack(side=TOP, fill=BOTH, expand=True)
    root.iconbitmap('icons/icon.ico')
    root.geometry('1250x750+100+20')
    root.mainloop()
