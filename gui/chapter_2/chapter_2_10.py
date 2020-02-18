from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk

root = themed_tk.ThemedTk()
root.get_themes()
root.set_theme('radiance')

# theme names are  aquativo, arc, black, blue, clearlooks, elegance, itft1, kroc, radiance

def information():
    username = username_input.get()
    password = password_input.get()
    print('username:' + username + '\tpassword:', password)


title = ttk.Label(root, text='Select lesson', font=(('Verdana'), 25))
username_label = ttk.Label(root, text='Username')
username_input = ttk.Entry(root, width=30)
password_label = ttk.Label(root, text='Password')
password_input = ttk.Entry(root, width=30, show='*')
btn = ttk.Button(root, text='Enter', command=information)
btn_2 = ttk.Button(root, text='Click')

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
