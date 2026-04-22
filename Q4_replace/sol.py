from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Window as W
import pyspark
import datetime
import json

spark = SparkSession.builder.appName('run-pyspark-code').getOrCreate()

def etl(social_media):
    # Write code here
    result_df=(social_media
               .select('comments','date','id','likes','platform','shares',F.regexp_replace(F.col('text'),'Python','PySpark').alias('text'))
              ).fillna({'id':0,'text':''}).orderBy('comments')
    return result_df
    





    
