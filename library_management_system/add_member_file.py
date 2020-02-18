from tkinter import *
from tkinter import messagebox
import sqlite3

connection = sqlite3.connect('library.db')
cursor = connection.cursor()


class AddMember(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('750x600+450+100')
        self.resizable(False, False)
        self.title('Add Member')
        # Frames
        self.top_frame = Frame(self, bg='white', height=120)
        self.top_frame.pack(fill=X)
        self.bottom_frame = Frame(self, bg='#fcc324', height=480)
        self.bottom_frame.pack(fill=X)

        # Widgets
        self.add_person_icon = PhotoImage(file='icons/addperson.png')
        self.add_person_label = Label(self.top_frame, image=self.add_person_icon, bg='white')
        self.add_person_label.place(x=120, y=10)
        self.header = Label(self.top_frame, text='Add Person', font='arial 16 bold', fg='#003f8a', bg='white')
        self.header.place(x=290, y=60)

        self.name_label = Label(self.bottom_frame, text='Person Name:', font='arial 14 bold', fg='white', bg='#fcc324')
        self.name_entry = Entry(self.bottom_frame, width=35, bd=3)
        self.name_label.place(x=40, y=40)
        self.name_entry.place(x=180, y=40)

        self.phone_label = Label(self.bottom_frame, text='Phone Number:', font='arial 14 bold', fg='white',
                                 bg='#fcc324')
        self.phone_entry = Entry(self.bottom_frame, width=35, bd=3)
        self.phone_label.place(x=40, y=100)
        self.phone_entry.place(x=180, y=100)

        self.btn_add_person = Button(self.bottom_frame, text='Add', command=self.add_person_function)
        self.btn_add_person.place(x=420, y=150)

    def add_person_function(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if (name and phone) != '':
            try:
                query = "INSERT INTO 'members' (member_name, member_phone) VALUES (?, ?)"
                cursor.execute(query, (name, phone))
                connection.commit()
                messagebox.showinfo('Success', 'Successfully added to database', icon='info')
            except:
                messagebox.showerror('Failed', 'Failed to add to database', icon='warning')
        else:
            messagebox.showerror('Failed', 'Fields can not be empty', icon='warning')
