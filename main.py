import GUI
import backend

def main():
    root = GUI.init("Flights Tracker")

    airports_df = backend.loadFile("./Datasets/airports.csv")
    flights_small_df = backend.loadFile("./Datasets/flights_small.csv")
    planes_df = backend.loadFile("./Datasets/planes.csv")

    root.mainloop()

if __name__ == "__main__":
    main()
