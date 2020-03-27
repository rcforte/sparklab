from pyspark.sql import SparkSession

if __name__ == '__main__':
    linuxconf = '/home/rcforte/dev/tools/ignite/examples/config/example-ignite.xml'
    winconf = r'C:\Users\rcfor\Dev\Tools\ignite\examples\config\example-ignite.xml'

    conf = winconf

    spark = SparkSession\
        .builder\
        .appName('app')\
        .getOrCreate()

    df = spark\
        .read\
        .format('ignite')\
        .option('table', 'city')\
        .option('config', conf)\
        .load()
    df.createOrReplaceTempView('city')
    df.show()

    newrow = spark.sql('select (select max(id) from city) + 1 as id, "Stamford" as name')
    newrow\
        .write\
        .format('ignite')\
        .mode('append')\
        .option('table', 'city')\
        .option('config', conf)\
        .save()

    df.show()

    spark.stop()
