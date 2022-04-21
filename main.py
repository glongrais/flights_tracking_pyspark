from pyexpat import model
import pandas as pd
import GUI
import backend

def updatePlaneModelsList(val):
    models = backend.getColumnElement(backend.filterElements(planes_df, planes_df.manufacturer, val), "model")
    combo_model['values']=sorted(models)

def updateDestAirportsList(val):
    dest = backend.getColumnElement(backend.filterElements(flights_small_df, flights_small_df.origin, val), "dest")
    backend.getFaaFromName(airports_df, "Jekyll Island Airport")
    combo_dest['values']=sorted(dest)

def countModel(val):
    return backend.filterElements(planes_df, planes_df.model, val).count()

def main():

    global flights_small_df, airports_df, combo_dest, map

    root = GUI.init("Flights Tracker",800,650)

    airports_df = backend.loadFile("./Datasets/airports.csv")
    flights_small_df = backend.loadFile("./Datasets/flights_small.csv")
    #planes_df = backend.loadFile("./Datasets/planes.csv")

    origin_airports = backend.getColumnElement(flights_small_df, "origin")

    combos_frame = GUI.createFrame(root)
    origin_combo = GUI.createComboBoxOrigin(combos_frame, "Origin Airports", origin_airports, updateDestAirportsList)
    dest_combo = GUI.createComboBoxOrigin(combos_frame, "Destination Airports", origin_airports, updateDestAirportsList)

    combo_dest = GUI.getFrameChild(dest_combo, "TCombobox")

    origin_combo.grid(column=0, row=0, padx=10)
    dest_combo.grid(column=1, row=0, padx=10)

    map = GUI.createMap(root)

    combos_frame.grid(column=0, row=0, pady=10)
    map.grid(column=0,row=1)

    """     manufacturers = backend.getColumnElement(planes_df, "manufacturer")
    GUI.createComboBoxManufacturer(root, "Plane manufacturers", manufacturers, updatePlaneModelsList)

    models = backend.getColumnElement(planes_df, "model")
    combo_model = GUI.createComboBoxModel(root, "Plane models", sorted(models), countModel)

    df = planes_df.filter(planes_df.manufacturer=="AIRBUS")
    data = backend.getCountedElements(df, 'model', 'engine').toPandas() """

    root.mainloop()

if __name__ == "__main__":
    main()
