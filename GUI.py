from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkintermapview import *
 
 #Init function

def init(window_name, width, height):
    root = Tk()
    root.title(window_name)
    root.geometry(str(width)+"x"+str(height))

    return root

#Command functions
def __retrieveOrigin(obj, func):
    val = obj.get()
    new_val = func(val)

def __retrieveModel(obj, func, var):
    val = obj.get()
    var.set(func(val))

#Generation functions

def createFrame(root):
    return Frame(root)

def __createComboBox(root, name, values):
    f = Frame(root)

    combo = ttk.Combobox(f, values = values)
    combo.set(name) 
    combo.pack(side=LEFT)

    button = Button(f, text="select")
    button.pack(side=LEFT)

    return f, combo, button

def createComboBoxOrigin(root, name, values, func):

    frame, combo, button = __createComboBox(root, name, values)

    button.configure(command=lambda: __retrieveOrigin(combo, func))

    return frame

def createComboBoxModel(root, name, values, func):

    combo, button = __createComboBox(root, name, values)

    var = IntVar()
    var.set(0)

    button.configure(command=lambda: __retrieveModel(combo, func, var))
    #createLabelCountPlanes(root, var)

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

def createMap(root):
    map_widget = TkinterMapView(root, width=800, height=600, corner_radius=0)
    return map_widget

def getFrameChild(frame, type):
    children_widgets = frame.winfo_children()
    for child_widget in children_widgets:
        print(child_widget.winfo_class())
        if child_widget.winfo_class() == type:
            return child_widget