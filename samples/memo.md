## what is RDD?
 -> Resilient Distributed Datasets

Resilient:
able to quickly become healthy, happy, or strong again
after an illness, disappointment, or other problem

## Connectors
 Spark JDBC driver:
 https://docs.databricks.com/spark/latest/data-sources/sql-databases.html

 Spark Cassandra connector:
 http://www.datastax.com/dev/blog/kindling-an-introduction-to-spark-with-cassandra-part-1

 Spark Elasticsearch connector:
 https://www.elastic.co/guide/en/elasticsearch/hadoop/current/spark.html

## その他
 ↓あとで整理する
 distinctは重い・・・シャッフルしてから重複を排除するため
 使用例: sc.parallelize([1,1,2,3]).distinct().collect() => [1,2,3]

 union(self, other)・・・集合A,Bの全体を返す
 ```
 julyFirstLogs = sc.textFile("in/nasa_19950701.tsv")
 augustFirstLogs = sc.textFile("in/nasa_19950801.tsv")

 aggregatedLogLines = julyFirstLogs.union(augustFirstLogs)
 ```

 intersection(self, other)・・・集合A,Bの重複部分のみを返す
 subtract(self, other, numPartitions=None)・・・集合Aから集合A,Bの重複部分を除いた集合A'を返す
 cartesian(self, other)・・・集合A,Bに含まれる要素のペアで作れるすべての組みあわせを返す

 Action
  - collect
  - count
  - countByValue 。。。UniqueなValueをカウント
  - take ・・・デバッグに使える。ｎ個の要素を取得！
  - saveAsTextFile
  - reduce

Spark components
 - Spark sql
 - Spark streaming
 - Spark MLib -> pysparkはこれに含まれる
 - Graph X

 Pair RDD -> Key Value Storeのこと
