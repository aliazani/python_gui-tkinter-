from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('500x500')
button1 = Button(root, text='click 1')
button2 = ttk.Button(root, text='click 1')

button1.pack()
button2.pack()
root.mainloop()
