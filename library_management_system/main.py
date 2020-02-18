from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import add_books_file
import add_member_file

connection = sqlite3.connect('library.db')
cursor = connection.cursor()


class Main:
    def __init__(self, root):
        self.root = root

        # List of details of books

        # List of books insert
        def display_books():
            books = cursor.execute("SELECT * FROM 'all_books'").fetchall()
            count = 0
            for book in books:
                self.list_of_books.insert(count, str(book[0]) + '-' + book[2])
                count += 1

            def book_info(event):
                value = str(self.list_of_books.get(self.list_of_books.curselection()))
                book_id = value.split('-')[0]
                select_book = cursor.execute("SELECT * FROM 'all_books' WHERE book_id = ?", (book_id,))
                book_information = select_book.fetchall()
                self.list_of_details.delete(0, END)
                self.list_of_details.insert(0, 'Book Name: ' + book_information[0][2])
                self.list_of_details.insert(1, 'Author Name: ' + book_information[0][1])
                self.list_of_details.insert(2, 'Language: ' + book_information[0][3])
                self.list_of_details.insert(3, 'Page Number: ' + book_information[0][4])
                if book_information[0][5] == 0:
                    self.list_of_details.insert(4, 'Status: Available')
                else:
                    self.list_of_details.insert(4, 'Status: Not Available')

            self.list_of_books.bind('<<ListboxSelect>>', func=book_info)

        # Main frame
        main_frame = Frame(self.root)
        main_frame.pack()

        # Top frame
        top_frame = Frame(main_frame, width=1260, height=100, relief=SUNKEN, padx=20, bg='#f8f8f8', borderwidth=2)
        top_frame.pack(side=TOP, fill=X)

        # Center frame
        center_frame = Frame(main_frame, width=1260, height=550, relief=RIDGE, bg='#e0f0f0')
        center_frame.pack(side=TOP, fill=X)

        # Center left frame
        center_left_frame = Frame(center_frame, width=900, height=550, bg='#e0f0f0', borderwidth=2, relief=SUNKEN)
        center_left_frame.pack(side=LEFT)

        # Center right frame
        center_right_frame = Frame(center_frame, width=460, height=550, bg='#e0f0f0', borderwidth=2, relief=SUNKEN)
        center_right_frame.pack()

        # Search bar
        search_bar = LabelFrame(center_right_frame, width=460, height=65, text='Search Bar', bg='#9bc9ff')
        search_bar.pack(fill=BOTH)
        self.label_search = Label(search_bar, text='Search', font='arial 12 bold', bg='#9bc9ff', fg='white')
        self.label_search.grid(row=0, column=0, padx=20, pady=10)
        self.entry_search = Entry(search_bar, width=30, bd=6)
        self.entry_search.grid(row=0, column=1, padx=2, pady=10)
        self.search_btn = Button(search_bar, text='Enter', font='arial 12 bold', bg='#fcc324', fg='white',
                                 command=self.search_book)
        self.search_btn.grid(row=0, column=2, pady=10, padx=10)

        # List bar
        list_bar = LabelFrame(center_right_frame, width=460, height=165, text='Search Bar', bg='#fcc324')
        list_bar.pack(fill=BOTH)
        self.label_list = Label(list_bar, text='Sort By', font='times 16 bold', bg='#fcc324', fg='#2488ff')
        self.label_list.grid(row=0, column=1, columnspan=2, pady=10)
        self.btn_choice = IntVar()
        radio_btn_1 = Radiobutton(list_bar, text='All Books', var=self.btn_choice, value=1, bg='#fcc324')
        radio_btn_2 = Radiobutton(list_bar, text='In Library', var=self.btn_choice, value=2, bg='#fcc324')
        radio_btn_3 = Radiobutton(list_bar, text='Borrowed Books', var=self.btn_choice, value=3, bg='#fcc324')
        radio_btn_1.grid(row=1, column=0, padx=2)
        radio_btn_2.grid(row=1, column=1)
        radio_btn_3.grid(row=1, column=2)
        list_btn = Button(list_bar, text='List Books', bg='#2488ff', fg='white')
        list_btn.grid(row=1, column=3, padx=15)

        # Image bar
        image_bar = Frame(center_right_frame, width=460, height=300)
        image_bar.pack(fill=BOTH)
        self.title_label_right = Label(image_bar, text='Welcome to our library', font='arial 16 bold')
        self.title_label_right.grid(row=0)
        self.library_icon = PhotoImage(file='./icons/library.png')
        self.library_photo_label = Label(image_bar, image=self.library_icon)
        self.library_photo_label.grid(row=1)

        # Add book button
        self.add_book_icon = PhotoImage(file='./icons/add_book.png')
        self.add_book_button = Button(top_frame, text='Add Book', image=self.add_book_icon, compound=LEFT,
                                      font='arial 12 bold', command=self.add_books)
        self.add_book_button.pack(side=LEFT)

        # Add member button
        self.add_member_icon = PhotoImage(file='./icons/users.png')
        self.add_member_button = Button(top_frame, text='Add Member', image=self.add_member_icon, compound=LEFT,
                                        font='arial 12 bold', command=self.add_member)
        self.add_member_button.pack(side=LEFT)

        # Give book button
        self.give_book_icon = PhotoImage(file='./icons/givebook.png')
        self.give_book_button = Button(top_frame, text='Give Book', image=self.give_book_icon, compound=LEFT,
                                       font='arial 12 bold')
        self.give_book_button.pack(side=LEFT)

        # Tabs
        self.tabs = ttk.Notebook(center_left_frame, width=900, height=550)
        self.tabs.pack()
        self.tab1_icon = PhotoImage(file='icons/books.png')
        self.tab2_icon = PhotoImage(file='icons/members.png')
        self.tab1 = ttk.Frame(self.tabs)
        self.tab2 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab1, text='Library Management', image=self.tab1_icon, compound=LEFT)
        self.tabs.add(self.tab2, text='Statistics', image=self.tab2_icon, compound=LEFT)

        # Tab 1

        # List of books
        self.list_of_books = Listbox(self.tab1, width=35, height=25, bd=4, font='arial 12 bold')
        self.scroll_bar = Scrollbar(self.tab1, orient=VERTICAL)
        self.list_of_books.grid(row=0, column=0, padx=(10, 0), pady=10, sticky=N)
        self.scroll_bar.config(command=self.list_of_books.yview)
        self.list_of_books.config(yscrollcommand=self.scroll_bar.set)
        self.scroll_bar.grid(row=0, column=0, sticky=N + E + S)

        # List details
        self.list_of_details = Listbox(self.tab1, width=60, height=25, bd=4, font='arial 12 bold')
        self.list_of_details.grid(row=0, column=1, padx=(10, 0), pady=10, sticky=N)

        # Tab 2

        # Statistics
        self.count_of_books_label = Label(self.tab2, text='', pady=15, font='arial 14 bold')
        self.count_of_books_label.grid(row=0, sticky=W)
        self.count_of_members_label = Label(self.tab2, text='', pady=15, font='arial 14 bold')
        self.count_of_members_label.grid(row=1, sticky=W)
        self.count_of_taken_books_label = Label(self.tab2, text='', pady=15, font='arial 14 bold')
        self.count_of_taken_books_label.grid(row=2, sticky=W)

        # Functions
        display_books()

    # Buttons functions
    def add_books(self):
        add_books_file.AddBooks()

    def add_member(self):
        add_member_file.AddMember()

    def search_book(self):
        value = self.entry_search.get()
        search = cursor.execute("SELECT * FROM 'all_books' WHERE book_name LIKE ?", ('%' + value + '%',)).fetchall()
        self.list_of_books.delete(0, END)
        count = 0
        for book in search:
            self.list_of_books.insert(count, str(book[0]) + '-' + book[2])
            count += 1


def main():
    root = Tk()
    app = Main(root)
    root.title("Library Management System")
    root.geometry("1260x650")
    # root.iconbitmap('icon.ico ')
    root.mainloop()


if __name__ == '__main__':
    main()
