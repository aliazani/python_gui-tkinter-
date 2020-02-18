from tkinter import *
from tkinter import messagebox
import sqlite3

connection = sqlite3.connect('library.db')
cursor = connection.cursor()


class AddBooks(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('750x600+450+100')
        self.resizable(False, False)
        self.title('Add Book')

        # Frames
        self.top_frame = Frame(self, bg='white', height=120)
        self.top_frame.pack(fill=X)
        self.bottom_frame = Frame(self, bg='#fcc324', height=480)
        self.bottom_frame.pack(fill=X)

        # Widgets
        self.add_book_icon = PhotoImage(file='icons/add_book.png')
        self.add_book_label = Label(self.top_frame, image=self.add_book_icon, bg='white')
        self.add_book_label.place(x=120, y=10)
        self.header = Label(self.top_frame, text='Add books', font='arial 16 bold', fg='#003f8a', bg='white')
        self.header.place(x=290, y=60)

        self.name_label = Label(self.bottom_frame, text='Book Name:', font='arial 14 bold', fg='white', bg='#fcc324')
        self.name_entry = Entry(self.bottom_frame, width=35, bd=3)
        self.name_label.place(x=40, y=40)
        self.name_entry.place(x=180, y=40)

        self.author_label = Label(self.bottom_frame, text='Author:', font='arial 14 bold', fg='white', bg='#fcc324')
        self.author_entry = Entry(self.bottom_frame, width=35, bd=3)
        self.author_label.place(x=40, y=100)
        self.author_entry.place(x=180, y=100)

        self.language_label = Label(self.bottom_frame, text='language:', font='arial 14 bold', fg='white', bg='#fcc324')
        self.language_entry = Entry(self.bottom_frame, width=35, bd=3)
        self.language_label.place(x=40, y=160)
        self.language_entry.place(x=180, y=160)

        self.page_label = Label(self.bottom_frame, text='Page Number:', font='arial 14 bold', fg='white', bg='#fcc324')
        self.page_entry = Entry(self.bottom_frame, width=35, bd=3)
        self.page_label.place(x=40, y=220)
        self.page_entry.place(x=180, y=220)

        self.btn_add_book = Button(self.bottom_frame, text='Add', command=self.add_book_function)
        self.btn_add_book.place(x=420, y=270)

    def add_book_function(self):
        name = self.name_entry.get()
        page = self.page_entry.get()
        language = self.language_entry.get()
        author = self.author_entry.get()
        if (name and page and author and language) != '':
            try:
                query = "INSERT INTO 'all_books' (book_name, book_author, book_language, book_page) VALUES (?, ?, ?, ?)"
                cursor.execute(query, (name, author, language, page))
                connection.commit()
                messagebox.showinfo('Success', 'Successfully added to database', icon='info')
            except:
                messagebox.showerror('Failed', 'Failed to add to database', icon='warning')
        else:
            messagebox.showerror('Failed', 'Fields can not be empty', icon='warning')
