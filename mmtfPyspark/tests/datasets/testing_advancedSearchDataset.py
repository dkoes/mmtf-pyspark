import unittest

from pyspark.sql import SparkSession

from mmtfPyspark.datasets import advancedSearchDataset

spark = SparkSession.builder.master("local[*]") \
            .appName("AdvancedSearchDatasetTest") \
            .getOrCreate()

query = (
    "<orgPdbQuery>"
    "<queryType>org.pdb.query.simple.StoichiometryQuery</queryType>"
    "<stoichiometry>A3B3C3</stoichiometry>"
    "</orgPdbQuery>"
)

ds = advancedSearchDataset.get_dataset(query)
print(ds)
