from pyspark import SparkConf,SparkContext


conf = SparkConf().setMaster('local').setAppName('customerMaxPurchaseAmount')
sc = SparkContext(conf= conf)

def parseCSVFile(test):
    fileContaints = test.split(',')
    return(int(fileContaints[0]), float(fileContaints[2]))


file = sc.textFile('PySpark/src/samples/SparkBasic/excercise/customer-orders.csv')

customerSpending = file.map(parseCSVFile).reduceByKey(lambda x,y: x+y).map(lambda x:(x[1],x[0])).sortByKey().collect()

for spending,customer in customerSpending:
    print(f"{customer} spent: {spending}")