# spark_redshift

To run spark redshift example code you will need the Spark-RedShift JDBC driver. This example is for Amazon EMR and uses the default jdbc drivers that come as part of EMR cluster.

The jdbc driver is available on EMR master node at /usr/share/aws/redshift/jdbc/ .

**Authenticating to S3 and Redshift**

The use of the jdbc library involves several connections which must be authenticated / secured, all of which are illustrated in the following diagram:
```
                            ┌───────┐
       ┌───────────────────▶│  S3   │◀─────────────────┐
       │    IAM or keys     └───────┘    IAM or keys   │
       │                        ▲                      │
       │                        │ IAM or keys          │
       ▼                        ▼               ┌──────▼────┐
┌────────────┐            ┌───────────┐         │┌──────────┴┐
│  Redshift  │            │   Spark   │         ││   Spark   │
│            │◀──────────▶│  Driver   │◀────────▶┤ Executors │
└────────────┘            └───────────┘          └───────────┘
               JDBC with                  Configured
               username /                     in
                password                    Spark
            (can enable SSL)
```            
The jdbc library reads and writes data to S3 when transferring data to/from Redshift. As a result, it requires AWS credentials with read and write access to a S3 bucket (specified using the tempdir configuration parameter).

The following describes how each connection can be authenticated:

- **Spark driver to Redshift**: The Spark driver connects to Redshift via JDBC using a username and password.
    Redshift does not support the use of IAM roles to authenticate this connection.
    This connection can be secured using SSL; for more details, see the Encryption section below.

- **Spark to S3**: S3 acts as a middleman to store bulk data when reading from or writing to Redshift.
    Spark connects to S3 using both the Hadoop FileSystem interfaces and directly using the Amazon
    Java SDK's S3 client.

    This connection can be authenticated using either AWS keys or IAM roles. 

The example code redshift.py in this repo relies on using IAM role. This role should have the necessary permissions to the S3 bucket to store temporary data to/from RedShift.
    
To run redshift.py with Spark on EMR you need to provide the necessary jar and driver class path:

```spark-submit --driver-class-path /usr/share/aws/redshift/jdbc/RedshiftJDBC42.jar --jars /usr/share/aws/redshift/jdbc/RedshiftJDBC42.jar redshift.py```
