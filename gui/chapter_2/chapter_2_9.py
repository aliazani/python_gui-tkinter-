from tkinter import *

root = Tk()
canvas = Canvas(root, width=650, height=550)
canvas.pack()
rectangle = canvas.create_rectangle(150, 150, 250, 250, fill='green', width=10)

root.geometry('550x500+450+150')
root.mainloop()
