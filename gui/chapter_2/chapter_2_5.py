from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Using images')

logo = PhotoImage(file='../icons/logo.png')

lbl_text = Label(root, text='Image', font=(('Times'), 15))
lbl_text.pack()

lbl_image = Label(root, image=logo)
lbl_image.pack()

root.geometry('550x500+450+150')
root.mainloop()
