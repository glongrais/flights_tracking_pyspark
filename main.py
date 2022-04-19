from pydoc import ModuleScanner
import GUI
import backend

def updatePlaneModelsList(val):
    global planes_df
    models = backend.getColumnElement(backend.filterElements(planes_df, planes_df.manufacturer, val), "model")
    combo_model['values']=sorted(models)

def main():
    root = GUI.init("Flights Tracker")
    global planes_df, combo_model
    airports_df = backend.loadFile("./Datasets/airports.csv")
    flights_small_df = backend.loadFile("./Datasets/flights_small.csv")
    planes_df = backend.loadFile("./Datasets/planes.csv")

    manufacturers = backend.getColumnElement(planes_df, "manufacturer")
    GUI.createComboBoxManufacturer(root, "Plane manufacturers", manufacturers, updatePlaneModelsList)

    models = backend.getColumnElement(planes_df, "model")
    combo_model = GUI.createComboBoxModel(root, "Plane models", sorted(models), updatePlaneModelsList)

    root.mainloop()

if __name__ == "__main__":
    main()
