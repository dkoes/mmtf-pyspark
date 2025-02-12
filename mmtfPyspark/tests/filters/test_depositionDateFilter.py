#!/usr/bin/env python

import unittest
from pyspark.sql import SparkSession
from mmtfPyspark.io.mmtfReader import download_mmtf_files
from mmtfPyspark.filters import DepositionDate


class DepositionDateFilterTest(unittest.TestCase):

    def setUp(self):
        self.spark = SparkSession.builder.master("local[*]") \
                                 .appName("DepositionDateFilterTest") \
                                 .getOrCreate()

        # 4MYA: deposited on 2013-09-27
        # 1O6Y: deposited on 2002-10-21
        # 3VCO: deposited on 2012-01-04
        # 5N0Y: deposited on 2017-02-03
        pdbIds = ['1O6Y', '4MYA', '3VCO', '5N0Y']
        self.pdb = download_mmtf_files(pdbIds)

    def test1(self):
        pdb_1 = self.pdb.filter(DepositionDate("2000-01-01", "2010-01-01"))
        results_1 = pdb_1.keys().collect()

        self.assertTrue('1O6Y' in results_1)
        self.assertFalse('4MYA' in results_1)
        self.assertFalse('3VCO' in results_1)
        self.assertFalse('5N0Y' in results_1)

    def test2(self):
        pdb_2 = self.pdb.filter(DepositionDate("2010-01-01", "2015-01-01"))
        results_2 = pdb_2.keys().collect()

        self.assertFalse('1O6Y' in results_2)
        self.assertTrue('4MYA' in results_2)
        self.assertTrue('3VCO' in results_2)
        self.assertFalse('5N0Y' in results_2)

    def test3(self):
        pdb_3 = self.pdb.filter(DepositionDate("2017-02-03", "2017-02-03"))
        results_3 = pdb_3.keys().collect()

        self.assertFalse('1O6Y' in results_3)
        self.assertFalse('4MYA' in results_3)
        self.assertFalse('3VCO' in results_3)
        self.assertTrue('5N0Y' in results_3)

    def tearDown(self):
        self.spark.stop()


if __name__ == '__main__':
    unittest.main()
