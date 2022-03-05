
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import colorchooser
from tkinter import scrolledtext
from tkinter import Menu


class GUI:
    def __init__(self, master):
        self.master = master

        self.master.title("GUI")
        self.master.geometry("500x500")
        self.master.resizable(False, False)
        self.master.configure(background="white")
        
        

    

root = Tk()
my_gui = GUI(root)
root.mainloop()