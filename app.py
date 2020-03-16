from pyspark.sql import SparkSession

if __name__ == '__main__':
    spark = SparkSession\
        .builder\
        .appName('app')\
        .getOrCreate()

    df = spark\
        .read\
        .format('ignite')\
        .option('table', 'city')\
        .option('config', '/home/rcforte/dev/tools/ignite/examples/config/example-ignite.xml')\
        .load()
    df.createOrReplaceTempView('city')
    df.show()

    newrow = spark.sql('select (select max(id) from city) + 1 as id, "Stamford" as name')
    newrow\
        .write\
        .format('ignite')\
        .mode('append')\
        .option('table', 'city')\
        .option('config', '/home/rcforte/dev/tools/ignite/examples/config/example-ignite.xml')\
        .save()

    df.show()

    spark.stop()
