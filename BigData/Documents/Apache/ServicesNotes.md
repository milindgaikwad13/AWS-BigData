# Apache Services


## Scoop

* Import data from RDBMS , NOSQL to HDFS and vice versa
* command line to import export


## Flume

* Bring web server logs to HDFS
* Bring streaming data to HDFS
* Flume Agent
* Runs anywhere, Not required to be running on Hadoop cluster
* log4j: Flume client talk to log4j to get the log data

![flume](Images/Flume.png)

* Source : Source receive the data from client
* Channel: 
* Sink   : Sink pushes data to HDFS 


## Kafka

![kafka](Images/Kafka_1.png)

![kafka](Images/Kafka_points.png)



## Oozie

Workflow scheduler

![oozie](Images/Oozie.png)
![oozie](Images/Oozie_1.png)


## Hue

Interface on hadoop to run hive and pig scripts
Exploring HDFS

## Zookeeper

Coordinating your cluster

![Zookeeper](Images/Zookeeper_1.png)
![Zookeeper](Images/Zookeeper.png)


## Hive/Hcatalog 

* Metadata and table management system for Hadoop
* Relational view of data
* Serde ( eg. JSON) 
* metastore
* Supports HIVE DDL commands

## Solr

Solr is an open source enterprise search platform



