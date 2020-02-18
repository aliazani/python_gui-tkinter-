from tkinter import *
from tkinter import filedialog


def open_file():
    file_name = filedialog.askopenfilename(initialdir='/~/', title='open a file',
                                           filetypes=(('Text file', '.txt'), ('All files', '*.*')))
    if file_name is '':
        return

    content = open(file_name, 'r').read()
    text_editor.insert(END, content)


root = Tk()

text_editor = Text(root, width=25, height=15, wrap='word')
text_editor.pack()
button = Button(root, text='open', command=open_file).pack()

root.geometry('450x450+650+650')
root.mainloop()
