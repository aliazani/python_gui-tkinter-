from tkinter import *


def text():
    values = text_editor.get(1.0, END)
    print(values)


root = Tk()
text_editor = Text(root, width=30, height=3, font=(('Arial'), 20), wrap='word')
text_editor.grid(row=0, column=0, padx=40, pady=20)
text_editor.insert(INSERT, 'This is for test.')
btn = Button(root, text='Save', command=text, width=10, height=1).grid(row=3, column=2)
root.geometry('800x500')
root.mainloop()
