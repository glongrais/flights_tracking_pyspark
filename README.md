# Flights Tracking with Pyspark

### Table of Content

[Principles](#Principles)   
[Ressources](#Ressources)

## Principles

From this 3 datasets (airports.csv, flights.csv, planes.csv), build a browsing interface to visualise the data. For examples, the routes of one specific plane or type of plane, all the flights of a specific day or periods.

## Ressources  

- The data pipeline is handled by PySpark, the python version of [Apache Saprk](https://spark.apache.org).  
To install PySpark: 
````
pip install pyspark
`````
Additional information to install PySpark on MacOS can be found [here](https://sparkbyexamples.com/pyspark/how-to-install-pyspark-on-mac/).

- The graphic user interface is handled by [Tkinter](https://wiki.python.org/moin/TkInter) (Present by default in the python packages).

- The map is provided by [Tom Schimansky](https://github.com/TomSchimansky) with his custom Tkinter widget [TkinterMapView](https://github.com/TomSchimansky/TkinterMapView).  
To install TkinterMapView:
````
pip install tkintermapview
`````
