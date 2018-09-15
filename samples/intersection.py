from pyspark import SparkContext, SparkConf

def isNotHeader(line: str):
    return not (line.startswith("host") and "bytes" in line)

if __name__ == "__main__":
    conf = SparkConf().setAppName("unionLogs").setMaster("local[*]")
    sc = SparkContext(conf = conf)

    ## Read Data from local text files
    julyFirstLogs = sc.textFile("in/nasa_19950701.tsv")
    augustFirstLogs = sc.textFile("in/nasa_19950801.tsv")

    ## Shape data format. In this case, just pick out the first element from the raw data.
    julyFirstLogs = julyFirstLogs.map(lambda line: line.split("\t")[0]));
    augustFirstLogs =augustFirstLogs.map(lambda line: line.split("\t")[0]));

    # intersection...https://en.wikipedia.org/wiki/Intersection_(set_theory)
    intersection = julyFirstLogs.intersection(augustFirstLogs)

    # Exclude header lines from the data
    cleanLogLines = aggregatedLogLines.filter(isNotHeader)
    sample = cleanLogLines.sample(withReplacement = True, fraction = 0.1)

    sample.saveAsTextFile("out/sample_nasa_logs.csv")
