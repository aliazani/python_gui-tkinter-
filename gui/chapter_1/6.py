from tkinter import *
from tkinter import ttk

root = Tk()


def back():
    username = entry_1.get()
    password = entry_2.get()
    print(username)
    print(password)
    if checkbox_value.get() == 1:
        print('Remember me selected.')
    else:
        print('NOT')

    print(radio_button_value.get())
    print(options.get())
    print(year.get())


title = Label(text='Select Lesson')
lbl_name = Label(text='Name:')
lbl_pass = Label(text='password:')
entry_1 = Entry(width=40)
entry_2 = Entry(width=40, show='*')
btn = Button(text='Enter', command=back)

checkbox_value = IntVar()
checkbox_value.set(0)
check_box = Checkbutton(root, text='Remember me', variable=checkbox_value)

radio_button_value = StringVar()
gender_m = ttk.Radiobutton(text='Male', value='Male', var=radio_button_value)
gender_f = ttk.Radiobutton(text='Female', value='Female', var=radio_button_value)

options = StringVar()
combo_box = ttk.Combobox(textvariable=options, state='readonly',
                         values=('Change password', 'Check the site state', 'Selected Lesson'))

year = StringVar()
spin_box = Spinbox(state='readonly', from_=1980, to=2020, textvariable=year)

title.grid(row=0, column=0, columnspan=2)
lbl_name.grid(row=1, column=0, sticky=W, pady=5)
lbl_pass.grid(row=2, column=0, sticky=W, pady=5)
entry_1.grid(row=1, column=1, pady=5)
entry_2.grid(row=2, column=1, pady=5)
btn.grid(row=3, column=1, sticky=E, pady=5)
check_box.grid(row=3, column=0, sticky=W)
gender_m.grid(row=4, column=0)
gender_f.grid(row=4, column=1)
combo_box.grid(row=5, column=1)
spin_box.grid(row=5, column=0)
root.geometry('600x500')
root.mainloop()
