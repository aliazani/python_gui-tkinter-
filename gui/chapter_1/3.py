from tkinter import *

root = Tk()

lbl = Label(root, text='The first label.')
lbl.pack()


def back():
    lbl.config(text='The second label.', fg='red', bg='yellow')


btn = Button(root, text='Click me', command=back)
btn.pack()
# btn['state'] = 'disable'
btn['state'] = 'normal'
root.geometry('500x500')
root.mainloop()
