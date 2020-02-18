from tkinter import *

root = Tk()

text_box = Text(root, width=40, height=15)
text_box.grid(row=0, column=0)

scroll = Scrollbar(root, orient=VERTICAL, command=text_box.yview)
scroll.grid(row=0, column=1, stick=N+S)

text_box.config(yscrollcommand=scroll.set)

root.geometry('550x500+450+150')
root.mainloop()
