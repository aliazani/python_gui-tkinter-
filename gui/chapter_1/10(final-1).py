from tkinter import *

root = Tk()
root.title('Frames')
frame = Frame(root, height=400, width=400, bg='green', bd='8', relief=SUNKEN)
frame.pack()

btn1 = Button(frame, text='Button1')
btn2 = Button(frame, text='Button2')

btn1.pack(side=LEFT, padx=10)
btn2.pack(side=LEFT)

lbl_frame = LabelFrame(root, text='Search Box', padx=25, pady=20, bg='#fcd45d')
lbl_frame.pack(side=TOP)

lbl = Label(lbl_frame, text='Search Label', bg='#fcd45d')
lbl.pack(side=LEFT, padx=15)

entry = Entry(lbl_frame)
entry.pack(side=LEFT, padx=15)

btn_3 = Button(lbl_frame, text='Button')
btn_3.pack(side=LEFT, padx=15)

root.geometry('500x550')
root.mainloop()
