# Using Spark SQL.

## Distributed Data
* Data Presence;
    * How Data can be present.
        * Data can be evenly distributed and all the memory and cores are available for processing. 
        This is ideal scenario.
        * Data is not sharded properly.
        * Data partitions vary and query can turn out to be very complex.
        * Data is skewed.
    * Reading Data. 
        * Spark gives a straight forward way
            * Spark RDD (Old Style)
            * Spark Dataframes / Datasets (New Style)
    * Initial Transformation.
        * Ones the data is read, one has to create tables to perform a spark sql-query. 
            * Tables can be created from one or more dataframes.
            * Store dataframe directly as table.
            * Hive Metadata helps!
## Optimizing Join Query
* Project Tungsten built over Catalyst Query Optimizer.
* Diff Types of Joins in Spark. (Distributed Computing.) 
    * Shuffle Hash Join
        * Essenstially performs Map-Reduce over Data
        * Map through table/DataFrames
        * Generate output key (hashed) based on the Fields of join.
        * Shuffle Datasets based on the output key.
        * Reduce the data from the two datasets. (Typically performs operation)
        
        >> This works best when data is distributed evenly 
        >> When more keys are present for parallelism. 
        Below is example.
        ```python
            output_df = spark.sql(""" 
                select act.account_number, act.account_holder_name, transaction.date as trans_month,
                sum(transaction.total_debit) as total_debit, sum(transaction.total_credit) as total_credit    
                from act join transaction on act.account_number = transaction.account_number;
            """) 
        ```
    * Broadcast Hast Join
        * 
    * Cartesian Join
    * Theta Join
## Perfrom Aggregations
