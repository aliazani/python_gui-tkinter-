from tkinter import *
from tkinter import ttk

root = Tk()

icon = PhotoImage(file='../icons/command.png')
print(icon)
tabs = ttk.Notebook(root)
tabs.pack(fill=BOTH, expand=True)

frame_1 = Frame(tabs)
frame_2 = Frame(tabs)

tabs.add(frame_1, text='Tab 1')
tabs.add(frame_2, text='Tab 2', image=icon, compound=RIGHT)

lbl = Label(frame_1, text='Hello man.').place(x=250, y=20)
btn = Button(frame_2, text='Click ME!!').place(x=350, y=25)

root.geometry('550x500+500+150')
root.mainloop()
