from multiprocessing import Process
from turtle import position
import pandas as pd
import GUI
import backend

def updateDestAirportsList(val):
    faa = backend.getFaaFromName(airports_df, val)
    dest = backend.getColumnElement(backend.filterElements(flights_small_df, flights_small_df.origin, faa), "dest")

    names_dest = []
    for n in dest:
        names_dest.append(backend.getNameFromFaa(airports_df, n))

    combo_dest['values']=sorted(names_dest)

    clearMarkers(markers_list)

    pos = backend.getAirportPosition(airports_df, [faa])
    map.set_marker(pos[0], pos[1], text=backend.getNameFromFaa(airports_df, faa))
    backend.getAirportPosition(airports_df, dest)
    #setDestMarkers(markers_list, dest)

    map.set_zoom(3)

def originMarkerClicked(marker):
    updateDestAirportsList(marker.text)

def clearMarkers(markers_list):
    for m in markers_list:
        m.delete()

def setDestMarkers(markers_list, dest_faa):
    global positions, names
    positions = []
    names = []
    processes = []

    for n in dest_faa:
        #pos = backend.getAirportPosition(airports_df, n)
        #marker = map.set_marker(pos[0], pos[1], text=backend.getNameFromFaa(airports_df, n), marker_color_circle="#4272f5", marker_color_outside="#1b57fa")
        #markers_list.append(marker)
        processes.append(Process(target=pushPositionandName, args=(n)))

    for p in processes:
        p.start()
    
    for p in processes:
        p.join()
    
    for i in range(len(positions)):
        marker = map.set_marker(positions[i][0], positions[i][1], text=names[i], marker_color_circle="#4272f5", marker_color_outside="#1b57fa")
        markers_list.append(marker)

def pushPositionandName(dest):
    pos = backend.getAirportPosition(airports_df, dest)
    name = backend.getNameFromFaa(airports_df, dest)
    #positions.append(pos)
    #names.append(name)

def main():

    global flights_small_df, airports_df, combo_dest, map, markers_list

    root = GUI.init("Flights Tracker",800,650)

    airports_df = backend.loadFile("./Datasets/airports.csv")
    flights_small_df = backend.loadFile("./Datasets/flights_small.csv")
    #planes_df = backend.loadFile("./Datasets/planes.csv")

    map = GUI.createMap(root)
    markers_list = []

    origin_airports = backend.getColumnElement(flights_small_df, "origin")
    pos = backend.getAirportPosition(airports_df, origin_airports)

    names_origin = []
    x = []
    y = []

    for n in origin_airports:
        airport_name = backend.getNameFromFaa(airports_df, n)
        names_origin.append(airport_name)
        p = pos[n]
        marker = map.set_marker(p[0], p[1], text=airport_name, command=originMarkerClicked)
        markers_list.append(marker)
        x.append(p[0])
        y.append(p[1])

    centroid = (sum(x) / len(x), sum(y) / len(y))
    map.set_position(centroid[0], centroid[1])
    map.set_zoom(7)

    combos_frame = GUI.createFrame(root)
    origin_combo = GUI.createComboBoxOrigin(combos_frame, "Origin Airports", names_origin, updateDestAirportsList)
    dest_combo = GUI.createComboBoxOrigin(combos_frame, "Destination Airports", origin_airports, updateDestAirportsList)

    combo_dest = GUI.getFrameChild(dest_combo, "TCombobox")

    origin_combo.grid(column=0, row=0, padx=10)
    dest_combo.grid(column=1, row=0, padx=10)

    combos_frame.grid(column=0, row=0, pady=10)
    map.grid(column=0,row=1)

    root.mainloop()

if __name__ == "__main__":
    main()
