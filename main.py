from pyexpat import model
import pandas as pd
import GUI
import backend

def updatePlaneModelsList(val):
    models = backend.getColumnElement(backend.filterElements(planes_df, planes_df.manufacturer, val), "model")
    combo_model['values']=sorted(models)

def countModel(val):
    return backend.filterElements(planes_df, planes_df.model, val).count()

def main():
    root = GUI.init("Flights Tracker")
    global planes_df, combo_model
    
    airports_df = backend.loadFile("./Datasets/airports.csv")
    flights_small_df = backend.loadFile("./Datasets/flights_small.csv")
    planes_df = backend.loadFile("./Datasets/planes.csv")

    manufacturers = backend.getColumnElement(planes_df, "manufacturer")
    GUI.createComboBoxManufacturer(root, "Plane manufacturers", manufacturers, updatePlaneModelsList)

    models = backend.getColumnElement(planes_df, "model")
    combo_model = GUI.createComboBoxModel(root, "Plane models", sorted(models), countModel)

    df = planes_df.filter(planes_df.manufacturer=="AIRBUS")
    data = backend.getCountedElements(df, 'model', 'engine').toPandas()

    GUI.createPlotUI(root, data)

    root.mainloop()

if __name__ == "__main__":
    main()
