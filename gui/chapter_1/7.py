from tkinter import *
from tkinter import messagebox

root = Tk()


def delete():
    answer = messagebox.askyesno('Delete', 'Are you sure you want to delete?')
    if answer is True:
        print('Deleted.')
    else:
        print('NOT deleted.')


def info():
    messagebox.showinfo('Info', 'Well done')
    print('This is info.')


btn_1 = Button(root, text='Delete', command=delete).grid(row=0, column=0, padx=30, pady=50)
btn_2 = Button(root, text='Info', command=info).grid(row=0, column=1, padx=30, pady=50)

root.geometry('450x500')
root.mainloop()
