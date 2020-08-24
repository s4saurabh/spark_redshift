import pyspark
from pyspark.sql import SQLContext
from pyspark import SparkContext
from pyspark.sql import SparkSession

sc = SparkContext.getOrCreate()
#sc = SparkSession.builder.appName("redshift").enableHiveSupport().getOrCreate()
sql_context = SQLContext(sc)

# Read data from a query
df = sql_context.read \
    .format("jdbc") \
    .option("jdbcdriver", "com.amazon.redshift.jdbc42.Driver") \
    .option("url", "jdbc:redshift://redshifthost:5439/database?user=username&password=pass")
    .option("query", "select * from orders") \
    .option("aws_iam_role", "arn:aws:iam::123456789000:role/redshift_iam_role") \
    .option("tempdir", "s3://path_to_temp_dir") \
    .load()

df.show()
