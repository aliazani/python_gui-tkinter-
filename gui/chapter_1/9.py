from tkinter import *

root = Tk()


def information():
    username = username_input.get()
    password = password_input.get()
    print('username:' + username + '\tpassword:', password)


title = Label(root, text='Select lesson', font=(('Verdana'), 25))
username_label = Label(root, text='Username')
username_input = Entry(root, width=30)
password_label = Label(root, text='Password')
password_input = Entry(root, width=30, show='*')
btn = Button(root, text='Enter', command=information)
btn_2 = Button(root, text='Click', bg='red', fg='yellow')

title.place(x=100, y=20)
username_label.place(x=20, y=80)
username_input.place(x=100, y=80)
password_label.place(x=20, y=120)
password_input.place(x=100, y=120)
btn.place(x=284, y=160)
btn_2.place(relx=0.3, rely=0.36)
# , anchor='center'

root.geometry('450x450+650+650')
root.mainloop()
