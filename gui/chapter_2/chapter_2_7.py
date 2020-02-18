from tkinter import *
from tkinter import ttk

root = Tk()


def show_func(event):
    items = tree_view.identify('item', event.x, event.y)
    print(f'You clicked {tree_view.item(items, "text")}')


tree_view = ttk.Treeview(root)
tree_view.pack()

tree_view.insert('', 0, 'item 0', text='first item')
tree_view.insert('', 1, 'item 1', text='second item')
tree_view.insert('', 2, 'item 2', text='third item')
tree_view.insert('', 3, 'item 3', text='forth item')
tree_view.insert('', 4, 'item 4', text='fifth item')
tree_view.insert('', 5, 'item 5', text='sixth item')

tree_view.move('item 5', 'item 0', 'end')
tree_view.bind('<Double-1>', show_func)

root.geometry('550x500+450+150')
root.mainloop()
