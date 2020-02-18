from tkinter import *
from tkinter import ttk

root = Tk()
progressbar = ttk.Progressbar(root, length=200, orient=HORIZONTAL, mode='indeterminate')
progressbar.pack(pady=20)
progressbar.start()
progressbar.stop()
progressbar.config(mode='determinate', value=20.0, maximum=80.0)
progressbar.start()
progressbar.stop()
value = DoubleVar()
progressbar.config(variable=value)

scale = ttk.Scale(root, length=200, orient=HORIZONTAL, var=value, from_=0.0, to=80.0)
scale.pack()

root.geometry('500x450')
root.mainloop()
