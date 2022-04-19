from tkinter import *
from tkinter import ttk

def init(window_name):
    root = Tk()
    root.title(window_name)
    root.geometry("200x200")

    return root

def createComboBox(root, name, values):
    Combo = ttk.Combobox(root, values = values)
    Combo.set(name) 
    Combo.pack()