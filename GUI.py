from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
 
 #Init function

def init(window_name):
    root = Tk()
    root.title(window_name)
    root.geometry("800x400")

    return root

#Command functions
def __retrieveManufacturer(obj, func):
    val = obj.get()
    new_val = func(val)

def __retrieveModel(obj, func, var):
    val = obj.get()
    var.set(func(val))

#Generation functions

def __createComboBox(root, name, values):
    f = Frame(root)
    f.pack()

    combo = ttk.Combobox(f, values = values)
    combo.set(name) 
    combo.pack(side=LEFT)

    button = Button(f, text="select")
    button.pack(side=LEFT)

    return combo, button

def createComboBoxManufacturer(root, name, values, func):

    combo, button = __createComboBox(root, name, values)

    button.configure(command=lambda: __retrieveManufacturer(combo, func))

def createComboBoxModel(root, name, values, func):

    combo, button = __createComboBox(root, name, values)

    var = IntVar()
    var.set(0)

    button.configure(command=lambda: __retrieveModel(combo, func, var))
    createLabelCountPlanes(root, var)

    return combo

def createLabelCountPlanes(root, var):

    label = Label(root, textvariable= var)
    label.pack()

def createPlotUI(root, data):
    figure = plt.Figure(figsize=(6,5), dpi=100)
    ax1 = figure.add_subplot()
    plot = FigureCanvasTkAgg(figure, root)
    plot.get_tk_widget().pack(fill=BOTH)
    data.plot(kind='bar', ax=ax1, legend=True)
    ax1.set_xticklabels(data['model'], rotation=45)