from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Window as W
import pyspark
import datetime
import json

spark = SparkSession.builder.appName('run-pyspark-code').getOrCreate()

def etl(input_df):
    
    # Write code here
    result_df=input_df.select(
#(F.concat(F.repeat(F.col("*"),F.lit(F.length(F.col("phone"))-4)),F.right(F.col("phone"),4))).alias('anon_phone')) this won't work because repeat(col,number) will take constant value but we have given column expression which will execute at runtime
    F.expr("concat(repeat('*',length(phone)-4),right(phone,4))").alias("anon_phone"),
        F.regexp_extract(F.col('email'),'@(.+)',1).alias('email_domain') ,'user_id').na.fill({'anon_phone':0,'email_domain':'','user_id':0}).orderBy(F.col('anon_phone').asc())
     
    return result_df




    
