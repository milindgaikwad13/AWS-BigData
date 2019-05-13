
## AVRO

* 4 years more mature than parquet
* Spark and impala and pig 
* serizalied : Schema is stored along with data
* Send data across network ( flume logs)
* Sqoop generates Avro schema from RDBMS metadata
* Snappy for compression and decompression fast
* Spark SQL with Avro is good
* Spark Streaming

## PARQUET
* columnar format
* google
* nested data ( hierarchy data)


## ORC
* columnar format
* facebook
* Better for predicate pushdown
* ACID
* better compression than parquet


## Predicate Pushdown
* Optimization engine
* spark catalyst optimizer 
* file stores statistics about partitions ( eg. max value , min value)
* acts as statistics
* bloomfilters :  
    * Data structure: to find if record present in dataset or not 



