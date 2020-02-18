from tkinter import *

root = Tk()


def back():
    username = entry_1.get()
    password = entry_2.get()
    print(username)
    print(password)


title = Label(text='Select Lesson')
lbl_name = Label(text='Name:')
lbl_pass = Label(text='password:')
entry_1 = Entry(width=40)
entry_2 = Entry(width=40)
btn = Button(text='Enter', command=back)
title.grid(row=0, column=0, columnspan=2)
lbl_name.grid(row=1, column=0, sticky=W, pady=5)
lbl_pass.grid(row=2, column=0, sticky=W, pady=5)
entry_1.grid(row=1, column=1, pady=5)
entry_2.grid(row=2, column=1, pady=5)
btn.grid(row=3, column=1, sticky=E, pady=5)
root.geometry('450x450')
root.mainloop()
