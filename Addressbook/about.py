from tkinter import *


class About(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.frame = Frame(self, bg='#ffa500', width=550, height=550)
        self.frame.pack(fill=BOTH)
        self.text = Label(self.frame, bg='#ffa500', font='arial 14 bold', fg='white'
                          , text='This is about us page you can find more \n'
                                 'aliazn2013@yahoo.com\n'
                                 'This application is created for educational purposes.')
        self.text.place(x=50, y=50)

