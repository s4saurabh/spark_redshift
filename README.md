# spark_redshift

To run spark redshift example code you will need the Spark-RedShift JDBC driver. This example is for Amazon EMR and uses the default jdbc drivers that come as part of EMR cluster.

The jdbc driver is available on EMR master node at /usr/share/aws/redshift/jdbc/ .

To run redshift.py with Spark on EMR you need to provide the necessary jar and driver class path:

spark-submit --driver-class-path /usr/share/aws/redshift/jdbc/RedshiftJDBC42.jar --jars /usr/share/aws/redshift/jdbc/RedshiftJDBC42.jar redshift.py
