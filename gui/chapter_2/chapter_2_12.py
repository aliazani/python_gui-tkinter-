from tkinter import *
from tkinter import filedialog


def open_file():
    file_name = filedialog.askopenfilename(initialdir='/~/', title='open a file',
                                           filetypes=(('Text file', '.txt'), ('All files', '*.*')))

    if file_name is '':
        return
    content = open(file_name, 'r').read()
    text_editor.insert(END, content)


def save_file():
    file_name = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if file_name is None:
        return
    content = text_editor.get(1.0, 'end-1c')
    file_name.write(content)


root = Tk()

text_editor = Text(root, width=25, height=15, wrap='word')
text_editor.pack()
button1 = Button(root, text='open', command=open_file).pack(side=LEFT, padx=(180, 10))
button2 = Button(root, text='save', command=save_file).pack(side=LEFT)

root.geometry('450x450+650+650')
root.mainloop()
