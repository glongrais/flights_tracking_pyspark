from pyspark import SparkContext
from pyspark.sql import SparkSession

sc = SparkContext("local", "Simple App")
spark = SparkSession.builder.getOrCreate()

def loadFile(path):
    return spark.read.csv(path, header=True)