from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("data_frame").getOrCreate()
# Create a simple DataFrame
data = [("Alice", 20), ("Bob", 25), ("Charlie", 30)]
df = spark.createDataFrame(data, ["Name", "Age"])

print(df.show())

spark.stop()
