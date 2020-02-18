from tkinter import *
from tkinter import ttk

root = Tk()


def print_items():
    items = list_box.curselection()
    for item in items:
        print(list_box.get(item))


def delete_items():
    items = list_box.curselection()
    for item in items:
        list_box.delete(item)


list_box = Listbox(root, width=20, height=15, selectmode=MULTIPLE)
list_box.insert(0, 'Python')
list_box.insert(1, 'C')
list_box.insert(2, 'C++')
list_box.insert(3, 'C#')
list_box.pack(pady=25)
btn_1 = Button(root, text='print', command=print_items).place(x=300, y=300)
btn_2 = Button(root, text='delete', command=delete_items).place(x=200, y=300)

root.geometry('550x500+450+150')
root.mainloop()
