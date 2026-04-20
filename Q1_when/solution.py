
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Window as W

spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

# Assume the dataframes employees, payroll are already initialized.

df=employees.join(payroll, how='inner', on ='employee_id' )

df_result=df.withColumn('pay', 
    F.when(df.hours_worked<=40, df.hours_worked*df.hourly_rate)
    .otherwise((40 *df.hourly_rate) + 
               ((df.hours_worked-40)*(1.5 * df.hourly_rate)))
                       ).select('employee_id','name','pay','position')

display(df_result)
# Write the logic and display the final dataframe

#display(df_result)
    
