import GUI
import backend

def main():
    root = GUI.init("Flights Tracker")

    airports_df = backend.loadFile("./Datasets/airports.csv")
    flights_small_df = backend.loadFile("./Datasets/flights_small.csv")
    planes_df = backend.loadFile("./Datasets/planes.csv")

    manufacturers = backend.getColumnElement(planes_df, "manufacturer")
    GUI.createComboBox(root, "Plane manufacturers", manufacturers)

    models = backend.getColumnElement(planes_df.filter(planes_df.manufacturer=="AIRBUS INDUSTRIE"), "model")
    GUI.createComboBox(root, "Plane models", sorted(models))

    root.mainloop()

if __name__ == "__main__":
    main()
