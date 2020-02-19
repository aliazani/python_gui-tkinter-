from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

connection = sqlite3.connect('library.db')
cursor = connection.cursor()


class GiveBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('750x600+450+100')
        self.resizable(False, False)
        self.title('Lend Book')
        query = "SELECT * FROM all_books WHERE status = 0"
        all_books = cursor.execute(query).fetchall()
        self.book_list = []
        for book in all_books:
            self.book_list.append(str(book[0]) + '-' + book[2])
        second_query = "SELECT * FROM members"
        all_members = cursor.execute(second_query).fetchall()
        self.member_list = []
        for member in all_members:
            self.member_list.append(str(member[0]) + '-' + member[1])

        # frames and widgets
        self.top_frame = Frame(self, bg='white', height=120)
        self.top_frame.pack(fill=X)
        self.bottom_frame = Frame(self, bg='#fcc324', height=480)
        self.bottom_frame.pack(fill=X)
        self.add_person_icon = PhotoImage(file='icons/addperson.png')
        self.add_person_label = Label(self.top_frame, image=self.add_person_icon, bg='white')
        self.add_person_label.place(x=120, y=10)
        self.header = Label(self.top_frame, text='Lend Book', font='arial 16 bold', fg='#003f8a', bg='white')
        self.header.place(x=290, y=60)

        # book name
        self.book_name = StringVar()
        self.book_name_label = Label(self.bottom_frame, text='Book Name:', font='arial 14 bold', fg='white'
                                     , bg='#fcc324')
        self.book_name_label.place(x=40, y=40)

        self.combo_book_name = ttk.Combobox(self.bottom_frame, textvariable=self.book_name)
        self.combo_book_name['values'] = self.book_list
        self.combo_book_name.place(x=180, y=45)
        # Member name
        self.member_name = StringVar()
        self.member_name_label = Label(self.bottom_frame, text='Member Name:', font='arial 14 bold', fg='white',
                                       bg='#fcc324')
        self.member_name_label.place(x=40, y=100)

        self.combo_member_name = ttk.Combobox(self.bottom_frame, textvariable=self.member_name)
        self.combo_member_name['values'] = self.member_list

        self.combo_member_name.place(x=180, y=105)

        self.btn_add_person = Button(self.bottom_frame, text='Lend', command=self.lend_book)
        self.btn_add_person.place(x=420, y=150)

    def lend_book(self):
        book_name = self.book_name.get()
        member_name = self.member_name.get()
        self.book_id = book_name.split('-')[0]
        if (book_name and member_name) != '':
            try:
                query = "INSERT INTO 'borrowed_books' (borrowed_book_id, borrower_person_id) VALUES (?, ?)"
                cursor.execute(query, (book_name, member_name))
                connection.commit()
                messagebox.showinfo('Success', 'Book successfully gave to member', icon='info')
                cursor.execute("UPDATE all_books SET status = ? WHERE book_id = ?", (1, self.book_id))
                connection.commit()
            except:
                messagebox.showerror('Fail', 'Book Could not give to member', icon='warning')
        else:
            messagebox.showerror('Fail', 'Fields can not be empty', icon='warning')

