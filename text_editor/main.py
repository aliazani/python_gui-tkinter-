from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

show_status_bar = True
show_tool_bar = True


class TextEditor(Text):
    def __init__(self, parent, *args, **kwargs):
        Text.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.config(wrap='word', relief=FLAT)
        self.pack(fill=BOTH, expand=True)
        self.horizontal_scroll_bar = Scrollbar(self, orient=HORIZONTAL)
        self.horizontal_scroll_bar.pack(side=BOTTOM, fill=X)
        self.vertical_scroll_bar = Scrollbar(self, orient=VERTICAL)
        self.vertical_scroll_bar.pack(side=RIGHT, fill=Y)
        self.horizontal_scroll_bar.config(command=self.xview)
        self.vertical_scroll_bar.config(command=self.yview)
        self.config(xscrollcommand=self.horizontal_scroll_bar.set)
        self.config(yscrollcommand=self.vertical_scroll_bar.set)

class MainMenu(Menu):
    def __init__(self, parent, *args, **kwargs):
        Menu.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        # File
        self.new_icon = PhotoImage(file='icons/new.png')
        self.open_icon = PhotoImage(file='icons/open.png')
        self.save_icon = PhotoImage(file='icons/save_icon.png')
        self.exit_icon = PhotoImage(file='icons/exit.png')
        self.file = Menu(self, tearoff=0)
        self.file.add_command(label='New', image=self.new_icon, compound=LEFT, accelerator='Ctrl+N')
        self.file.add_command(label='Open', image=self.open_icon, compound=LEFT, accelerator='Ctrl+O')
        self.file.add_command(label='Save', image=self.save_icon, compound=LEFT, accelerator='Ctrl+S')
        self.file.add_command(label='Save As', image=self.save_icon, compound=LEFT, accelerator='Ctrl+Alt+S')
        self.file.add_command(label='Exit', image=self.exit_icon, compound=LEFT)

        self.add_cascade(label='File', menu=self.file)

        # Edit
        self.edit = Menu(self, tearoff=0)
        self.edit.add_command(label='Copy', accelerator='Ctrl+C')
        self.edit.add_command(label='Cut', accelerator='Ctrl+X')
        self.edit.add_command(label='Paste', accelerator='Ctrl+P')
        self.edit.add_command(label='Clear All', accelerator='Ctrl+Alt+C')
        self.edit.add_command(label='Find', accelerator='Ctrl+F')

        self.add_cascade(label='Edit', menu=self.edit)

        # View
        global show_status_bar
        global show_tool_bar
        self.view = Menu(self, tearoff=0)
        self.view.add_checkbutton(onvalue=True, offvalue=False, var=show_tool_bar, label='Tool Bar')
        self.view.add_checkbutton(onvalue=True, offvalue=False, var=show_status_bar, label='Status Bar')

        self.add_cascade(label='View', menu=self.view)

        # Templates

        self.templates = Menu(self, tearoff=0)
        self.color_choice = StringVar()
        self.color_dic = {
            'Default': '#000000.#FFFFFF',  # first one is the font color and second one is the background color
            'Tomato': '#ffff00.#ff6347',
            'LimeGreen': '#fffff0.#32cd32',
            'Magenta': '#fffafa.#ff00ff',
            'RoyalBlue': '#ffffbb.#4169e1',
            'MediumBlue': '#d1e7e0.#0000cd',
            'Dracula': '#ffffff.#000000'
        }
        for color in sorted(self.color_dic):
            self.templates.add_radiobutton(label=color, var=self.color_choice)
        self.add_cascade(label='Templates', menu=self.templates)

        # About

        self.about = Menu(self, tearoff=0)
        self.about.add_command()

        self.add_cascade(label='About', menu=self.about)


class MainApplication(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pack(fill=BOTH, expand=True)

        # Widgets
        self.main_menu = MainMenu(self)

        self.text_editor = TextEditor(self)
        self.text_editor.focus()

        # Menu configuration
        self.parent.config(menu=self.main_menu)


if __name__ == '__main__':
    root = Tk()
    root.title('Text editor')
    MainApplication(root).pack(side=TOP, fill=BOTH, expand=True)
    root.iconbitmap('icons/icon.ico')
    root.geometry('1250x750+100+20')
    root.mainloop()
