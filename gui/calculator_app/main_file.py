from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Calculator App')
root.geometry('380x550+450+100')
root.resizable(False, False)

entry_box = Entry(root, font='verdana 14 bold', bd=10, justify=RIGHT, bg='#e6e6fa')
entry_box.insert(0, 'o')
entry_box.place(x=20, y=10)

btn_numbers = []


def enter_number(x):
    if entry_box.get() == 'o':
        entry_box.delete(0, 'end')
        entry_box.insert(0, str(x))
    else:
        length = len(entry_box.get())
        entry_box.insert(length, str(x))


# numbers
for i in range(10):
    btn_numbers.append(Button(root, font='times 15 bold', bd=5, text=str(i), command=lambda x=i: enter_number(x)))

btn_text_number = 1
for i in range(0, 3):
    for j in range(0, 3):
        btn_numbers[btn_text_number].place(x=25 + j * 90, y=70 + i * 70)
        btn_text_number += 1


# operations
def enter_operator(x):
    if entry_box.get() != 'o':
        length = len(entry_box.get())
        entry_box.insert(length, operations[x]['text'])


operations = []
for i in range(4):
    operations.append(Button(root, width=2, font='times 15 bold', bd=5, command=lambda x=i: enter_operator(x)))

operations[0]['text'] = '+'
operations[1]['text'] = '-'
operations[2]['text'] = '*'
operations[3]['text'] = '/'

for i in range(4):
    operations[i].place(x=290, y=70 + i * 70)


# other buttons
def clear():
    entry_box.delete(0, END)
    entry_box.insert(0, 'o')


result_list = []


def equal():
    content = entry_box.get()
    result = eval(content)
    entry_box.delete(0, END)
    entry_box.insert(0, str(result))
    result_list.append(content)
    result_list.reverse()
    status_bar.configure(text='History: ' + '| '.join(result_list[:2]),  font=('verdana 12 bold'))


def delete():
    length = len(entry_box.get())
    entry_box.delete(length - 1, 'end')
    if length == 1:
        entry_box.insert(0, 'o')


btn_zero = Button(root, text='0', width=19, font='times 15 bold', bd=5, command=lambda x=0: enter_number(x))
btn_clean = Button(root, text='C', width=4, font='times 15 bold', bd=5, command=clear)
btn_dot = Button(root, text='.', width=4, font='times 15 bold', bd=5, command=lambda x='.': enter_number(x))
btn_equal = Button(root, text='=', width=4, font='times 15 bold', bd=5, command=equal)
delete_icon = PhotoImage(file='./arrow.png')
delete_btn = Button(root, image=delete_icon, bd=5, command=delete)

btn_zero.place(x=25, y=280)
btn_clean.place(x=25, y=340)
btn_dot.place(x=110, y=340)
btn_equal.place(x=200, y=340)
delete_btn.place(x=300, y=340)
# status bar
status_bar = Label(root, text='History', height=5, relief=SUNKEN, justify=RIGHT, font=('verdana 12 bold'), anchor=W, )
status_bar.pack(fill=X, side=BOTTOM)
root.mainloop()
