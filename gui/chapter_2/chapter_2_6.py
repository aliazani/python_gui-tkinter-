from tkinter import *
from tkinter import messagebox


def exit_func():
    msg_box = messagebox.askyesnocancel('Exit', 'Are you sure to exit?', icon='warning')
    if msg_box is True:
        root.destroy()
    else:
        pass


root = Tk()

menu_bar = Menu(root)
root.config(menu=menu_bar)
file_bar = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='File', menu=file_bar)

file_bar.add_command(label='New')
file_bar.add_separator()
file_bar.add_command(label='Open')
file_bar.add_command(label='Save')
exit_item = PhotoImage(file='../icons/command.png')
file_bar.add_command(label='Exit', image=exit_item, compound=RIGHT, command=exit_func)

edit_bar = Menu(menu_bar)
menu_bar.add_cascade(label='Edit', menu=edit_bar)
about_bar = Menu(menu_bar)
menu_bar.add_cascade(label='About', menu=about_bar)

root.geometry('550x500+450+150')
root.mainloop()
