from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('450x450')
label = Label(root, text='Hello python')
# label['text'] = 'Hello Tkinter'
label.config(text='Hello Tkinter and bla bla bla just for test'
             , font='times 20', fg='red', bg='yellow', wraplength='200', justify='center')

label.pack()
root.mainloop()
