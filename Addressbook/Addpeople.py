from tkinter import *
import sqlite3
from tkinter import messagebox

connection = sqlite3.connect('database.db')
cursor = connection.cursor()


# cursor.execute('insert')


class AddPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('750x550+320+100')
        self.title('Add People')
        self.resizable(False, False)

        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=600, bg='#fcc324')
        self.bottom.pack(fill=X)
        # top
        self.add_people_icon = PhotoImage(file='./icons/addperson.png')
        self.add_people_label = Label(self.top, image=self.add_people_icon, bg='white')
        self.add_people_label.place(x=120, y=10)

        self.add_people_label_text = Label(self, text='My People', font='arial 15 bold', bg='white', fg='#003f8a')
        self.add_people_label_text.place(x=260, y=60)

        # Labels and entries

        self.first_name_label = Label(self.bottom, text='First Name:', bg='#fcc324', font='arial 15 bold', fg='white')
        self.first_name_input = Entry(self.bottom, width=35, bd=4)
        self.first_name_label.grid(row=0, column=0, pady=15, sticky=W)
        self.first_name_input.grid(row=0, column=1, pady=15)

        self.last_name_label = Label(self.bottom, text='Last Name:', bg='#fcc324', font='arial 15 bold', fg='white')
        self.last_name_input = Entry(self.bottom, width=35, bd=4)
        self.last_name_label.grid(row=1, column=0, pady=15, sticky=W)
        self.last_name_input.grid(row=1, column=1, pady=15)

        self.email_label = Label(self.bottom, text='Email:', bg='#fcc324', font='arial 15 bold', fg='white')
        self.email_input = Entry(self.bottom, width=35, bd=4)
        self.email_label.grid(row=2, column=0, pady=15, sticky=W)
        self.email_input.grid(row=2, column=1, pady=15)

        self.phone_number_label = Label(self.bottom, text='Phone Number:', bg='#fcc324', font='arial 15 bold',
                                        fg='white')
        self.phone_number_input = Entry(self.bottom, width=35, bd=4)
        self.phone_number_label.grid(row=3, column=0, pady=15, sticky=W)
        self.phone_number_input.grid(row=3, column=1, pady=15)

        self.address_label = Label(self.bottom, text='Address:', bg='#fcc324', font='arial 15 bold', fg='white')
        self.address_input = Text(self.bottom, width=35, height=4, wrap='word')
        self.address_label.grid(row=4, column=0, pady=15, sticky=W)
        self.address_input.grid(row=4, column=1, pady=15)
        self.btn_add_people = Button(self.bottom, text='Add', command=self.add_person)
        self.btn_add_people.grid(row=5, column=1, padx=(50, 0), pady=15, sticky=E)

    def add_person(self):
        first_name = self.first_name_input.get()
        last_name = self.last_name_input.get()
        email = self.email_input.get()
        phone = self.phone_number_input.get()
        address = self.address_input.get(1.0, END)

        if first_name and last_name and email and phone and address != '':
            try:
                query = f"INSERT INTO 'persons' (person_fname, person_lname, person_email, person_number, person_address) " \
                        f"VALUES(?,?,?,?,?)"
                cursor.execute(query, (first_name, last_name, email, phone, address))
                connection.commit()
                messagebox.showinfo('Success', 'Successfully added to database', icon='info')
            except:
                messagebox.showerror('Error', "Can't added to database", icon='warning')

        else:
            messagebox.showerror('Error', 'Fill all the fields', icon='warning')
