from tkinter import *
from tkinter import ttk

root = Tk()
entry_1 = Entry(root, width=30)
entry_1.insert(0, 'Enter your name:')
entry_2 = ttk.Entry(root, width=30, show='*')


def back():
    user = entry_1.get()
    password = entry_2.get()
    print('username is :', user)
    print('password is :', password)


btn = ttk.Button(root, text='Enter', command=back)
entry_1.pack()
entry_2.pack()
btn.pack()
root.geometry('400x400')
root.mainloop()
