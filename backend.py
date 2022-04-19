from pyspark import SparkContext
from pyspark.sql import SparkSession

sc = SparkContext("local", "Simple App")
spark = SparkSession.builder.getOrCreate()

def loadFile(path):
    return spark.read.csv(path, header=True)

def getColumnElement(df, col_name):
    return df.select(col_name).distinct().rdd.map(lambda r: r[0]).collect()