from pyspark import SparkContext
from pyspark.sql import SparkSession

sc = SparkContext("local", "Simple App")
spark = SparkSession.builder.master('local[*]').getOrCreate()

def loadFile(path):
    return spark.read.csv(path, header=True)

def getColumnElement(df, col_name):
    return df.select(col_name).distinct().rdd.map(lambda r: r[0]).collect()

def filterElements(df, col, val):
    return df.filter(col==val)

def getCountedElements(df, col1, col2):
    return df[[col1,col2]].groupby(col1).count()

def getFaaFromName(df, name):
    res =df.filter(df.name==name).collect()[0]['faa']
    return res

def getNameFromFaa(df, faa):
    res =df.filter(df.faa==faa).collect()[0]['name']
    return res

def getAirportPosition(df, faa):
    res = {}
    rows = df.filter(df.faa.isin(faa)).collect()
    for r in rows:
        res[r['faa']] = (float(r['lat']), float(r['lon']))

    return res
