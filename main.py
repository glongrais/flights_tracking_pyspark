import numpy as np
from tkinter import *
from pyspark import SparkContext
from pyspark.sql import SparkSession

sc = SparkContext("local", "Simple App")
spark = SparkSession.builder.getOrCreate()

airports_df = spark.read.csv("./Datasets/airports.csv", header=True)
flights_small_df = spark.read.csv("./Datasets/flights_small.csv", header=True)
planes_df = spark.read.csv("./Datasets/planes.csv", header=True)

planes_df.show()
