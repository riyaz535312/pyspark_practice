
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Window as W

spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

# Assume the dataframes products, sales, inventory are already initialized.

# Write the logic and display the final dataframe

#df=(products.join(sales,how='inner',on ='product_id')
#            .join(inventory,how='inner',on='product_id')
         #  .groupby('category','name','product_id')
         #  #.agg({'quantity':'sum','revenue': 'sum','stock':'sum'})
         #  .agg(F.sum("quantity").alias("total_quantity")
         #       ,F.sum("revenue").alias("total_revenue")
         #      ,F.sum("stock").alias("total_stock")) 
         #.fillna(0)
         #.orderBy('category','name','product_id')
  # )

sales_df=(sales.groupby('product_id')
          .agg(F.sum('quantity').alias('total_quantity')
               , F.sum("revenue").alias("total_revenue"))
         )
inventory_df=(
            inventory.groupby("product_id")
            .agg(F.sum("stock").alias("total_stock"))
)

# using left join because some products may not have sales or inventory for those we need to fill 0 as total_sales,toatl_revenue
result_df=(
            products.join(sales_df,how="left", on="product_id")
            .join(inventory_df,how='left',on="product_id")
            .fillna(0)
            .select('category','name','product_id','total_quantity','total_revenue','total_stock')
            .orderBy('category','name','product_id')
)


display(result_df)
#display(df_result)
    
