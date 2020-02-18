from tkinter import *
from tkinter import ttk

root = Tk()

paned_window = ttk.PanedWindow(root, orient=HORIZONTAL)
paned_window.pack(fill=BOTH, expand=True)

frame_1 = ttk.Frame(paned_window, height=200, width=300, relief=SUNKEN)
frame_2 = ttk.Frame(paned_window, height=200, width=100, relief=SUNKEN)
frame_3 = ttk.Frame(paned_window, height=200, width=75, relief=SUNKEN)
paned_window.add(frame_1, weight=3)
paned_window.add(frame_2, weight=1)
paned_window.insert(1, frame_3)

lbl = Label(frame_1, text='Name:').grid(row=0, column=0, pady=20)
btn = Button(frame_1, text='Click me ').grid(row=0, column=1, pady=20)

root.geometry('500x500+400+100')
# The + is for first location of tk application
root.mainloop()
