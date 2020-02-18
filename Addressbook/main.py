from tkinter import *
from datetime import datetime
import myPeople
import Addpeople
import about


class Application():

    def __init__(self, root):
        self.root = root
        self.top = Frame(root, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottom = Frame(root, height=500, bg='#ADFF2F')
        self.bottom.pack(fill=X)
        # top
        self.phone_book_icon = PhotoImage(file='./icons/book.png')
        self.phone_book_label_icon = Label(self.top, image=self.phone_book_icon, bg='white')
        self.phone_book_label_icon.place(x=120, y=10)

        self.phone_book_label = Label(root, text='My Phone Book', font='arial 15 bold', bg='white', fg='#ffa500')
        self.phone_book_label.place(x=260, y=60)

        self.date_label = Label(self.top, text="Today's date " + str(datetime.now().date()), font='arial 12 bold',
                                bg='white', fg='#ffa500')
        self.date_label.place(x=450, y=5)

        # bottom

        self.my_people_icon = PhotoImage(file='./icons/man.png')
        self.my_people_btn = Button(self.bottom, text='    My People    ', font='arial 12 bold',
                                    image=self.my_people_icon,
                                    compound=LEFT, command=self.open_my_people)
        self.my_people_btn.place(x=250, y=10)

        self.add_people_icon = PhotoImage(file='./icons/add.png')
        self.add_people_btn = Button(self.bottom, text='   Add People   ', font='arial 12 bold',
                                     image=self.add_people_icon,
                                     compound=LEFT, command=self.add_people)
        self.add_people_btn.place(x=250, y=70)

        self.about_icon = PhotoImage(file='./icons/info.png')
        self.about_btn = Button(self.bottom, text='     About Us     ', font='arial 12 bold', image=self.about_icon,
                                compound=LEFT, command=self.about_us)
        self.about_btn.place(x=250, y=130)

    def open_my_people(self):
        myPeople.MyPeople()

    def add_people(self):
        Addpeople.AddPeople()

    def about_us(self):
        about.About()


def main():
    root = Tk()
    app = Application(root)
    root.title('Address Book')
    root.geometry('650x550+650+100')
    root.resizable(False, False)

    root.mainloop()


if __name__ == '__main__':
    main()
