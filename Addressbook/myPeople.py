from tkinter import *
from tkinter import messagebox
import sqlite3
import Addpeople

connection = sqlite3.connect('database.db')
cursor = connection.cursor()


class MyPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('750x550+320+100')
        self.title('My People')
        self.resizable(False, False)

        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=500, bg='#fcc324')
        self.bottom.pack(fill=X)
        # top
        self.my_people_icon = PhotoImage(file='./icons/person_icon.png')
        self.my_people_label = Label(self.top, image=self.my_people_icon, bg='white')
        self.my_people_label.place(x=120, y=10)

        self.my_people_label_text = Label(self, text='My People', font='arial 15 bold', bg='white', fg='#003f8a')
        self.my_people_label_text.place(x=260, y=60)

        # list box
        self.list_box = Listbox(self.bottom, width=60, height=30)
        self.list_box.grid(row=0, column=0, padx=(40, 0))
        persons = cursor.execute('SELECT * FROM persons').fetchall()
        count = 0
        for person in persons:
            self.list_box.insert(count + 1, str(person[0]) + '-' + person[1] + ' ' + person[2])
            count += 1
        # scroll bar

        self.scroll = Scrollbar(self.bottom, orient=VERTICAL)
        self.scroll.config(command=self.list_box.yview)
        self.list_box.config(yscrollcommand=self.scroll.set)
        self.scroll.grid(row=0, column=1, sticky=N + S)

        # Buttons
        self.btn_1 = Button(self.bottom, text='Add', width=12, font='Sans 12 bold', command=self.func_add)
        self.btn_1.grid(row=0, column=2, padx=10, pady=10, sticky=N)

        self.btn_2 = Button(self.bottom, text='Update', width=12, font='Sans 12 bold', command=self.func_update)
        self.btn_2.grid(row=0, column=2, padx=10, pady=50, sticky=N)

        self.btn_3 = Button(self.bottom, text='Display', width=12, font='Sans 12 bold', command=self.display_func)
        self.btn_3.grid(row=0, column=2, padx=10, pady=90, sticky=N)

        self.btn_4 = Button(self.bottom, text='Delete', width=12, font='Sans 12 bold', command=self.func_delete_person)
        self.btn_4.grid(row=0, column=2, padx=10, pady=130, sticky=N)

    def func_add(self):
        Addpeople.AddPeople()
        self.destroy()

    def func_update(self):
        global person_id
        selected_items = self.list_box.curselection()
        person = self.list_box.get(selected_items)
        person_id = person.split('-')[0]
        update_page = UpdatePage()

    def display_func(self):
        global person_id
        selected_items = self.list_box.curselection()
        person = self.list_box.get(selected_items)
        person_id = person.split('-')[0]
        display_page = Display()
        self.destroy()

    def func_delete_person(self):
        selected_items = self.list_box.curselection()
        person = self.list_box.get(selected_items)
        person_id = person.split('-')[0]
        msg = messagebox.askquestion('Warning', 'Are you sure to delete this person?', icon='warning')
        if msg:
            try:
                query = 'DELETE FROM persons WHERE person_id=?'
                cursor.execute(query, (person_id,))
                connection.commit()
                messagebox.showinfo('Success', 'Person has been successfully deleted!')
                self.destroy()

            except:
                messagebox.showinfo('Info', 'Person has not been deleted!')


class UpdatePage(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('750x550+320+100')
        self.title('Update People')
        self.resizable(False, False)

        # get data from database

        global person_id
        person = cursor.execute('SELECT * FROM persons WHERE person_id=?', (person_id,))
        person_info = person.fetchall()
        self.person_id = person_info[0][0]
        self.person_fname = person_info[0][1]
        self.person_lname = person_info[0][2]
        self.person_email = person_info[0][3]
        self.person_phone = person_info[0][4]
        self.person_address = person_info[0][5]
        # frame
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
        self.first_name_input.insert(0, self.person_fname)
        self.last_name_label = Label(self.bottom, text='Last Name:', bg='#fcc324', font='arial 15 bold', fg='white')
        self.last_name_input = Entry(self.bottom, width=35, bd=4)
        self.last_name_label.grid(row=1, column=0, pady=15, sticky=W)
        self.last_name_input.grid(row=1, column=1, pady=15)
        self.last_name_input.insert(0, self.person_lname)

        self.email_label = Label(self.bottom, text='Email:', bg='#fcc324', font='arial 15 bold', fg='white')
        self.email_input = Entry(self.bottom, width=35, bd=4)
        self.email_label.grid(row=2, column=0, pady=15, sticky=W)
        self.email_input.grid(row=2, column=1, pady=15)
        self.email_input.insert(0, self.person_email)

        self.phone_number_label = Label(self.bottom, text='Phone Number:', bg='#fcc324', font='arial 15 bold',
                                        fg='white')
        self.phone_number_input = Entry(self.bottom, width=35, bd=4)
        self.phone_number_label.grid(row=3, column=0, pady=15, sticky=W)
        self.phone_number_input.grid(row=3, column=1, pady=15)
        self.phone_number_input.insert(0, self.person_phone)

        self.address_label = Label(self.bottom, text='Address:', bg='#fcc324', font='arial 15 bold', fg='white')
        self.address_input = Text(self.bottom, width=35, height=4, wrap='word')
        self.address_label.grid(row=4, column=0, pady=15, sticky=W)
        self.address_input.grid(row=4, column=1, pady=15)
        self.address_input.insert('1.0', self.person_address)

        self.btn_add_people = Button(self.bottom, text='Update', command=self.update_database)
        self.btn_add_people.grid(row=5, column=1, padx=(50, 0), pady=15, sticky=E)

    def update_database(self):
        person_id = self.person_id
        person_fname = self.first_name_input.get()
        person_lname = self.last_name_input.get()
        person_email = self.email_input.get()
        person_phone = self.phone_number_input.get()
        person_address = self.address_input.get(1.0, END)

        try:
            query = 'UPDATE persons  SET person_fname=?, person_lname=?, person_email=?, person_number=?,' \
                    ' person_address=? WHERE person_id=?'
            cursor.execute(query, (person_fname, person_lname, person_email, person_phone, person_address, person_id))
            connection.commit()
            messagebox.showinfo('Success', 'Person has been Successfully Updated', icon='info')
            self.destroy()

        except:
            messagebox.showerror('Error', "Person has not been Updated", icon='warning')


class Display(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('750x550+320+100')
        self.title('Update People')
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
        self.first_name_input.config(state='disabled')

        self.last_name_label = Label(self.bottom, text='Last Name:', bg='#fcc324', font='arial 15 bold', fg='white')
        self.last_name_input = Entry(self.bottom, width=35, bd=4)
        self.last_name_label.grid(row=1, column=0, pady=15, sticky=W)
        self.last_name_input.grid(row=1, column=1, pady=15)
        self.last_name_input.config(state='disabled')

        self.email_label = Label(self.bottom, text='Email:', bg='#fcc324', font='arial 15 bold', fg='white')
        self.email_input = Entry(self.bottom, width=35, bd=4)
        self.email_label.grid(row=2, column=0, pady=15, sticky=W)
        self.email_input.grid(row=2, column=1, pady=15)
        self.email_input.config(state='disabled')

        self.phone_number_label = Label(self.bottom, text='Phone Number:', bg='#fcc324', font='arial 15 bold',
                                        fg='white')
        self.phone_number_input = Entry(self.bottom, width=35, bd=4)
        self.phone_number_label.grid(row=3, column=0, pady=15, sticky=W)
        self.phone_number_input.grid(row=3, column=1, pady=15)
        self.phone_number_input.config(state='disabled')

        self.address_label = Label(self.bottom, text='Address:', bg='#fcc324', font='arial 15 bold', fg='white')
        self.address_input = Text(self.bottom, width=35, height=4, wrap='word')
        self.address_label.grid(row=4, column=0, pady=15, sticky=W)
        self.address_input.grid(row=4, column=1, pady=15)
        self.address_input.config(state='disabled')
