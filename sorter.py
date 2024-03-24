import tkinter as tk
from tkinter import ttk


class App():
    def __init__(self):
        self.root = tk.Tk()
        #size of window
        self.root.geometry("500x500")
        #title
        self.root.title('File Sorter')
        #window properties included inside a mainframe called "self.mainframe"
        self.mainframe = tk.Frame(self.root, background = 'white')

        self.mainframe.pack(fill = 'both', expand =True)

        self.text= ttk.Label(self.mainframe, text = "Hello", background = 'white', foreground ='green', font = ('Brass Mono', 30))

        self.set_text_field = ttk.Entry(self.mainframe)
        self.set_text_field.grid(row =1, column = 0, pady =10, sticky = 'NWES')
        set_text_button = ttk.Button(self.mainframe, text = 'Set Text', command = self.set_text)
        set_text_button.grid(row =1, column =1,pady =10)
        self.text.grid(column = 0, row = 0)
        color_options = ['red', 'green', 'blue', 'black']
        self.set_color_field = ttk.Combobox(self.mainframe, values = color_options)
        self.set_color_field.grid(row=2, column = 0, sticky = 'NWES', pady=10)
        set_color_button = ttk.Button(self.mainframe, text = 'Set Color', command = self.set_color)
        set_color_button.grid(row =2, column =1,pady =10)

        self.reverse_text = ttk.Button(self.mainframe)
        #so it doesnt just close immedieatly
        self.root.mainloop()
        return

    def set_text(self):
        newtext = self.set_text_field.get()
        self.text.config(text = newtext)

    def set_color(self):
        newcolor = self.set_color_field.get()
        self.text.config(foreground=newcolor)
if __name__ == "__main__":
    App()