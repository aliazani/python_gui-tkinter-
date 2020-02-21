from tkinter import *
from tkinter import font, colorchooser, ttk, messagebox, filedialog
import sqlite3

show_status_bar = True
show_tool_bar = True

font_name = 'system'
font_size = 12
url_var = ''


class TextEditor(Text):
    def __init__(self, parent, *args, **kwargs):
        Text.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.config(wrap='word', relief=FLAT)
        self.pack(fill=BOTH, expand=True)
        self.horizontal_scroll_bar = Scrollbar(self, orient=HORIZONTAL)
        self.horizontal_scroll_bar.pack(side=BOTTOM, fill=X)
        self.vertical_scroll_bar = Scrollbar(self, orient=VERTICAL)
        self.vertical_scroll_bar.pack(side=RIGHT, fill=Y)
        self.horizontal_scroll_bar.config(command=self.xview)
        self.vertical_scroll_bar.config(command=self.yview)
        self.config(xscrollcommand=self.horizontal_scroll_bar.set)
        self.config(yscrollcommand=self.vertical_scroll_bar.set)


class StatusBar(Label):
    def __init__(self, parent, *args, **kwargs):
        Label.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.config(text='Status Bar')
        self.pack(side=BOTTOM)


class ToolBar(Label):
    def __init__(self, parent, *args, **kwargs):
        Label.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pack(side=TOP, fill=X)

        # Combo Boxes
        self.font_combo_box = ttk.Combobox(self)
        self.font_size_combo_box = ttk.Combobox(self)

        self.font_combo_box.pack(side=LEFT, padx=(5, 10))
        self.font_size_combo_box.pack(side=LEFT)

        # Bold
        self.bold_icon = PhotoImage(file='icons/bold.png')
        self.bold_btn = Button(self, image=self.bold_icon, command=self.parent.bold_function)

        self.bold_btn.pack(side=LEFT, padx=(10, 5))

        # Italic
        self.italic_icon = PhotoImage(file='icons/italic.png')
        self.italic_btn = Button(self, image=self.italic_icon, command=self.parent.italic_function)

        self.italic_btn.pack(side=LEFT, padx=(10, 5))

        # Underline
        self.underline_icon = PhotoImage(file='icons/under_line.png')
        self.underline_btn = Button(self, image=self.underline_icon, command=self.parent.underline_function)

        self.underline_btn.pack(side=LEFT, padx=(10, 5))

        # Color
        self.color_icon = PhotoImage(file='icons/color.png')
        self.color_btn = Button(self, image=self.color_icon, command=self.parent.change_color_function)

        self.color_btn.pack(side=LEFT, padx=(10, 5))

        # Align Right
        self.align_right_icon = PhotoImage(file='icons/alignright.png')
        self.align_right_btn = Button(self, image=self.align_right_icon, command=self.parent.align_right_function)

        self.align_right_btn.pack(side=LEFT, padx=(10, 5))

        # Align Center
        self.align_center_icon = PhotoImage(file='icons/aligncenter.png')
        self.align_center_btn = Button(self, image=self.align_center_icon, command=self.parent.align_center_function)

        self.align_center_btn.pack(side=LEFT, padx=(10, 5))

        # Align Left
        self.align_left_icon = PhotoImage(file='icons/alignleft.png')
        self.align_left_btn = Button(self, image=self.align_left_icon, command=self.parent.align_left_function)

        self.align_left_btn.pack(side=LEFT, padx=(10, 5))

        # Fonts
        all_fonts = list(font.families())
        self.font_variable = StringVar()
        self.font_combo_box.config(values=all_fonts, textvariable=self.font_variable)
        self.font_combo_box.current(0)

        # Font Sizes
        font_sizes_list = []
        for number in range(1, 101):
            font_sizes_list.append(number)

        self.font_size_combo_box.config(values=font_sizes_list)
        self.font_size_combo_box.current(11)

        # Bind methods
        self.font_combo_box.bind('<<ComboboxSelected>>', self.parent.get_font)
        self.font_size_combo_box.bind('<<ComboboxSelected>>', self.parent.get_font_size)


class MainMenu(Menu):
    def __init__(self, parent, *args, **kwargs):
        Menu.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        # File
        self.new_icon = PhotoImage(file='icons/new.png')
        self.open_icon = PhotoImage(file='icons/open.png')
        self.save_icon = PhotoImage(file='icons/save_icon.png')
        self.exit_icon = PhotoImage(file='icons/exit.png')
        self.file = Menu(self, tearoff=0)
        self.file.add_command(label='New', image=self.new_icon, compound=LEFT, accelerator='Ctrl+N',
                              command=self.parent.new_file)
        self.file.add_command(label='Open', image=self.open_icon, compound=LEFT, accelerator='Ctrl+O',
                              command=self.parent.open_file)
        self.file.add_command(label='Save', image=self.save_icon, compound=LEFT, accelerator='Ctrl+S',
                              command=self.parent.save_file)
        self.file.add_command(label='Save As', image=self.save_icon, compound=LEFT, accelerator='Ctrl+Alt+S',
                              command=self.parent.save_as_file)
        self.file.add_command(label='Exit', image=self.exit_icon, compound=LEFT, command=self.parent.exit_func)

        self.add_cascade(label='File', menu=self.file)

        # Edit
        self.edit = Menu(self, tearoff=0)
        self.edit.add_command(label='Copy', accelerator='Ctrl+C')
        self.edit.add_command(label='Cut', accelerator='Ctrl+X')
        self.edit.add_command(label='Paste', accelerator='Ctrl+P')
        self.edit.add_command(label='Clear All', accelerator='Ctrl+Alt+C')
        self.edit.add_command(label='Find', accelerator='Ctrl+F')

        self.add_cascade(label='Edit', menu=self.edit)

        # View
        global show_status_bar
        global show_tool_bar
        self.view = Menu(self, tearoff=0)
        self.view.add_checkbutton(onvalue=True, offvalue=False, var=show_tool_bar, label='Tool Bar')
        self.view.add_checkbutton(onvalue=True, offvalue=False, var=show_status_bar, label='Status Bar')

        self.add_cascade(label='View', menu=self.view)

        # Templates

        self.templates = Menu(self, tearoff=0)
        self.color_choice = StringVar()
        self.color_dic = {
            'Default': '#000000.#FFFFFF',  # first one is the font color and second one is the background color
            'Tomato': '#ffff00.#ff6347',
            'LimeGreen': '#fffff0.#32cd32',
            'Magenta': '#fffafa.#ff00ff',
            'RoyalBlue': '#ffffbb.#4169e1',
            'MediumBlue': '#d1e7e0.#0000cd',
            'Dracula': '#ffffff.#000000'
        }
        for color in sorted(self.color_dic):
            self.templates.add_radiobutton(label=color, var=self.color_choice)
        self.add_cascade(label='Templates', menu=self.templates)

        # About

        self.about = Menu(self, tearoff=0)
        self.about.add_command()

        self.add_cascade(label='About', menu=self.about)


class MainApplication(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pack(fill=BOTH, expand=True)

        # Widgets
        self.main_menu = MainMenu(self)

        # Tool Bar
        self.tool_bar = ToolBar(self)

        # Text Editor
        self.text_editor = TextEditor(self)
        self.text_editor.focus()

        # Menu configuration
        self.parent.config(menu=self.main_menu)

        # Status Bar
        self.status_bar = StatusBar(self)

    # Tool bar functions
    def get_font(self, *args, **kwargs):
        global font_name
        font_name = self.tool_bar.font_combo_box.get()
        self.text_editor.configure(font=(font_name, font_size))

    def get_font_size(self, *args, **kwargs):
        global font_size
        font_size = self.tool_bar.font_size_combo_box.get()
        self.text_editor.configure(font=(font_name, font_size))

    def bold_function(self, *args):
        text_property = font.Font(font=self.text_editor['font'])

        if text_property.actual('weight') == 'normal':
            self.text_editor.configure(font=(font_name, font_size, 'bold'))
        elif text_property.actual('weight') == 'bold':
            self.text_editor.configure(font=(font_name, font_size, 'normal'))

    def italic_function(self, *args):
        text_property = font.Font(font=self.text_editor['font'])

        if text_property.actual('slant') == 'roman':
            self.text_editor.configure(font=(font_name, font_size, 'italic'))
        elif text_property.actual('slant') == 'italic':
            self.text_editor.configure(font=(font_name, font_size, 'roman'))

    def underline_function(self, *args):
        text_property = font.Font(font=self.text_editor['font'])

        if text_property.actual('underline') == 0:
            self.text_editor.configure(font=(font_name, font_size, 'underline'))
        elif text_property.actual('underline') == 1:
            self.text_editor.configure(font=(font_name, font_size, 'normal'))

    def change_color_function(self, *args):
        color = colorchooser.askcolor()
        self.text_editor.configure(fg=color[1])

    def align_right_function(self, *args):
        content = self.text_editor.get(1.0, END)
        self.text_editor.tag_config('right', justify=RIGHT)
        self.text_editor.delete(1.0, END)
        self.text_editor.insert(INSERT, content, 'right')

    def align_center_function(self, *args):
        content = self.text_editor.get(1.0, END)
        self.text_editor.tag_config('center', justify=CENTER)
        self.text_editor.delete(1.0, END)
        self.text_editor.insert(INSERT, content, 'center')

    def align_left_function(self, *args):
        content = self.text_editor.get(1.0, END)
        self.text_editor.tag_config('left', justify=LEFT)
        self.text_editor.delete(1.0, END)
        self.text_editor.insert(INSERT, content, 'left')

    def new_file(self, *args):
        global url_var
        self.text_editor.delete(1.0, END)

    def open_file(self, *args):
        global url_var

        url_var = filedialog.askopenfilename(initialdir='./', title='select file',
                                             filetypes=(('Text Files', '*.txt'), ('All Files', '*.*')))
        try:
            with open(url_var, 'r') as read_file:
                content_of_file = read_file.read()
                self.text_editor.delete(1.0, END)
                self.text_editor.insert(INSERT, content_of_file)
        except:
            return

        self.parent.title('Editing ' + str(url_var.split('/')[-1]))

    def save_file(self, *args):
        global url_var
        try:
            if url_var != '':
                content = str(self.text_editor.get(1.0, END))
                with open(url_var, 'w', encoding='utf-8') as writable_file:
                    writable_file.write(content)

            else:
                url_var = filedialog.asksaveasfile(initialdir='./', title='Save file', mode='w',
                                                   defaultextension='.txt',
                                                   filetypes=(('Text Files', '*.txt'), ('All Files', '*.*')))

                content_2 = str(self.text_editor.get(1.0, END))
                url_var.write(content_2)
                url_var.close()
        except:
            return

    def save_as_file(self, *args):
        global url_var
        try:
            url_var = filedialog.asksaveasfile(initialdir='./', title='Save file', mode='w',
                                               defaultextension='.txt',
                                               filetypes=(('Text Files', '*.txt'), ('All Files', '*.*')))

            content_2 = str(self.text_editor.get(1.0, END))
            url_var.write(content_2)
            url_var.close()
            self.parent.title('Editing ' + str(url_var.split('/')[-1]))
        except:
            return

    def exit_func(self, *args):
        pass


if __name__ == '__main__':
    root = Tk()
    root.title('Text editor')
    MainApplication(root).pack(side=TOP, fill=BOTH, expand=True)
    root.iconbitmap('icons/icon.ico')
    root.geometry('1250x750+100+20')
    root.mainloop()
